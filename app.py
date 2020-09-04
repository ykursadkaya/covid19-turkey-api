from flask import Flask, request, jsonify
import requests
from threading import Event, Thread

app = Flask(__name__)
app.url_map.strict_slashes = False

allStats = []
allStatsDict = {}
todayStatsDict = {}
timeSeriesData = {}

dateSeparator = '/'
apiURL = 'https://covid19.saglik.gov.tr/covid19api'
todayQuery = '?getir=sondurum'
allQuery = '?getir=liste'
checkInterval = 5 * 60  # seconds

keysTRtoEN = {
    'tarih': 'date',
    'gunluk_test': 'test',
    'gunluk_vaka': 'case',
    'gunluk_vefat': 'death',
    'gunluk_iyilesen': 'recovered',
    'toplam_test': 'test',
    'toplam_vaka': 'case',
    'toplam_vefat': 'death',
    'toplam_iyilesen': 'recovered',
    'toplam_yogun_bakim': 'icuPatient',
    'toplam_entube': 'intubatedPatient',
    'hastalarda_zaturre_oran': 'pneumoniaPercent',
    'agir_hasta_sayisi': 'seriouslyIllPatient'
}


class TimerThread(Thread):
    def __init__(self, event, func, *args, **kwargs):
        Thread.__init__(self)
        self.stopped = event
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while not self.stopped.wait(checkInterval):
            self.func(*self.args, **self.kwargs)


def getStats(query):
    try:
        response = requests.get(apiURL + query)
        stats = response.json()

        return stats
    except Exception as e:
        print('>>>[ERROR] Cannot get data!', e)
        return None


def statsListToDict(stats):
    allDict = {}
    previousDayStats = {
        'gunluk_vaka': '0',
        'gunluk_vefat': '0',
        'gunluk_iyilesen': '0',
        'toplam_vaka': '0',
        'toplam_vefat': '0',
        'toplam_iyilesen': '0',
    }

    for dayStats in stats[::-1]:
        date = dateSeparator.join(dayStats.pop('tarih').split('.')[::-1])
        allDict[date] = {'daily': {}, 'total': {}}
        for key, value in dayStats.items():
            if key.startswith('gunluk'):
                if value != '':
                    allDict[date]['daily'][keysTRtoEN[key]] = int(value.replace('.', ''))
                else:
                    totalKey = 'toplam_' + key.split('_')[1]
                    if (previousValue := previousDayStats.get(totalKey, None)) and \
                            (dayValue := dayStats.get(totalKey, None)):
                        allDict[date]['daily'][keysTRtoEN[key]] = int(dayValue.replace('.', '')) \
                                                                  - int(previousValue.replace('.', ''))
                    else:
                        allDict[date]['daily'][keysTRtoEN[key]] = None
            else:
                if value != '':
                    if keysTRtoEN[key] == 'pneumoniaPercent':
                        allDict[date]['total'][keysTRtoEN[key]] = float(value.replace(',', '.'))
                    else:
                        allDict[date]['total'][keysTRtoEN[key]] = int(value.replace('.', ''))
                else:
                    if (keysTRtoEN[key] == 'death') or (keysTRtoEN[key] == 'recovered'):
                        allDict[date]['total'][keysTRtoEN[key]] = 0
                    else:
                        allDict[date]['total'][keysTRtoEN[key]] = None
        previousDayStats = dict(dayStats)

    return allDict


def generateTimeseries(allDict):
    timeSeriesDict = {'daily': {'test': [], 'case': [], 'death': [], 'recovered': []},
                      'total': {'test': [], 'case': [], 'death': [], 'recovered': [], 'icuPatient': [],
                                'intubatedPatient': [], 'pneumoniaPercent': [], 'seriouslyIllPatient': []}}
    dates = list(allDict.keys())

    for dataType, dictArray in timeSeriesDict.items():
        for dataName, dataArray in dictArray.items():
            for date, dayStats in allDict.items():
                dataArray.append(dayStats[dataType][dataName])
    timeSeriesDict['dates'] = dates

    return timeSeriesDict


def routine():
    global allStats, allStatsDict, todayStatsDict, timeSeriesData

    allResponse = getStats(allQuery)
    if (allResponse != allStats) and (allResponse is not None):
        allStats = allResponse
        allStatsDict = statsListToDict(allStats)
        lastDate = sorted(list(allStatsDict.keys()), reverse=True)[0]
        todayStatsDict = {lastDate: allStatsDict[lastDate]}
        timeSeriesData = generateTimeseries(allStatsDict)


