# COVID-19 Turkey Statistics API

Provides information about COVID-19 in Turkey.

- Gets data directly from **Republic of Turkey Ministry of Health COVID-19 information website**.
  - Last day's statistics:
    - **[TR]** [https://covid19.saglik.gov.tr/](https://covid19.saglik.gov.tr/?_Dil=1)
    - **[EN]** [https://covid19.saglik.gov.tr/?_Dil=2](https://covid19.saglik.gov.tr/?_Dil=2)
  - All statistics:
    - **[TR]** [https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html](https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html)
    - **[EN]** [https://covid19.saglik.gov.tr/EN-69532/general-coronavirus-table.html](https://covid19.saglik.gov.tr/EN-69532/general-coronavirus-table.html)
- Checks the website every n (default is 300 in script) seconds, if anything changes in the stats script updates it's own data.
- Provides an API for today's data, total data and a timeseries dataset for days.



## Setup

### Run on a Docker container

1. Clone this repository

   ```bash
   git clone https://github.com/ykursadkaya/covid19-turkey-api.git
   cd covid19-turkey-api
   ```

2. Build Docker image

   ```bash
   docker build -t covidapi .
   ```

3. Run container

   ```bash
   docker run -p <external-port>:5000 --name <container-name> covidapi
   ```



### Run directly on your machine

1. Install Python 3.8.x or later (script has walrus assignment)

   [Python Download Page](https://www.python.org/downloads/)

2. Install pip for Python3

   [pip installation guide](https://pip.pypa.io/en/stable/installing/)

3. Clone this repository

   ```bash
   git clone https://github.com/ykursadkaya/covid19-turkey-api.git
   cd covid19-turkey-api
   ```

4. Install required Python packages

   ```bash
   pip3 install -r requirements.txt
   ```

5. Run [script](./covidbot.py)

   ```bash
   python3 app.py
   ```



### [API Documentation](./APIDOC.md)