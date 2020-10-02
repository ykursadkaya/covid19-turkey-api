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

keysTRtoENCategory = {
    'daily': {
        'gunluk_test': 'test',
        'gunluk_vaka': 'case',
        'gunluk_vefat': 'death',
        'gunluk_iyilesen': 'recovered'
    },
    'total': {
        'toplam_test': 'test',
        'toplam_vaka': 'case',
        'toplam_vefat': 'death',
        'toplam_iyilesen': 'recovered',
        'toplam_yogun_bakim': 'icuPatient',
        'toplam_entube': 'intubatedPatient',
        'agir_hasta_sayisi': 'seriouslyIllPatient'
    },
    'weekly': {
        'hastalarda_zaturre_oran': 'pneumoniaRate',
        'yatak_doluluk_orani': 'hospitalBedOccupancyRate',
        'eriskin_yogun_bakim_doluluk_orani': 'adultIcuOccupancyRate',
        'ventilator_doluluk_orani': 'ventilatorOccupancyRate',
        'ortalama_filyasyon_suresi': 'averageFiliationTime',
        'ortalama_temasli_tespit_suresi': 'averagePositiveContactDetectionTime',
        'filyasyon_orani': 'filiationRate'
    }
}

percentKeys = [
    'hastalarda_zaturre_oran',
    'yatak_doluluk_orani',
    'eriskin_yogun_bakim_doluluk_orani',
    'ventilator_doluluk_orani',
    'filyasyon_orani'
]


class TimerThread(Thread):
    def __init__(self, event, interval, func, *args, **kwargs):
        Thread.__init__(self)
        self.stopped = event
        self.interval = interval
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while not self.stopped.wait(self.interval):
            self.func(*self.args, **self.kwargs)


def getStats(query):
    try:
        response = requests.get(apiURL + query)
        stats = response.json()

        return stats
    except Exception as e:
        print('>>>[ERROR] Cannot get data!', e)
        return None


def convertDayStats(dayStats):
    dayDict = {category: {} for category in keysTRtoENCategory.keys()}

    for category, origKeyDict in keysTRtoENCategory.items():
        for originalKey, translatedKey in origKeyDict.items():
            if (value := dayStats[originalKey]) != '':
                func, replacement = (float, (',', '.')) if originalKey in percentKeys else (int, ('.', ''))
                dayDict[category][translatedKey] = func(value.replace(*replacement))
            else:
                dayDict[category][translatedKey] = None

    return dayDict


def statsListToDict(stats):
    allDict = {}

    for dayStats in stats[::-1]:
        date = dateSeparator.join(dayStats.pop('tarih').split('.')[::-1])
        allDict[date] = convertDayStats(dayStats)

    return allDict


def generateTimeseries(allDict):
    timeSeriesDict = {category: {key: [] for key in keyDict.values()} for category, keyDict in keysTRtoENCategory.items()}

    for dataCategory, categoryDict in timeSeriesDict.items():
        for dataName, dataArray in categoryDict.items():
            for dayStats in allDict.values():
                dataArray.append(dayStats[dataCategory][dataName])
    timeSeriesDict['dates'] = list(allDict.keys())

    return timeSeriesDict


def routine():
    global allStats, allStatsDict, todayStatsDict, timeSeriesData

    allResponse = getStats(allQuery)
    if (allResponse != allStats) and (allResponse is not None):
        allStats = list(allResponse)
        allStatsDict = statsListToDict(allStats)
        lastDate = sorted(list(allStatsDict.keys()), reverse=True)[0]
        todayStatsDict = {lastDate: dict(allStatsDict[lastDate])}
        timeSeriesData = generateTimeseries(allStatsDict)


@app.route('/', methods=['GET'])
@app.route('/today-all', methods=['GET'])
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


@app.route('/weekly', methods=['GET'])
def getWeek():
    if (todayStatsDict != {}) and (todayStatsDict is not None):
        date, responseDict = dict(todayStatsDict).popitem()
        responseDict = responseDict['weekly']
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


@app.route('/timeseries/weekly/<string:dataname>', methods=['GET'])
def getWeeklyTimeseries(dataname):
    if (timeSeriesData != {}) and (timeSeriesData is not None):
        if timeSeriesData.get('weekly', None) is not None:
            if dataname in timeSeriesData['weekly']:
                responseDict = {'weekly': {dataname: timeSeriesData['weekly'][dataname]},
                                'dates': timeSeriesData['dates']}

                return jsonify(responseDict), 200
            else:
                return 'Timeseries weekly data can only be ' + str(list(timeSeriesData['weekly'].keys())) + '!', 404
        else:
            return '', 404
    else:
        return '', 404


if __name__ == '__main__':
    routine()
    stopFlag = Event()
    thread = TimerThread(stopFlag, checkInterval, routine)
    thread.start()
    app.run(debug=False, port=5000, host='0.0.0.0')