@app.route('/', methods=['GET'])
@app.route('/today_all', methods=['GET'])
def getTodayAll():
    if (todayStatsDict != {}) and (todayStatsDict is not None):
        date, responseDict = dict(todayStatsDict).popitem()
        responseDict['date'] = date

        return jsonify(responseDict), 200
    else:
        return '', 404


@app.route('/today', methods=['GET'])
@app.route('/daily', methods=['GET'])
def getToday():
    if (todayStatsDict != {}) and (todayStatsDict is not None):
        date, responseDict = dict(todayStatsDict).popitem()
        responseDict = responseDict['daily']
        responseDict['date'] = date

        return jsonify(responseDict), 200
    else:
        return '', 404


@app.route('/total', methods=['GET'])
def getTotal():
    if (todayStatsDict != {}) and (todayStatsDict is not None):
        date, responseDict = dict(todayStatsDict).popitem()
        responseDict = responseDict['total']
        responseDict['date'] = date

        return jsonify(responseDict), 200
    else:
        return '', 404


@app.route('/date', methods=['GET', 'POST'])
def getDate():
    if (allStatsDict != {}) and (allStatsDict is not None):
        if request.method == 'GET':
            requestDict = request.args
        elif request.method == 'POST':
            requestDict = request.get_json()
        else:
            return '', 400

        if year := requestDict.get('year', None):
            responseDict = {k: v for k, v in allStatsDict.items() if k.startswith(str(year))}
            if month := requestDict.get('month', None):
                responseDict = {k: v for k, v in responseDict.items() if k.startswith(str(year) + '/' + str(month))}
                if day := requestDict.get('day', None):
                    responseDate = f'{str(year)}/{str(month)}/{str(day)}'
                    responseDict = {responseDate: responseDict.get(responseDate, None)}
        else:
            responseDict = None
            return 'You must specify at least the year!', 400

        return jsonify(responseDict), 200
    else:
        return '', 404


@app.route('/dataset', methods=['GET'])
@app.route('/all', methods=['GET'])
def getDataset():
    if (allStatsDict != {}) and (allStatsDict is not None):
        responseDict = dict(allStatsDict)

        return jsonify(responseDict), 200
    else:
        return '', 404


@app.route('/timeseries', methods=['GET'])
@app.route('/timeseries/all', methods=['GET'])
def getTimeseries():
    if (timeSeriesData != {}) and (timeSeriesData is not None):
        responseDict = dict(timeSeriesData)

        return jsonify(responseDict), 200
    else:
        return '', 404


@app.route('/timeseries/<string:datatype>', methods=['GET'])
@app.route('/timeseries/<string:datatype>/all', methods=['GET'])
def getTimeseriesType(datatype):
    if (datatype in timeSeriesData.keys()) and (datatype != 'dates'):
        if (timeSeriesData != {}) and (timeSeriesData is not None):
            if timeSeriesData.get(datatype, None) is not None:
                responseDict = {datatype: timeSeriesData[datatype], 'dates': timeSeriesData['dates']}

                return jsonify(responseDict), 200
            else:
                return '', 404
        else:
            return '', 404
    else:
        endpointList = list(timeSeriesData.keys())
        endpointList.remove('dates')
        return 'Timeseries data can only be ' + str(endpointList) + '!', 400


@app.route('/timeseries/daily/<string:dataname>', methods=['GET'])
def getDailyTimeseries(dataname):
    if (timeSeriesData != {}) and (timeSeriesData is not None):
        if timeSeriesData.get('daily', None) is not None:
            if dataname in timeSeriesData['daily']:
                responseDict = {'daily': {dataname: timeSeriesData['daily'][dataname]},
                                'dates': timeSeriesData['dates']}

                return jsonify(responseDict), 200
            else:
                return 'Timeseries daily data can only be ' + str(list(timeSeriesData['daily'].keys())) + '!', 404
        else:
            return '', 404
    else:
        return '', 404


@app.route('/timeseries/total/<string:dataname>', methods=['GET'])
def getTotalTimeseries(dataname):
    if (timeSeriesData != {}) and (timeSeriesData is not None):
        if timeSeriesData.get('total', None) is not None:
            if dataname in timeSeriesData['total']:
                responseDict = {'total': {dataname: timeSeriesData['total'][dataname]},
                                'dates': timeSeriesData['dates']}

                return jsonify(responseDict), 200
            else:
                return 'Timeseries total data can only be ' + str(list(timeSeriesData['total'].keys())) + '!', 404
        else:
            return '', 404
    else:
        return '', 404


if __name__ == '__main__':
    routine()
    stopFlag = Event()
    thread = TimerThread(stopFlag, routine)
    thread.start()
    app.run(debug=False, port=5000, host='0.0.0.0')
