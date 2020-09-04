

## API Documentation

### Index

- **[Basic Data](#basic-data)**
  - **[Today All Data](#today-all-data)**
  - **[Today Data](#today-data)**
  - **[Total Data](#today-data)**
  - **[Specific Date's Data](#specific-dates-data)**
- **[Datasets](#datasets)**
  - **[All Dataset](#all-dataset)**
  - **[All Timeseries Dataset](#all-timeseries-dataset)**
  - **[Typed Timeseries Dataset](#typed-timeseries-dataset)**
  - **[Named Timeseries Dataset](#named-timeseries-dataset)**

### *Basic* Data

### Today All Data

Use to get today's and total data until today.

**URL:** `/`

**URL:** `/today_all/`

**Method:** `GET`

**Auth required:** No

#### Success Response

**Code:** `200 OK`

**Content example**

```json
{
    "daily": {
        "case": 1642,
        "death": 49,
        "recovered": 1211,
        "test": 110225
    },
    "date": "2020/09/03",
    "total": {
        "case": 274943,
        "death": 6511,
        "icuPatient": null,
        "intubatedPatient": null,
        "pneumoniaPercent": 7.6,
        "recovered": 248087,
        "seriouslyIllPatient": 1041,
        "test": 7466087
    }
}
```

#### Error Response

**Code:** `404 NOT FOUND`



### Today Data

Use to get today's data.

**URL:** `/today/`

**URL:** `/daily/`

**Method:** `GET`

**Auth required:** No

#### Success Response

**Code:** `200 OK`

**Content example**

```json
{
    "case": 1642,
    "date": "2020/09/03",
    "death": 49,
    "recovered": 1211,
    "test": 110225
}
```

#### Error Response

**Code:** `404 NOT FOUND`



### Total Data

Use to get total data until today.

**URL:** `/total/`

**Method:** `GET`

**Auth required:** No

#### Success Response

**Code:** `200 OK`

**Content example**

```json
{
    "case": 274943,
    "date": "2020/09/03",
    "death": 6511,
    "icuPatient": null,
    "intubatedPatient": null,
    "pneumoniaPercent": 7.6,
    "recovered": 248087,
    "seriouslyIllPatient": 1041,
    "test": 7466087
}
```

#### Error Response

**Code:** `404 NOT FOUND`



### Specific Date's Data

Use to get specified date's data.

**URL:** `/date/`

**Parameters:** `'year', 'month', day `

- Must specify at least year.
- Parameter list are ordered.
  - For example: If you specify year and month but not the day, you will get specified year's specified month's data.

**Example request:**  `GET /date?year=2020&month=09&day=01`

​								`GET /date?year=2020&month=09`

**Method:** `GET`, `POST` 

- If request is POST, send parameters in JSON body.

  - For example:

    ```json
    POST /date/
    
    {
        "year": "2020",
        "month": "09",
        "day": "01"
    }
    ```

    

**Auth required:** No

#### Success Response

**Code:** `200 OK`

**Content example**

```json
{
    "2020/09/01": {
        "daily": {
            "case": 1572,
            "death": 47,
            "recovered": 1003,
            "test": 109443
        },
        "total": {
            "case": 271705,
            "death": 6417,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.6,
            "recovered": 245929,
            "seriouslyIllPatient": 991,
            "test": 7247935
        }
    },
    "2020/09/02": {
        "daily": {
            "case": 1596,
            "death": 45,
            "recovered": 947,
            "test": 107927
        },
        "total": {
            "case": 273301,
            "death": 6462,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.6,
            "recovered": 246876,
            "seriouslyIllPatient": 1017,
            "test": 7355862
        }
    },
    "2020/09/03": {
        "daily": {
            "case": 1642,
            "death": 49,
            "recovered": 1211,
            "test": 110225
        },
        "total": {
            "case": 274943,
            "death": 6511,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.6,
            "recovered": 248087,
            "seriouslyIllPatient": 1041,
            "test": 7466087
        }
    }
}
```

#### Error Response

**Code:** `404 NOT FOUND`



### *Datasets*

### All Dataset

Use to get cases all data sorted by day.

**URL:** `/dataset/`

**URL:** `/all/`

**Method:** `GET`

**Auth required:** No

#### Success Response

**Code:** `200 OK`

**Content example**

```json
{
    "2020/03/11": {
        "daily": {
            "case": 1,
            "death": null,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 1,
            "death": 0,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/12": {
        "daily": {
            "case": 0,
            "death": null,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 1,
            "death": 0,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/13": {
        "daily": {
            "case": 4,
            "death": null,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 5,
            "death": 0,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/14": {
        "daily": {
            "case": 1,
            "death": null,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 6,
            "death": 0,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/15": {
        "daily": {
            "case": 12,
            "death": null,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 18,
            "death": 0,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/16": {
        "daily": {
            "case": 29,
            "death": null,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 47,
            "death": 0,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/17": {
        "daily": {
            "case": 51,
            "death": null,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 98,
            "death": 1,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/18": {
        "daily": {
            "case": 93,
            "death": 1,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 191,
            "death": 2,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/19": {
        "daily": {
            "case": 168,
            "death": 2,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 359,
            "death": 4,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/20": {
        "daily": {
            "case": 311,
            "death": 5,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 670,
            "death": 9,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/21": {
        "daily": {
            "case": 277,
            "death": 12,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 947,
            "death": 21,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/22": {
        "daily": {
            "case": 289,
            "death": 9,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 1236,
            "death": 30,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/23": {
        "daily": {
            "case": 293,
            "death": 7,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 1529,
            "death": 37,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/24": {
        "daily": {
            "case": 343,
            "death": 7,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 1872,
            "death": 44,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/25": {
        "daily": {
            "case": 561,
            "death": 15,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 2433,
            "death": 59,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/26": {
        "daily": {
            "case": 1196,
            "death": 16,
            "recovered": null,
            "test": null
        },
        "total": {
            "case": 3629,
            "death": 75,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": null,
            "recovered": 0,
            "seriouslyIllPatient": null,
            "test": null
        }
    },
    "2020/03/27": {
        "daily": {
            "case": 2069,
            "death": 17,
            "recovered": null,
            "test": 7533
        },
        "total": {
            "case": 5698,
            "death": 92,
            "icuPatient": 344,
            "intubatedPatient": 241,
            "pneumoniaPercent": null,
            "recovered": 42,
            "seriouslyIllPatient": null,
            "test": 47823
        }
    },
    "2020/03/28": {
        "daily": {
            "case": 1704,
            "death": 16,
            "recovered": 28,
            "test": 7641
        },
        "total": {
            "case": 7402,
            "death": 108,
            "icuPatient": 445,
            "intubatedPatient": 309,
            "pneumoniaPercent": null,
            "recovered": 70,
            "seriouslyIllPatient": null,
            "test": 55464
        }
    },
    "2020/03/29": {
        "daily": {
            "case": 1815,
            "death": 23,
            "recovered": 35,
            "test": 9982
        },
        "total": {
            "case": 9217,
            "death": 131,
            "icuPatient": 568,
            "intubatedPatient": 394,
            "pneumoniaPercent": null,
            "recovered": 105,
            "seriouslyIllPatient": null,
            "test": 65446
        }
    },
    "2020/03/30": {
        "daily": {
            "case": 1610,
            "death": 37,
            "recovered": 57,
            "test": 11535
        },
        "total": {
            "case": 10827,
            "death": 168,
            "icuPatient": 725,
            "intubatedPatient": 523,
            "pneumoniaPercent": null,
            "recovered": 162,
            "seriouslyIllPatient": null,
            "test": 76981
        }
    },
    "2020/03/31": {
        "daily": {
            "case": 2704,
            "death": 46,
            "recovered": 81,
            "test": 15422
        },
        "total": {
            "case": 13531,
            "death": 214,
            "icuPatient": 847,
            "intubatedPatient": 622,
            "pneumoniaPercent": null,
            "recovered": 243,
            "seriouslyIllPatient": null,
            "test": 92403
        }
    },
    "2020/04/01": {
        "daily": {
            "case": 2148,
            "death": 63,
            "recovered": 90,
            "test": 14396
        },
        "total": {
            "case": 15679,
            "death": 277,
            "icuPatient": 979,
            "intubatedPatient": 692,
            "pneumoniaPercent": null,
            "recovered": 333,
            "seriouslyIllPatient": null,
            "test": 106799
        }
    },
    "2020/04/02": {
        "daily": {
            "case": 2456,
            "death": 79,
            "recovered": 82,
            "test": 18757
        },
        "total": {
            "case": 18135,
            "death": 356,
            "icuPatient": 1101,
            "intubatedPatient": 783,
            "pneumoniaPercent": null,
            "recovered": 415,
            "seriouslyIllPatient": null,
            "test": 125556
        }
    },
    "2020/04/03": {
        "daily": {
            "case": 2786,
            "death": 69,
            "recovered": 69,
            "test": 16160
        },
        "total": {
            "case": 20921,
            "death": 425,
            "icuPatient": 1251,
            "intubatedPatient": 867,
            "pneumoniaPercent": null,
            "recovered": 484,
            "seriouslyIllPatient": null,
            "test": 141716
        }
    },
    "2020/04/04": {
        "daily": {
            "case": 3013,
            "death": 76,
            "recovered": 302,
            "test": 19664
        },
        "total": {
            "case": 23934,
            "death": 501,
            "icuPatient": 1311,
            "intubatedPatient": 909,
            "pneumoniaPercent": null,
            "recovered": 786,
            "seriouslyIllPatient": null,
            "test": 161380
        }
    },
    "2020/04/05": {
        "daily": {
            "case": 3135,
            "death": 73,
            "recovered": 256,
            "test": 20065
        },
        "total": {
            "case": 27069,
            "death": 574,
            "icuPatient": 1381,
            "intubatedPatient": 935,
            "pneumoniaPercent": null,
            "recovered": 1042,
            "seriouslyIllPatient": null,
            "test": 181445
        }
    },
    "2020/04/06": {
        "daily": {
            "case": 3148,
            "death": 75,
            "recovered": 284,
            "test": 21400
        },
        "total": {
            "case": 30217,
            "death": 649,
            "icuPatient": 1415,
            "intubatedPatient": 966,
            "pneumoniaPercent": null,
            "recovered": 1326,
            "seriouslyIllPatient": null,
            "test": 202845
        }
    },
    "2020/04/07": {
        "daily": {
            "case": 3892,
            "death": 76,
            "recovered": 256,
            "test": 20023
        },
        "total": {
            "case": 34109,
            "death": 725,
            "icuPatient": 1474,
            "intubatedPatient": 987,
            "pneumoniaPercent": null,
            "recovered": 1582,
            "seriouslyIllPatient": null,
            "test": 222868
        }
    },
    "2020/04/08": {
        "daily": {
            "case": 4117,
            "death": 87,
            "recovered": 264,
            "test": 24900
        },
        "total": {
            "case": 38226,
            "death": 812,
            "icuPatient": 1492,
            "intubatedPatient": 995,
            "pneumoniaPercent": null,
            "recovered": 1846,
            "seriouslyIllPatient": null,
            "test": 247768
        }
    },
    "2020/04/09": {
        "daily": {
            "case": 4056,
            "death": 96,
            "recovered": 296,
            "test": 28578
        },
        "total": {
            "case": 42282,
            "death": 908,
            "icuPatient": 1552,
            "intubatedPatient": 1017,
            "pneumoniaPercent": null,
            "recovered": 2142,
            "seriouslyIllPatient": null,
            "test": 276338
        }
    },
    "2020/04/10": {
        "daily": {
            "case": 4747,
            "death": 98,
            "recovered": 281,
            "test": 30864
        },
        "total": {
            "case": 47029,
            "death": 1006,
            "icuPatient": 1667,
            "intubatedPatient": 1062,
            "pneumoniaPercent": null,
            "recovered": 2423,
            "seriouslyIllPatient": null,
            "test": 307210
        }
    },
    "2020/04/11": {
        "daily": {
            "case": 5138,
            "death": 95,
            "recovered": 542,
            "test": 33170
        },
        "total": {
            "case": 52167,
            "death": 1101,
            "icuPatient": 1626,
            "intubatedPatient": 1021,
            "pneumoniaPercent": null,
            "recovered": 2965,
            "seriouslyIllPatient": null,
            "test": 340380
        }
    },
    "2020/04/12": {
        "daily": {
            "case": 4789,
            "death": 97,
            "recovered": 481,
            "test": 35720
        },
        "total": {
            "case": 56956,
            "death": 1198,
            "icuPatient": 1665,
            "intubatedPatient": 978,
            "pneumoniaPercent": null,
            "recovered": 3446,
            "seriouslyIllPatient": null,
            "test": 376100
        }
    },
    "2020/04/13": {
        "daily": {
            "case": 4093,
            "death": 98,
            "recovered": 511,
            "test": 34456
        },
        "total": {
            "case": 61049,
            "death": 1296,
            "icuPatient": 1786,
            "intubatedPatient": 1063,
            "pneumoniaPercent": null,
            "recovered": 3957,
            "seriouslyIllPatient": null,
            "test": 410556
        }
    },
    "2020/04/14": {
        "daily": {
            "case": 4062,
            "death": 107,
            "recovered": 842,
            "test": 33070
        },
        "total": {
            "case": 65111,
            "death": 1403,
            "icuPatient": 1809,
            "intubatedPatient": 1087,
            "pneumoniaPercent": null,
            "recovered": 4799,
            "seriouslyIllPatient": null,
            "test": 443626
        }
    },
    "2020/04/15": {
        "daily": {
            "case": 4291,
            "death": 115,
            "recovered": 875,
            "test": 34090
        },
        "total": {
            "case": 69392,
            "death": 1518,
            "icuPatient": 1820,
            "intubatedPatient": 1052,
            "pneumoniaPercent": null,
            "recovered": 5674,
            "seriouslyIllPatient": null,
            "test": 477716
        }
    },
    "2020/04/16": {
        "daily": {
            "case": 4801,
            "death": 125,
            "recovered": 1415,
            "test": 40427
        },
        "total": {
            "case": 74193,
            "death": 1643,
            "icuPatient": 1854,
            "intubatedPatient": 1040,
            "pneumoniaPercent": null,
            "recovered": 7089,
            "seriouslyIllPatient": null,
            "test": 518143
        }
    },
    "2020/04/17": {
        "daily": {
            "case": 4353,
            "death": 126,
            "recovered": 1542,
            "test": 40270
        },
        "total": {
            "case": 78546,
            "death": 1769,
            "icuPatient": 1845,
            "intubatedPatient": 1014,
            "pneumoniaPercent": null,
            "recovered": 8631,
            "seriouslyIllPatient": null,
            "test": 558413
        }
    },
    "2020/04/18": {
        "daily": {
            "case": 3783,
            "death": 121,
            "recovered": 1822,
            "test": 40520
        },
        "total": {
            "case": 82329,
            "death": 1890,
            "icuPatient": 1894,
            "intubatedPatient": 1054,
            "pneumoniaPercent": null,
            "recovered": 10453,
            "seriouslyIllPatient": null,
            "test": 598933
        }
    },
    "2020/04/19": {
        "daily": {
            "case": 3977,
            "death": 127,
            "recovered": 1523,
            "test": 35344
        },
        "total": {
            "case": 86306,
            "death": 2017,
            "icuPatient": 1922,
            "intubatedPatient": 1031,
            "pneumoniaPercent": null,
            "recovered": 11976,
            "seriouslyIllPatient": null,
            "test": 634277
        }
    },
    "2020/04/20": {
        "daily": {
            "case": 4674,
            "death": 123,
            "recovered": 1454,
            "test": 39703
        },
        "total": {
            "case": 90980,
            "death": 2140,
            "icuPatient": 1909,
            "intubatedPatient": 1033,
            "pneumoniaPercent": null,
            "recovered": 13430,
            "seriouslyIllPatient": null,
            "test": 673980
        }
    },
    "2020/04/21": {
        "daily": {
            "case": 4611,
            "death": 119,
            "recovered": 1488,
            "test": 39429
        },
        "total": {
            "case": 95591,
            "death": 2259,
            "icuPatient": 1865,
            "intubatedPatient": 1006,
            "pneumoniaPercent": null,
            "recovered": 14918,
            "seriouslyIllPatient": null,
            "test": 713409
        }
    },
    "2020/04/22": {
        "daily": {
            "case": 3083,
            "death": 117,
            "recovered": 1559,
            "test": 37535
        },
        "total": {
            "case": 98674,
            "death": 2376,
            "icuPatient": 1814,
            "intubatedPatient": 985,
            "pneumoniaPercent": null,
            "recovered": 16477,
            "seriouslyIllPatient": null,
            "test": 750944
        }
    },
    "2020/04/23": {
        "daily": {
            "case": 3116,
            "death": 115,
            "recovered": 2014,
            "test": 40962
        },
        "total": {
            "case": 101790,
            "death": 2491,
            "icuPatient": 1816,
            "intubatedPatient": 982,
            "pneumoniaPercent": null,
            "recovered": 18491,
            "seriouslyIllPatient": null,
            "test": 791906
        }
    },
    "2020/04/24": {
        "daily": {
            "case": 3122,
            "death": 109,
            "recovered": 3246,
            "test": 38351
        },
        "total": {
            "case": 104912,
            "death": 2600,
            "icuPatient": 1790,
            "intubatedPatient": 929,
            "pneumoniaPercent": null,
            "recovered": 21737,
            "seriouslyIllPatient": null,
            "test": 830257
        }
    },
    "2020/04/25": {
        "daily": {
            "case": 2861,
            "death": 106,
            "recovered": 3845,
            "test": 38308
        },
        "total": {
            "case": 107773,
            "death": 2706,
            "icuPatient": 1782,
            "intubatedPatient": 900,
            "pneumoniaPercent": null,
            "recovered": 25582,
            "seriouslyIllPatient": null,
            "test": 868565
        }
    },
    "2020/04/26": {
        "daily": {
            "case": 2357,
            "death": 99,
            "recovered": 3558,
            "test": 30177
        },
        "total": {
            "case": 110130,
            "death": 2805,
            "icuPatient": 1776,
            "intubatedPatient": 883,
            "pneumoniaPercent": null,
            "recovered": 29140,
            "seriouslyIllPatient": null,
            "test": 898742
        }
    },
    "2020/04/27": {
        "daily": {
            "case": 2131,
            "death": 95,
            "recovered": 4651,
            "test": 20143
        },
        "total": {
            "case": 112261,
            "death": 2900,
            "icuPatient": 1736,
            "intubatedPatient": 882,
            "pneumoniaPercent": null,
            "recovered": 33791,
            "seriouslyIllPatient": null,
            "test": 918885
        }
    },
    "2020/04/28": {
        "daily": {
            "case": 2392,
            "death": 92,
            "recovered": 5018,
            "test": 29230
        },
        "total": {
            "case": 114653,
            "death": 2992,
            "icuPatient": 1621,
            "intubatedPatient": 845,
            "pneumoniaPercent": null,
            "recovered": 38809,
            "seriouslyIllPatient": null,
            "test": 948115
        }
    },
    "2020/04/29": {
        "daily": {
            "case": 2936,
            "death": 89,
            "recovered": 5231,
            "test": 43498
        },
        "total": {
            "case": 117589,
            "death": 3081,
            "icuPatient": 1574,
            "intubatedPatient": 831,
            "pneumoniaPercent": null,
            "recovered": 44022,
            "seriouslyIllPatient": null,
            "test": 991613
        }
    },
    "2020/04/30": {
        "daily": {
            "case": 2615,
            "death": 93,
            "recovered": 4846,
            "test": 42004
        },
        "total": {
            "case": 120204,
            "death": 3174,
            "icuPatient": 1514,
            "intubatedPatient": 803,
            "pneumoniaPercent": null,
            "recovered": 48886,
            "seriouslyIllPatient": null,
            "test": 1033617
        }
    },
    "2020/05/01": {
        "daily": {
            "case": 2188,
            "death": 84,
            "recovered": 4922,
            "test": 41431
        },
        "total": {
            "case": 122392,
            "death": 3258,
            "icuPatient": 1480,
            "intubatedPatient": 818,
            "pneumoniaPercent": null,
            "recovered": 53808,
            "seriouslyIllPatient": null,
            "test": 1075048
        }
    },
    "2020/05/02": {
        "daily": {
            "case": 1983,
            "death": 78,
            "recovered": 4451,
            "test": 36318
        },
        "total": {
            "case": 124375,
            "death": 3336,
            "icuPatient": 1445,
            "intubatedPatient": 778,
            "pneumoniaPercent": null,
            "recovered": 58259,
            "seriouslyIllPatient": null,
            "test": 1111366
        }
    },
    "2020/05/03": {
        "daily": {
            "case": 1670,
            "death": 61,
            "recovered": 4892,
            "test": 24001
        },
        "total": {
            "case": 126045,
            "death": 3397,
            "icuPatient": 1424,
            "intubatedPatient": 766,
            "pneumoniaPercent": null,
            "recovered": 63151,
            "seriouslyIllPatient": null,
            "test": 1135367
        }
    },
    "2020/05/04": {
        "daily": {
            "case": 1614,
            "death": 64,
            "recovered": 5015,
            "test": 35771
        },
        "total": {
            "case": 127659,
            "death": 3461,
            "icuPatient": 1384,
            "intubatedPatient": 727,
            "pneumoniaPercent": null,
            "recovered": 68166,
            "seriouslyIllPatient": null,
            "test": 1171138
        }
    },
    "2020/05/05": {
        "daily": {
            "case": 1832,
            "death": 59,
            "recovered": 5119,
            "test": 33283
        },
        "total": {
            "case": 129491,
            "death": 3520,
            "icuPatient": 1338,
            "intubatedPatient": 707,
            "pneumoniaPercent": null,
            "recovered": 73285,
            "seriouslyIllPatient": null,
            "test": 1204421
        }
    },
    "2020/05/06": {
        "daily": {
            "case": 2253,
            "death": 64,
            "recovered": 4917,
            "test": 30303
        },
        "total": {
            "case": 131744,
            "death": 3584,
            "icuPatient": 1278,
            "intubatedPatient": 669,
            "pneumoniaPercent": null,
            "recovered": 78202,
            "seriouslyIllPatient": null,
            "test": 1234724
        }
    },
    "2020/05/07": {
        "daily": {
            "case": 1977,
            "death": 57,
            "recovered": 4782,
            "test": 30395
        },
        "total": {
            "case": 133721,
            "death": 3641,
            "icuPatient": 1260,
            "intubatedPatient": 665,
            "pneumoniaPercent": null,
            "recovered": 82984,
            "seriouslyIllPatient": null,
            "test": 1265119
        }
    },
    "2020/05/08": {
        "daily": {
            "case": 1848,
            "death": 48,
            "recovered": 3412,
            "test": 33687
        },
        "total": {
            "case": 135569,
            "death": 3689,
            "icuPatient": 1219,
            "intubatedPatient": 653,
            "pneumoniaPercent": null,
            "recovered": 86396,
            "seriouslyIllPatient": null,
            "test": 1298806
        }
    },
    "2020/05/09": {
        "daily": {
            "case": 1546,
            "death": 50,
            "recovered": 3084,
            "test": 35605
        },
        "total": {
            "case": 137115,
            "death": 3739,
            "icuPatient": 1168,
            "intubatedPatient": 628,
            "pneumoniaPercent": null,
            "recovered": 89480,
            "seriouslyIllPatient": null,
            "test": 1334411
        }
    },
    "2020/05/10": {
        "daily": {
            "case": 1542,
            "death": 47,
            "recovered": 3211,
            "test": 36187
        },
        "total": {
            "case": 138657,
            "death": 3786,
            "icuPatient": 1154,
            "intubatedPatient": 598,
            "pneumoniaPercent": null,
            "recovered": 92691,
            "seriouslyIllPatient": null,
            "test": 1370598
        }
    },
    "2020/05/11": {
        "daily": {
            "case": 1114,
            "death": 55,
            "recovered": 3089,
            "test": 32722
        },
        "total": {
            "case": 139771,
            "death": 3841,
            "icuPatient": 1126,
            "intubatedPatient": 578,
            "pneumoniaPercent": null,
            "recovered": 95780,
            "seriouslyIllPatient": null,
            "test": 1403320
        }
    },
    "2020/05/12": {
        "daily": {
            "case": 1704,
            "death": 53,
            "recovered": 3109,
            "test": 37351
        },
        "total": {
            "case": 141475,
            "death": 3894,
            "icuPatient": 1045,
            "intubatedPatient": 576,
            "pneumoniaPercent": null,
            "recovered": 98889,
            "seriouslyIllPatient": null,
            "test": 1440671
        }
    },
    "2020/05/13": {
        "daily": {
            "case": 1639,
            "death": 58,
            "recovered": 2826,
            "test": 33332
        },
        "total": {
            "case": 143114,
            "death": 3952,
            "icuPatient": 998,
            "intubatedPatient": 535,
            "pneumoniaPercent": null,
            "recovered": 101715,
            "seriouslyIllPatient": null,
            "test": 1474003
        }
    },
    "2020/05/14": {
        "daily": {
            "case": 1635,
            "death": 55,
            "recovered": 2315,
            "test": 34821
        },
        "total": {
            "case": 144749,
            "death": 4007,
            "icuPatient": 963,
            "intubatedPatient": 508,
            "pneumoniaPercent": null,
            "recovered": 104030,
            "seriouslyIllPatient": null,
            "test": 1508824
        }
    },
    "2020/05/15": {
        "daily": {
            "case": 1708,
            "death": 48,
            "recovered": 2103,
            "test": 38565
        },
        "total": {
            "case": 146457,
            "death": 4055,
            "icuPatient": 944,
            "intubatedPatient": 490,
            "pneumoniaPercent": null,
            "recovered": 106133,
            "seriouslyIllPatient": null,
            "test": 1547389
        }
    },
    "2020/05/16": {
        "daily": {
            "case": 1610,
            "death": 41,
            "recovered": 2004,
            "test": 42236
        },
        "total": {
            "case": 148067,
            "death": 4096,
            "icuPatient": 906,
            "intubatedPatient": 474,
            "pneumoniaPercent": null,
            "recovered": 108137,
            "seriouslyIllPatient": null,
            "test": 1589625
        }
    },
    "2020/05/17": {
        "daily": {
            "case": 1368,
            "death": 44,
            "recovered": 1825,
            "test": 35369
        },
        "total": {
            "case": 149435,
            "death": 4140,
            "icuPatient": 914,
            "intubatedPatient": 468,
            "pneumoniaPercent": null,
            "recovered": 109962,
            "seriouslyIllPatient": null,
            "test": 1624994
        }
    },
    "2020/05/18": {
        "daily": {
            "case": 1158,
            "death": 31,
            "recovered": 1615,
            "test": 25141
        },
        "total": {
            "case": 150593,
            "death": 4171,
            "icuPatient": 903,
            "intubatedPatient": 463,
            "pneumoniaPercent": null,
            "recovered": 111577,
            "seriouslyIllPatient": null,
            "test": 1650135
        }
    },
    "2020/05/19": {
        "daily": {
            "case": 1022,
            "death": 28,
            "recovered": 1318,
            "test": 25382
        },
        "total": {
            "case": 151615,
            "death": 4199,
            "icuPatient": 882,
            "intubatedPatient": 455,
            "pneumoniaPercent": null,
            "recovered": 112895,
            "seriouslyIllPatient": null,
            "test": 1675517
        }
    },
    "2020/05/20": {
        "daily": {
            "case": 972,
            "death": 23,
            "recovered": 1092,
            "test": 20838
        },
        "total": {
            "case": 152587,
            "death": 4222,
            "icuPatient": 877,
            "intubatedPatient": 445,
            "pneumoniaPercent": null,
            "recovered": 113987,
            "seriouslyIllPatient": null,
            "test": 1696355
        }
    },
    "2020/05/21": {
        "daily": {
            "case": 961,
            "death": 27,
            "recovered": 1003,
            "test": 33633
        },
        "total": {
            "case": 153548,
            "death": 4249,
            "icuPatient": 820,
            "intubatedPatient": 424,
            "pneumoniaPercent": null,
            "recovered": 114990,
            "seriouslyIllPatient": null,
            "test": 1729988
        }
    },
    "2020/05/22": {
        "daily": {
            "case": 952,
            "death": 27,
            "recovered": 1121,
            "test": 37507
        },
        "total": {
            "case": 154500,
            "death": 4276,
            "icuPatient": 800,
            "intubatedPatient": 401,
            "pneumoniaPercent": null,
            "recovered": 116111,
            "seriouslyIllPatient": null,
            "test": 1767495
        }
    },
    "2020/05/23": {
        "daily": {
            "case": 1186,
            "death": 32,
            "recovered": 1491,
            "test": 40178
        },
        "total": {
            "case": 155686,
            "death": 4308,
            "icuPatient": 775,
            "intubatedPatient": 388,
            "pneumoniaPercent": null,
            "recovered": 117602,
            "seriouslyIllPatient": null,
            "test": 1807673
        }
    },
    "2020/05/24": {
        "daily": {
            "case": 1141,
            "death": 32,
            "recovered": 1092,
            "test": 24589
        },
        "total": {
            "case": 156827,
            "death": 4340,
            "icuPatient": 769,
            "intubatedPatient": 385,
            "pneumoniaPercent": null,
            "recovered": 118694,
            "seriouslyIllPatient": null,
            "test": 1832262
        }
    },
    "2020/05/25": {
        "daily": {
            "case": 987,
            "death": 29,
            "recovered": 1321,
            "test": 21492
        },
        "total": {
            "case": 157814,
            "death": 4369,
            "icuPatient": 756,
            "intubatedPatient": 371,
            "pneumoniaPercent": null,
            "recovered": 120015,
            "seriouslyIllPatient": null,
            "test": 1853754
        }
    },
    "2020/05/26": {
        "daily": {
            "case": 948,
            "death": 28,
            "recovered": 1492,
            "test": 19853
        },
        "total": {
            "case": 158762,
            "death": 4397,
            "icuPatient": 739,
            "intubatedPatient": 338,
            "pneumoniaPercent": null,
            "recovered": 121507,
            "seriouslyIllPatient": null,
            "test": 1873607
        }
    },
    "2020/05/27": {
        "daily": {
            "case": 1035,
            "death": 34,
            "recovered": 1286,
            "test": 21043
        },
        "total": {
            "case": 159797,
            "death": 4431,
            "icuPatient": 723,
            "intubatedPatient": 331,
            "pneumoniaPercent": null,
            "recovered": 122793,
            "seriouslyIllPatient": null,
            "test": 1894650
        }
    },
    "2020/05/28": {
        "daily": {
            "case": 1182,
            "death": 30,
            "recovered": 1576,
            "test": 33559
        },
        "total": {
            "case": 160979,
            "death": 4461,
            "icuPatient": 683,
            "intubatedPatient": 339,
            "pneumoniaPercent": null,
            "recovered": 124369,
            "seriouslyIllPatient": null,
            "test": 1928209
        }
    },
    "2020/05/29": {
        "daily": {
            "case": 1141,
            "death": 28,
            "recovered": 1594,
            "test": 36155
        },
        "total": {
            "case": 162120,
            "death": 4489,
            "icuPatient": 662,
            "intubatedPatient": 324,
            "pneumoniaPercent": null,
            "recovered": 125963,
            "seriouslyIllPatient": null,
            "test": 1964364
        }
    },
    "2020/05/30": {
        "daily": {
            "case": 983,
            "death": 26,
            "recovered": 1021,
            "test": 39230
        },
        "total": {
            "case": 163103,
            "death": 4515,
            "icuPatient": 649,
            "intubatedPatient": 308,
            "pneumoniaPercent": null,
            "recovered": 126984,
            "seriouslyIllPatient": null,
            "test": 2003594
        }
    },
    "2020/05/31": {
        "daily": {
            "case": 839,
            "death": 25,
            "recovered": 989,
            "test": 35600
        },
        "total": {
            "case": 163942,
            "death": 4540,
            "icuPatient": 648,
            "intubatedPatient": 287,
            "pneumoniaPercent": null,
            "recovered": 127973,
            "seriouslyIllPatient": null,
            "test": 2039194
        }
    },
    "2020/06/01": {
        "daily": {
            "case": 827,
            "death": 23,
            "recovered": 974,
            "test": 31525
        },
        "total": {
            "case": 164769,
            "death": 4563,
            "icuPatient": 651,
            "intubatedPatient": 283,
            "pneumoniaPercent": null,
            "recovered": 128947,
            "seriouslyIllPatient": null,
            "test": 2070719
        }
    },
    "2020/06/02": {
        "daily": {
            "case": 786,
            "death": 22,
            "recovered": 974,
            "test": 32325
        },
        "total": {
            "case": 165555,
            "death": 4585,
            "icuPatient": 633,
            "intubatedPatient": 271,
            "pneumoniaPercent": null,
            "recovered": 129921,
            "seriouslyIllPatient": null,
            "test": 2103044
        }
    },
    "2020/06/03": {
        "daily": {
            "case": 867,
            "death": 24,
            "recovered": 931,
            "test": 52305
        },
        "total": {
            "case": 166422,
            "death": 4609,
            "icuPatient": 612,
            "intubatedPatient": 261,
            "pneumoniaPercent": null,
            "recovered": 130852,
            "seriouslyIllPatient": null,
            "test": 2155349
        }
    },
    "2020/06/04": {
        "daily": {
            "case": 988,
            "death": 21,
            "recovered": 926,
            "test": 54234
        },
        "total": {
            "case": 167410,
            "death": 4630,
            "icuPatient": 602,
            "intubatedPatient": 265,
            "pneumoniaPercent": null,
            "recovered": 131778,
            "seriouslyIllPatient": null,
            "test": 2209583
        }
    },
    "2020/06/05": {
        "daily": {
            "case": 930,
            "death": 18,
            "recovered": 1622,
            "test": 57829
        },
        "total": {
            "case": 168340,
            "death": 4648,
            "icuPatient": 592,
            "intubatedPatient": 269,
            "pneumoniaPercent": null,
            "recovered": 133400,
            "seriouslyIllPatient": null,
            "test": 2267412
        }
    },
    "2020/06/06": {
        "daily": {
            "case": 878,
            "death": 21,
            "recovered": 1922,
            "test": 35846
        },
        "total": {
            "case": 169218,
            "death": 4669,
            "icuPatient": 591,
            "intubatedPatient": 264,
            "pneumoniaPercent": null,
            "recovered": 135322,
            "seriouslyIllPatient": null,
            "test": 2303258
        }
    },
    "2020/06/07": {
        "daily": {
            "case": 914,
            "death": 23,
            "recovered": 2647,
            "test": 35335
        },
        "total": {
            "case": 170132,
            "death": 4692,
            "icuPatient": 613,
            "intubatedPatient": 274,
            "pneumoniaPercent": null,
            "recovered": 137969,
            "seriouslyIllPatient": null,
            "test": 2338593
        }
    },
    "2020/06/08": {
        "daily": {
            "case": 989,
            "death": 19,
            "recovered": 3411,
            "test": 39361
        },
        "total": {
            "case": 171121,
            "death": 4711,
            "icuPatient": 625,
            "intubatedPatient": 261,
            "pneumoniaPercent": null,
            "recovered": 141380,
            "seriouslyIllPatient": null,
            "test": 2377954
        }
    },
    "2020/06/09": {
        "daily": {
            "case": 993,
            "death": 18,
            "recovered": 3218,
            "test": 37225
        },
        "total": {
            "case": 172114,
            "death": 4729,
            "icuPatient": 642,
            "intubatedPatient": 281,
            "pneumoniaPercent": null,
            "recovered": 144598,
            "seriouslyIllPatient": null,
            "test": 2415179
        }
    },
    "2020/06/10": {
        "daily": {
            "case": 922,
            "death": 17,
            "recovered": 2241,
            "test": 36521
        },
        "total": {
            "case": 173036,
            "death": 4746,
            "icuPatient": 631,
            "intubatedPatient": 280,
            "pneumoniaPercent": null,
            "recovered": 146839,
            "seriouslyIllPatient": null,
            "test": 2451700
        }
    },
    "2020/06/11": {
        "daily": {
            "case": 987,
            "death": 17,
            "recovered": 1021,
            "test": 49190
        },
        "total": {
            "case": 174023,
            "death": 4763,
            "icuPatient": 643,
            "intubatedPatient": 266,
            "pneumoniaPercent": null,
            "recovered": 147860,
            "seriouslyIllPatient": null,
            "test": 2500890
        }
    },
    "2020/06/12": {
        "daily": {
            "case": 1195,
            "death": 15,
            "recovered": 1242,
            "test": 41013
        },
        "total": {
            "case": 175218,
            "death": 4778,
            "icuPatient": 664,
            "intubatedPatient": 282,
            "pneumoniaPercent": null,
            "recovered": 149102,
            "seriouslyIllPatient": null,
            "test": 2541903
        }
    },
    "2020/06/13": {
        "daily": {
            "case": 1459,
            "death": 14,
            "recovered": 985,
            "test": 45092
        },
        "total": {
            "case": 176677,
            "death": 4792,
            "icuPatient": 684,
            "intubatedPatient": 284,
            "pneumoniaPercent": null,
            "recovered": 150087,
            "seriouslyIllPatient": null,
            "test": 2586995
        }
    },
    "2020/06/14": {
        "daily": {
            "case": 1562,
            "death": 15,
            "recovered": 1330,
            "test": 45176
        },
        "total": {
            "case": 178239,
            "death": 4807,
            "icuPatient": 717,
            "intubatedPatient": 290,
            "pneumoniaPercent": null,
            "recovered": 151417,
            "seriouslyIllPatient": null,
            "test": 2632171
        }
    },
    "2020/06/15": {
        "daily": {
            "case": 1592,
            "death": 18,
            "recovered": 947,
            "test": 42032
        },
        "total": {
            "case": 179831,
            "death": 4825,
            "icuPatient": 722,
            "intubatedPatient": 291,
            "pneumoniaPercent": null,
            "recovered": 152364,
            "seriouslyIllPatient": null,
            "test": 2674203
        }
    },
    "2020/06/16": {
        "daily": {
            "case": 1467,
            "death": 17,
            "recovered": 1015,
            "test": 46800
        },
        "total": {
            "case": 181298,
            "death": 4842,
            "icuPatient": 732,
            "intubatedPatient": 303,
            "pneumoniaPercent": null,
            "recovered": 153379,
            "seriouslyIllPatient": null,
            "test": 2721003
        }
    },
    "2020/06/17": {
        "daily": {
            "case": 1429,
            "death": 19,
            "recovered": 1261,
            "test": 52901
        },
        "total": {
            "case": 182727,
            "death": 4861,
            "icuPatient": 745,
            "intubatedPatient": 306,
            "pneumoniaPercent": null,
            "recovered": 154640,
            "seriouslyIllPatient": null,
            "test": 2773904
        }
    },
    "2020/06/18": {
        "daily": {
            "case": 1304,
            "death": 21,
            "recovered": 1382,
            "test": 48412
        },
        "total": {
            "case": 184031,
            "death": 4882,
            "icuPatient": 755,
            "intubatedPatient": 311,
            "pneumoniaPercent": null,
            "recovered": 156022,
            "seriouslyIllPatient": null,
            "test": 2822316
        }
    },
    "2020/06/19": {
        "daily": {
            "case": 1214,
            "death": 23,
            "recovered": 1494,
            "test": 41316
        },
        "total": {
            "case": 185245,
            "death": 4905,
            "icuPatient": 769,
            "intubatedPatient": 310,
            "pneumoniaPercent": null,
            "recovered": 157516,
            "seriouslyIllPatient": null,
            "test": 2863632
        }
    },
    "2020/06/20": {
        "daily": {
            "case": 1248,
            "death": 22,
            "recovered": 1312,
            "test": 41112
        },
        "total": {
            "case": 186493,
            "death": 4927,
            "icuPatient": 781,
            "intubatedPatient": 318,
            "pneumoniaPercent": null,
            "recovered": 158828,
            "seriouslyIllPatient": null,
            "test": 2904744
        }
    },
    "2020/06/21": {
        "daily": {
            "case": 1192,
            "death": 23,
            "recovered": 1412,
            "test": 40496
        },
        "total": {
            "case": 187685,
            "death": 4950,
            "icuPatient": 803,
            "intubatedPatient": 327,
            "pneumoniaPercent": null,
            "recovered": 169240,
            "seriouslyIllPatient": null,
            "test": 2945240
        }
    },
    "2020/06/22": {
        "daily": {
            "case": 1212,
            "death": 24,
            "recovered": 1293,
            "test": 41413
        },
        "total": {
            "case": 188897,
            "death": 4974,
            "icuPatient": 846,
            "intubatedPatient": 345,
            "pneumoniaPercent": null,
            "recovered": 161533,
            "seriouslyIllPatient": null,
            "test": 2986653
        }
    },
    "2020/06/23": {
        "daily": {
            "case": 1268,
            "death": 27,
            "recovered": 1315,
            "test": 42982
        },
        "total": {
            "case": 190165,
            "death": 5001,
            "icuPatient": 893,
            "intubatedPatient": 362,
            "pneumoniaPercent": null,
            "recovered": 162848,
            "seriouslyIllPatient": null,
            "test": 3029635
        }
    },
    "2020/06/24": {
        "daily": {
            "case": 1492,
            "death": 24,
            "recovered": 1386,
            "test": 53486
        },
        "total": {
            "case": 191657,
            "death": 5025,
            "icuPatient": 914,
            "intubatedPatient": 356,
            "pneumoniaPercent": null,
            "recovered": 164234,
            "seriouslyIllPatient": null,
            "test": 3083121
        }
    },
    "2020/06/25": {
        "daily": {
            "case": 1458,
            "death": 21,
            "recovered": 1472,
            "test": 52303
        },
        "total": {
            "case": 193115,
            "death": 5046,
            "icuPatient": 941,
            "intubatedPatient": 369,
            "pneumoniaPercent": null,
            "recovered": 165706,
            "seriouslyIllPatient": null,
            "test": 3135424
        }
    },
    "2020/06/26": {
        "daily": {
            "case": 1396,
            "death": 19,
            "recovered": 1492,
            "test": 51198
        },
        "total": {
            "case": 194511,
            "death": 5065,
            "icuPatient": 963,
            "intubatedPatient": 382,
            "pneumoniaPercent": null,
            "recovered": 167198,
            "seriouslyIllPatient": null,
            "test": 3186622
        }
    },
    "2020/06/27": {
        "daily": {
            "case": 1372,
            "death": 17,
            "recovered": 1984,
            "test": 45213
        },
        "total": {
            "case": 195883,
            "death": 5082,
            "icuPatient": 984,
            "intubatedPatient": 366,
            "pneumoniaPercent": null,
            "recovered": 169182,
            "seriouslyIllPatient": null,
            "test": 3231835
        }
    },
    "2020/06/28": {
        "daily": {
            "case": 1356,
            "death": 15,
            "recovered": 1413,
            "test": 48309
        },
        "total": {
            "case": 197239,
            "death": 5097,
            "icuPatient": 996,
            "intubatedPatient": 381,
            "pneumoniaPercent": null,
            "recovered": 170595,
            "seriouslyIllPatient": null,
            "test": 3280144
        }
    },
    "2020/06/29": {
        "daily": {
            "case": 1374,
            "death": 18,
            "recovered": 1214,
            "test": 51014
        },
        "total": {
            "case": 198613,
            "death": 5115,
            "icuPatient": 1018,
            "intubatedPatient": 375,
            "pneumoniaPercent": null,
            "recovered": 171809,
            "seriouslyIllPatient": null,
            "test": 3331158
        }
    },
    "2020/06/30": {
        "daily": {
            "case": 1293,
            "death": 16,
            "recovered": 1302,
            "test": 50492
        },
        "total": {
            "case": 199906,
            "death": 5131,
            "icuPatient": 1026,
            "intubatedPatient": 368,
            "pneumoniaPercent": null,
            "recovered": 173111,
            "seriouslyIllPatient": null,
            "test": 3381650
        }
    },
    "2020/07/01": {
        "daily": {
            "case": 1192,
            "death": 19,
            "recovered": 2311,
            "test": 52313
        },
        "total": {
            "case": 201098,
            "death": 5150,
            "icuPatient": 1035,
            "intubatedPatient": 362,
            "pneumoniaPercent": null,
            "recovered": 175422,
            "seriouslyIllPatient": null,
            "test": 3433963
        }
    },
    "2020/07/02": {
        "daily": {
            "case": 1186,
            "death": 17,
            "recovered": 1543,
            "test": 49714
        },
        "total": {
            "case": 202284,
            "death": 5167,
            "icuPatient": 1067,
            "intubatedPatient": 372,
            "pneumoniaPercent": null,
            "recovered": 176965,
            "seriouslyIllPatient": null,
            "test": 3483677
        }
    },
    "2020/07/03": {
        "daily": {
            "case": 1172,
            "death": 19,
            "recovered": 1313,
            "test": 52141
        },
        "total": {
            "case": 203456,
            "death": 5186,
            "icuPatient": 1082,
            "intubatedPatient": 374,
            "pneumoniaPercent": null,
            "recovered": 178278,
            "seriouslyIllPatient": null,
            "test": 3535818
        }
    },
    "2020/07/05": {
        "daily": {
            "case": 1148,
            "death": 19,
            "recovered": 1188,
            "test": 46414
        },
        "total": {
            "case": 205758,
            "death": 5225,
            "icuPatient": 1127,
            "intubatedPatient": 392,
            "pneumoniaPercent": null,
            "recovered": 180680,
            "seriouslyIllPatient": null,
            "test": 3630480
        }
    },
    "2020/07/06": {
        "daily": {
            "case": 1086,
            "death": 16,
            "recovered": 2315,
            "test": 52193
        },
        "total": {
            "case": 206844,
            "death": 5241,
            "icuPatient": 1130,
            "intubatedPatient": 395,
            "pneumoniaPercent": null,
            "recovered": 182995,
            "seriouslyIllPatient": null,
            "test": 3682673
        }
    },
    "2020/07/07": {
        "daily": {
            "case": 1053,
            "death": 19,
            "recovered": 2297,
            "test": 50545
        },
        "total": {
            "case": 207897,
            "death": 5260,
            "icuPatient": 1152,
            "intubatedPatient": 400,
            "pneumoniaPercent": null,
            "recovered": 185292,
            "seriouslyIllPatient": null,
            "test": 3733218
        }
    },
    "2020/07/08": {
        "daily": {
            "case": 1041,
            "death": 22,
            "recovered": 2219,
            "test": 49302
        },
        "total": {
            "case": 208938,
            "death": 5282,
            "icuPatient": 1172,
            "intubatedPatient": 406,
            "pneumoniaPercent": null,
            "recovered": 187511,
            "seriouslyIllPatient": null,
            "test": 3782520
        }
    },
    "2020/07/09": {
        "daily": {
            "case": 1024,
            "death": 18,
            "recovered": 2879,
            "test": 50103
        },
        "total": {
            "case": 209962,
            "death": 5300,
            "icuPatient": 1179,
            "intubatedPatient": 399,
            "pneumoniaPercent": null,
            "recovered": 190390,
            "seriouslyIllPatient": null,
            "test": 3832623
        }
    },
    "2020/07/10": {
        "daily": {
            "case": 1003,
            "death": 23,
            "recovered": 1493,
            "test": 48787
        },
        "total": {
            "case": 210965,
            "death": 5323,
            "icuPatient": 1182,
            "intubatedPatient": 402,
            "pneumoniaPercent": null,
            "recovered": 191883,
            "seriouslyIllPatient": null,
            "test": 3881410
        }
    },
    "2020/07/11": {
        "daily": {
            "case": 1016,
            "death": 21,
            "recovered": 1334,
            "test": 48813
        },
        "total": {
            "case": 211981,
            "death": 5344,
            "icuPatient": 1194,
            "intubatedPatient": 401,
            "pneumoniaPercent": null,
            "recovered": 193217,
            "seriouslyIllPatient": null,
            "test": 3930223
        }
    },
    "2020/07/12": {
        "daily": {
            "case": 1012,
            "death": 19,
            "recovered": 1298,
            "test": 45232
        },
        "total": {
            "case": 212993,
            "death": 5363,
            "icuPatient": 1209,
            "intubatedPatient": 409,
            "pneumoniaPercent": null,
            "recovered": 194515,
            "seriouslyIllPatient": null,
            "test": 3975455
        }
    },
    "2020/07/13": {
        "daily": {
            "case": 1008,
            "death": 19,
            "recovered": 1156,
            "test": 46492
        },
        "total": {
            "case": 214001,
            "death": 5382,
            "icuPatient": 1223,
            "intubatedPatient": 402,
            "pneumoniaPercent": null,
            "recovered": 195671,
            "seriouslyIllPatient": null,
            "test": 4021947
        }
    },
    "2020/07/14": {
        "daily": {
            "case": 992,
            "death": 20,
            "recovered": 1049,
            "test": 43231
        },
        "total": {
            "case": 214993,
            "death": 5402,
            "icuPatient": 1204,
            "intubatedPatient": 396,
            "pneumoniaPercent": null,
            "recovered": 196720,
            "seriouslyIllPatient": null,
            "test": 4065178
        }
    },
    "2020/07/15": {
        "daily": {
            "case": 947,
            "death": 17,
            "recovered": 1013,
            "test": 42320
        },
        "total": {
            "case": 215940,
            "death": 5419,
            "icuPatient": 1206,
            "intubatedPatient": 401,
            "pneumoniaPercent": null,
            "recovered": 197733,
            "seriouslyIllPatient": null,
            "test": 4107498
        }
    },
    "2020/07/16": {
        "daily": {
            "case": 933,
            "death": 21,
            "recovered": 1087,
            "test": 42411
        },
        "total": {
            "case": 216873,
            "death": 5440,
            "icuPatient": 1213,
            "intubatedPatient": 394,
            "pneumoniaPercent": null,
            "recovered": 198820,
            "seriouslyIllPatient": null,
            "test": 4149909
        }
    },
    "2020/07/17": {
        "daily": {
            "case": 926,
            "death": 18,
            "recovered": 1014,
            "test": 41215
        },
        "total": {
            "case": 217799,
            "death": 5458,
            "icuPatient": 1226,
            "intubatedPatient": 402,
            "pneumoniaPercent": null,
            "recovered": 199834,
            "seriouslyIllPatient": null,
            "test": 4191124
        }
    },
    "2020/07/18": {
        "daily": {
            "case": 918,
            "death": 17,
            "recovered": 1179,
            "test": 40943
        },
        "total": {
            "case": 218717,
            "death": 5475,
            "icuPatient": 1231,
            "intubatedPatient": 394,
            "pneumoniaPercent": null,
            "recovered": 201013,
            "seriouslyIllPatient": null,
            "test": 4232067
        }
    },
    "2020/07/19": {
        "daily": {
            "case": 924,
            "death": 16,
            "recovered": 997,
            "test": 41310
        },
        "total": {
            "case": 219641,
            "death": 5491,
            "icuPatient": 1246,
            "intubatedPatient": 398,
            "pneumoniaPercent": null,
            "recovered": 202010,
            "seriouslyIllPatient": null,
            "test": 4273377
        }
    },
    "2020/07/20": {
        "daily": {
            "case": 931,
            "death": 17,
            "recovered": 992,
            "test": 43404
        },
        "total": {
            "case": 220572,
            "death": 5508,
            "icuPatient": 1243,
            "intubatedPatient": 385,
            "pneumoniaPercent": null,
            "recovered": 203002,
            "seriouslyIllPatient": null,
            "test": 4316781
        }
    },
    "2020/07/21": {
        "daily": {
            "case": 928,
            "death": 18,
            "recovered": 1009,
            "test": 42846
        },
        "total": {
            "case": 221500,
            "death": 5526,
            "icuPatient": 1246,
            "intubatedPatient": 379,
            "pneumoniaPercent": null,
            "recovered": 204011,
            "seriouslyIllPatient": null,
            "test": 4359627
        }
    },
    "2020/07/22": {
        "daily": {
            "case": 902,
            "death": 19,
            "recovered": 1203,
            "test": 43404
        },
        "total": {
            "case": 222402,
            "death": 5545,
            "icuPatient": 1244,
            "intubatedPatient": 381,
            "pneumoniaPercent": null,
            "recovered": 205214,
            "seriouslyIllPatient": null,
            "test": 4403031
        }
    },
    "2020/07/23": {
        "daily": {
            "case": 913,
            "death": 18,
            "recovered": 1151,
            "test": 43343
        },
        "total": {
            "case": 223315,
            "death": 5563,
            "icuPatient": 1251,
            "intubatedPatient": 378,
            "pneumoniaPercent": null,
            "recovered": 206365,
            "seriouslyIllPatient": null,
            "test": 4446374
        }
    },
    "2020/07/24": {
        "daily": {
            "case": 937,
            "death": 17,
            "recovered": 1009,
            "test": 42986
        },
        "total": {
            "case": 224252,
            "death": 5580,
            "icuPatient": 1248,
            "intubatedPatient": 379,
            "pneumoniaPercent": null,
            "recovered": 207374,
            "seriouslyIllPatient": null,
            "test": 4489360
        }
    },
    "2020/07/25": {
        "daily": {
            "case": 921,
            "death": 16,
            "recovered": 1103,
            "test": 43312
        },
        "total": {
            "case": 225173,
            "death": 5596,
            "icuPatient": 1252,
            "intubatedPatient": 386,
            "pneumoniaPercent": null,
            "recovered": 208477,
            "seriouslyIllPatient": null,
            "test": 4532672
        }
    },
    "2020/07/26": {
        "daily": {
            "case": 927,
            "death": 17,
            "recovered": 1010,
            "test": 40016
        },
        "total": {
            "case": 226100,
            "death": 5613,
            "icuPatient": 1249,
            "intubatedPatient": 387,
            "pneumoniaPercent": null,
            "recovered": 209487,
            "seriouslyIllPatient": null,
            "test": 4572688
        }
    },
    "2020/07/27": {
        "daily": {
            "case": 919,
            "death": 17,
            "recovered": 982,
            "test": 45283
        },
        "total": {
            "case": 227019,
            "death": 5630,
            "icuPatient": 1263,
            "intubatedPatient": 392,
            "pneumoniaPercent": null,
            "recovered": 210469,
            "seriouslyIllPatient": null,
            "test": 4617971
        }
    },
    "2020/07/28": {
        "daily": {
            "case": 963,
            "death": 15,
            "recovered": 1092,
            "test": 47412
        },
        "total": {
            "case": 227982,
            "death": 5645,
            "icuPatient": 1280,
            "intubatedPatient": 403,
            "pneumoniaPercent": null,
            "recovered": 211561,
            "seriouslyIllPatient": null,
            "test": 4665383
        }
    },
    "2020/07/29": {
        "daily": {
            "case": 942,
            "death": 14,
            "recovered": 996,
            "test": 45712
        },
        "total": {
            "case": 228924,
            "death": 5659,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 9.4,
            "recovered": 212557,
            "seriouslyIllPatient": 542,
            "test": 4711095
        }
    },
    "2020/07/30": {
        "daily": {
            "case": 967,
            "death": 15,
            "recovered": 982,
            "test": 43967
        },
        "total": {
            "case": 229891,
            "death": 5674,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 9.3,
            "recovered": 213539,
            "seriouslyIllPatient": 561,
            "test": 4454331
        }
    },
    "2020/07/31": {
        "daily": {
            "case": 982,
            "death": 17,
            "recovered": 996,
            "test": 46492
        },
        "total": {
            "case": 230873,
            "death": 5691,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.8,
            "recovered": 214535,
            "seriouslyIllPatient": 582,
            "test": 4800823
        }
    },
    "2020/08/01": {
        "daily": {
            "case": 996,
            "death": 19,
            "recovered": 981,
            "test": 44846
        },
        "total": {
            "case": 231869,
            "death": 5710,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.7,
            "recovered": 215516,
            "seriouslyIllPatient": 586,
            "test": 4845669
        }
    },
    "2020/08/02": {
        "daily": {
            "case": 987,
            "death": 18,
            "recovered": 978,
            "test": 40247
        },
        "total": {
            "case": 232856,
            "death": 5728,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.5,
            "recovered": 216494,
            "seriouslyIllPatient": 582,
            "test": 4885916
        }
    },
    "2020/08/03": {
        "daily": {
            "case": 995,
            "death": 19,
            "recovered": 1003,
            "test": 41301
        },
        "total": {
            "case": 233851,
            "death": 5747,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.4,
            "recovered": 217497,
            "seriouslyIllPatient": 580,
            "test": 4927217
        }
    },
    "2020/08/04": {
        "daily": {
            "case": 1083,
            "death": 18,
            "recovered": 994,
            "test": 46249
        },
        "total": {
            "case": 234934,
            "death": 5765,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.5,
            "recovered": 218491,
            "seriouslyIllPatient": 583,
            "test": 4973466
        }
    },
    "2020/08/05": {
        "daily": {
            "case": 1178,
            "death": 19,
            "recovered": 1015,
            "test": 53842
        },
        "total": {
            "case": 236112,
            "death": 5784,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.4,
            "recovered": 219506,
            "seriouslyIllPatient": 582,
            "test": 5027308
        }
    },
    "2020/08/06": {
        "daily": {
            "case": 1153,
            "death": 14,
            "recovered": 1040,
            "test": 54494
        },
        "total": {
            "case": 237265,
            "death": 5798,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.3,
            "recovered": 220546,
            "seriouslyIllPatient": 580,
            "test": 5081802
        }
    },
    "2020/08/07": {
        "daily": {
            "case": 1185,
            "death": 15,
            "recovered": 1028,
            "test": 56726
        },
        "total": {
            "case": 238450,
            "death": 5813,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.3,
            "recovered": 221574,
            "seriouslyIllPatient": 586,
            "test": 5138528
        }
    },
    "2020/08/08": {
        "daily": {
            "case": 1172,
            "death": 16,
            "recovered": 1082,
            "test": 63842
        },
        "total": {
            "case": 239622,
            "death": 5829,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.1,
            "recovered": 222656,
            "seriouslyIllPatient": 587,
            "test": 5202370
        }
    },
    "2020/08/09": {
        "daily": {
            "case": 1182,
            "death": 15,
            "recovered": 1103,
            "test": 61446
        },
        "total": {
            "case": 240804,
            "death": 5844,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.1,
            "recovered": 223759,
            "seriouslyIllPatient": 596,
            "test": 5263816
        }
    },
    "2020/08/10": {
        "daily": {
            "case": 1193,
            "death": 14,
            "recovered": 1211,
            "test": 62219
        },
        "total": {
            "case": 241997,
            "death": 5858,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.2,
            "recovered": 224970,
            "seriouslyIllPatient": 603,
            "test": 5326035
        }
    },
    "2020/08/11": {
        "daily": {
            "case": 1183,
            "death": 15,
            "recovered": 1185,
            "test": 61716
        },
        "total": {
            "case": 243180,
            "death": 5873,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.2,
            "recovered": 226155,
            "seriouslyIllPatient": 617,
            "test": 5387751
        }
    },
    "2020/08/12": {
        "daily": {
            "case": 1212,
            "death": 18,
            "recovered": 934,
            "test": 67237
        },
        "total": {
            "case": 244392,
            "death": 5891,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 8.2,
            "recovered": 227089,
            "seriouslyIllPatient": 632,
            "test": 5454988
        }
    },
    "2020/08/13": {
        "daily": {
            "case": 1243,
            "death": 21,
            "recovered": 968,
            "test": 66892
        },
        "total": {
            "case": 245635,
            "death": 5912,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.9,
            "recovered": 228057,
            "seriouslyIllPatient": 647,
            "test": 5521880
        }
    },
    "2020/08/14": {
        "daily": {
            "case": 1226,
            "death": 22,
            "recovered": 923,
            "test": 70192
        },
        "total": {
            "case": 246861,
            "death": 5934,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.8,
            "recovered": 228980,
            "seriouslyIllPatient": 656,
            "test": 5592072
        }
    },
    "2020/08/15": {
        "daily": {
            "case": 1256,
            "death": 21,
            "recovered": 992,
            "test": 67214
        },
        "total": {
            "case": 248117,
            "death": 5955,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.6,
            "recovered": 229972,
            "seriouslyIllPatient": 668,
            "test": 5659286
        }
    },
    "2020/08/16": {
        "daily": {
            "case": 1192,
            "death": 19,
            "recovered": 997,
            "test": 65956
        },
        "total": {
            "case": 249309,
            "death": 5974,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.6,
            "recovered": 230969,
            "seriouslyIllPatient": 679,
            "test": 5725242
        }
    },
    "2020/08/17": {
        "daily": {
            "case": 1223,
            "death": 22,
            "recovered": 1002,
            "test": 74846
        },
        "total": {
            "case": 250524,
            "death": 5996,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.5,
            "recovered": 231971,
            "seriouslyIllPatient": 686,
            "test": 5800088
        }
    },
    "2020/08/18": {
        "daily": {
            "case": 1263,
            "death": 20,
            "recovered": 942,
            "test": 82318
        },
        "total": {
            "case": 251805,
            "death": 6016,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.5,
            "recovered": 232913,
            "seriouslyIllPatient": 703,
            "test": 5882406
        }
    },
    "2020/08/19": {
        "daily": {
            "case": 1303,
            "death": 23,
            "recovered": 1002,
            "test": 87223
        },
        "total": {
            "case": 253108,
            "death": 6039,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.4,
            "recovered": 233915,
            "seriouslyIllPatient": 719,
            "test": 5969629
        }
    },
    "2020/08/20": {
        "daily": {
            "case": 1412,
            "death": 19,
            "recovered": 882,
            "test": 92301
        },
        "total": {
            "case": 254520,
            "death": 6058,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.3,
            "recovered": 234797,
            "seriouslyIllPatient": 735,
            "test": 6061930
        }
    },
    "2020/08/21": {
        "daily": {
            "case": 1203,
            "death": 22,
            "recovered": 772,
            "test": 92227
        },
        "total": {
            "case": 255723,
            "death": 6080,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.3,
            "recovered": 235569,
            "seriouslyIllPatient": 749,
            "test": 6154157
        }
    },
    "2020/08/22": {
        "daily": {
            "case": 1309,
            "death": 22,
            "recovered": 801,
            "test": 93007
        },
        "total": {
            "case": 257032,
            "death": 6102,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.4,
            "recovered": 236370,
            "seriouslyIllPatient": 762,
            "test": 6247164
        }
    },
    "2020/08/23": {
        "daily": {
            "case": 1217,
            "death": 19,
            "recovered": 795,
            "test": 80302
        },
        "total": {
            "case": 258249,
            "death": 6121,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.5,
            "recovered": 237165,
            "seriouslyIllPatient": 783,
            "test": 6327466
        }
    },
    "2020/08/24": {
        "daily": {
            "case": 1443,
            "death": 18,
            "recovered": 743,
            "test": 95943
        },
        "total": {
            "case": 259692,
            "death": 6139,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.4,
            "recovered": 237908,
            "seriouslyIllPatient": 796,
            "test": 6423409
        }
    },
    "2020/08/25": {
        "daily": {
            "case": 1502,
            "death": 24,
            "recovered": 887,
            "test": 98231
        },
        "total": {
            "case": 261194,
            "death": 6163,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.4,
            "recovered": 238795,
            "seriouslyIllPatient": 811,
            "test": 6521640
        }
    },
    "2020/08/26": {
        "daily": {
            "case": 1313,
            "death": 20,
            "recovered": 1002,
            "test": 100109
        },
        "total": {
            "case": 262507,
            "death": 6183,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.4,
            "recovered": 239797,
            "seriouslyIllPatient": 841,
            "test": 6621749
        }
    },
    "2020/08/27": {
        "daily": {
            "case": 1491,
            "death": 26,
            "recovered": 995,
            "test": 106111
        },
        "total": {
            "case": 263998,
            "death": 6209,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.3,
            "recovered": 240792,
            "seriouslyIllPatient": 862,
            "test": 6727860
        }
    },
    "2020/08/28": {
        "daily": {
            "case": 1517,
            "death": 36,
            "recovered": 1017,
            "test": 107814
        },
        "total": {
            "case": 265515,
            "death": 6245,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.4,
            "recovered": 241809,
            "seriouslyIllPatient": 896,
            "test": 6835674
        }
    },
    "2020/08/29": {
        "daily": {
            "case": 1549,
            "death": 39,
            "recovered": 1003,
            "test": 101414
        },
        "total": {
            "case": 267064,
            "death": 6284,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.4,
            "recovered": 242812,
            "seriouslyIllPatient": 917,
            "test": 6937088
        }
    },
    "2020/08/30": {
        "daily": {
            "case": 1482,
            "death": 42,
            "recovered": 1027,
            "test": 91302
        },
        "total": {
            "case": 268546,
            "death": 6326,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.5,
            "recovered": 243839,
            "seriouslyIllPatient": 945,
            "test": 7028390
        }
    },
    "2020/08/31": {
        "daily": {
            "case": 1587,
            "death": 44,
            "recovered": 1087,
            "test": 110102
        },
        "total": {
            "case": 270133,
            "death": 6370,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.5,
            "recovered": 244926,
            "seriouslyIllPatient": 961,
            "test": 7138492
        }
    },
    "2020/09/01": {
        "daily": {
            "case": 1572,
            "death": 47,
            "recovered": 1003,
            "test": 109443
        },
        "total": {
            "case": 271705,
            "death": 6417,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.6,
            "recovered": 245929,
            "seriouslyIllPatient": 991,
            "test": 7247935
        }
    },
    "2020/09/02": {
        "daily": {
            "case": 1596,
            "death": 45,
            "recovered": 947,
            "test": 107927
        },
        "total": {
            "case": 273301,
            "death": 6462,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.6,
            "recovered": 246876,
            "seriouslyIllPatient": 1017,
            "test": 7355862
        }
    },
    "2020/09/03": {
        "daily": {
            "case": 1642,
            "date": "2020/09/03",
            "death": 49,
            "recovered": 1211,
            "test": 110225
        },
        "total": {
            "case": 274943,
            "date": "2020/09/03",
            "death": 6511,
            "icuPatient": null,
            "intubatedPatient": null,
            "pneumoniaPercent": 7.6,
            "recovered": 248087,
            "seriouslyIllPatient": 1041,
            "test": 7466087
        }
    }
}
```

#### Error Response

**Code:** `404 NOT FOUND`



### All Timeseries Dataset

Use to get all timeseries data.

**URL:** `/timeseries/`

**URL:** `/timeseries/all/`

**Method:** `GET`

**Auth required:** No

#### Success Response

**Code:** `200 OK`

**Content example**

```json
{
    "daily": {
        "case": [
            1,
            0,
            4,
            1,
            12,
            29,
            51,
            93,
            168,
            311,
            277,
            289,
            293,
            343,
            561,
            1196,
            2069,
            1704,
            1815,
            1610,
            2704,
            2148,
            2456,
            2786,
            3013,
            3135,
            3148,
            3892,
            4117,
            4056,
            4747,
            5138,
            4789,
            4093,
            4062,
            4291,
            4801,
            4353,
            3783,
            3977,
            4674,
            4611,
            3083,
            3116,
            3122,
            2861,
            2357,
            2131,
            2392,
            2936,
            2615,
            2188,
            1983,
            1670,
            1614,
            1832,
            2253,
            1977,
            1848,
            1546,
            1542,
            1114,
            1704,
            1639,
            1635,
            1708,
            1610,
            1368,
            1158,
            1022,
            972,
            961,
            952,
            1186,
            1141,
            987,
            948,
            1035,
            1182,
            1141,
            983,
            839,
            827,
            786,
            867,
            988,
            930,
            878,
            914,
            989,
            993,
            922,
            987,
            1195,
            1459,
            1562,
            1592,
            1467,
            1429,
            1304,
            1214,
            1248,
            1192,
            1212,
            1268,
            1492,
            1458,
            1396,
            1372,
            1356,
            1374,
            1293,
            1192,
            1186,
            1172,
            1148,
            1086,
            1053,
            1041,
            1024,
            1003,
            1016,
            1012,
            1008,
            992,
            947,
            933,
            926,
            918,
            924,
            931,
            928,
            902,
            913,
            937,
            921,
            927,
            919,
            963,
            942,
            967,
            982,
            996,
            987,
            995,
            1083,
            1178,
            1153,
            1185,
            1172,
            1182,
            1193,
            1183,
            1212,
            1243,
            1226,
            1256,
            1192,
            1223,
            1263,
            1303,
            1412,
            1203,
            1309,
            1217,
            1443,
            1502,
            1313,
            1491,
            1517,
            1549,
            1482,
            1587,
            1572,
            1596,
            1642
        ],
        "death": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            1,
            2,
            5,
            12,
            9,
            7,
            7,
            15,
            16,
            17,
            16,
            23,
            37,
            46,
            63,
            79,
            69,
            76,
            73,
            75,
            76,
            87,
            96,
            98,
            95,
            97,
            98,
            107,
            115,
            125,
            126,
            121,
            127,
            123,
            119,
            117,
            115,
            109,
            106,
            99,
            95,
            92,
            89,
            93,
            84,
            78,
            61,
            64,
            59,
            64,
            57,
            48,
            50,
            47,
            55,
            53,
            58,
            55,
            48,
            41,
            44,
            31,
            28,
            23,
            27,
            27,
            32,
            32,
            29,
            28,
            34,
            30,
            28,
            26,
            25,
            23,
            22,
            24,
            21,
            18,
            21,
            23,
            19,
            18,
            17,
            17,
            15,
            14,
            15,
            18,
            17,
            19,
            21,
            23,
            22,
            23,
            24,
            27,
            24,
            21,
            19,
            17,
            15,
            18,
            16,
            19,
            17,
            19,
            19,
            16,
            19,
            22,
            18,
            23,
            21,
            19,
            19,
            20,
            17,
            21,
            18,
            17,
            16,
            17,
            18,
            19,
            18,
            17,
            16,
            17,
            17,
            15,
            14,
            15,
            17,
            19,
            18,
            19,
            18,
            19,
            14,
            15,
            16,
            15,
            14,
            15,
            18,
            21,
            22,
            21,
            19,
            22,
            20,
            23,
            19,
            22,
            22,
            19,
            18,
            24,
            20,
            26,
            36,
            39,
            42,
            44,
            47,
            45,
            49
        ],
        "recovered": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            28,
            35,
            57,
            81,
            90,
            82,
            69,
            302,
            256,
            284,
            256,
            264,
            296,
            281,
            542,
            481,
            511,
            842,
            875,
            1415,
            1542,
            1822,
            1523,
            1454,
            1488,
            1559,
            2014,
            3246,
            3845,
            3558,
            4651,
            5018,
            5231,
            4846,
            4922,
            4451,
            4892,
            5015,
            5119,
            4917,
            4782,
            3412,
            3084,
            3211,
            3089,
            3109,
            2826,
            2315,
            2103,
            2004,
            1825,
            1615,
            1318,
            1092,
            1003,
            1121,
            1491,
            1092,
            1321,
            1492,
            1286,
            1576,
            1594,
            1021,
            989,
            974,
            974,
            931,
            926,
            1622,
            1922,
            2647,
            3411,
            3218,
            2241,
            1021,
            1242,
            985,
            1330,
            947,
            1015,
            1261,
            1382,
            1494,
            1312,
            1412,
            1293,
            1315,
            1386,
            1472,
            1492,
            1984,
            1413,
            1214,
            1302,
            2311,
            1543,
            1313,
            1188,
            2315,
            2297,
            2219,
            2879,
            1493,
            1334,
            1298,
            1156,
            1049,
            1013,
            1087,
            1014,
            1179,
            997,
            992,
            1009,
            1203,
            1151,
            1009,
            1103,
            1010,
            982,
            1092,
            996,
            982,
            996,
            981,
            978,
            1003,
            994,
            1015,
            1040,
            1028,
            1082,
            1103,
            1211,
            1185,
            934,
            968,
            923,
            992,
            997,
            1002,
            942,
            1002,
            882,
            772,
            801,
            795,
            743,
            887,
            1002,
            995,
            1017,
            1003,
            1027,
            1087,
            1003,
            947,
            1211
        ],
        "test": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            7533,
            7641,
            9982,
            11535,
            15422,
            14396,
            18757,
            16160,
            19664,
            20065,
            21400,
            20023,
            24900,
            28578,
            30864,
            33170,
            35720,
            34456,
            33070,
            34090,
            40427,
            40270,
            40520,
            35344,
            39703,
            39429,
            37535,
            40962,
            38351,
            38308,
            30177,
            20143,
            29230,
            43498,
            42004,
            41431,
            36318,
            24001,
            35771,
            33283,
            30303,
            30395,
            33687,
            35605,
            36187,
            32722,
            37351,
            33332,
            34821,
            38565,
            42236,
            35369,
            25141,
            25382,
            20838,
            33633,
            37507,
            40178,
            24589,
            21492,
            19853,
            21043,
            33559,
            36155,
            39230,
            35600,
            31525,
            32325,
            52305,
            54234,
            57829,
            35846,
            35335,
            39361,
            37225,
            36521,
            49190,
            41013,
            45092,
            45176,
            42032,
            46800,
            52901,
            48412,
            41316,
            41112,
            40496,
            41413,
            42982,
            53486,
            52303,
            51198,
            45213,
            48309,
            51014,
            50492,
            52313,
            49714,
            52141,
            46414,
            52193,
            50545,
            49302,
            50103,
            48787,
            48813,
            45232,
            46492,
            43231,
            42320,
            42411,
            41215,
            40943,
            41310,
            43404,
            42846,
            43404,
            43343,
            42986,
            43312,
            40016,
            45283,
            47412,
            45712,
            43967,
            46492,
            44846,
            40247,
            41301,
            46249,
            53842,
            54494,
            56726,
            63842,
            61446,
            62219,
            61716,
            67237,
            66892,
            70192,
            67214,
            65956,
            74846,
            82318,
            87223,
            92301,
            92227,
            93007,
            80302,
            95943,
            98231,
            100109,
            106111,
            107814,
            101414,
            91302,
            110102,
            109443,
            107927,
            110225
        ]
    },
    "dates": [
        "2020/03/11",
        "2020/03/12",
        "2020/03/13",
        "2020/03/14",
        "2020/03/15",
        "2020/03/16",
        "2020/03/17",
        "2020/03/18",
        "2020/03/19",
        "2020/03/20",
        "2020/03/21",
        "2020/03/22",
        "2020/03/23",
        "2020/03/24",
        "2020/03/25",
        "2020/03/26",
        "2020/03/27",
        "2020/03/28",
        "2020/03/29",
        "2020/03/30",
        "2020/03/31",
        "2020/04/01",
        "2020/04/02",
        "2020/04/03",
        "2020/04/04",
        "2020/04/05",
        "2020/04/06",
        "2020/04/07",
        "2020/04/08",
        "2020/04/09",
        "2020/04/10",
        "2020/04/11",
        "2020/04/12",
        "2020/04/13",
        "2020/04/14",
        "2020/04/15",
        "2020/04/16",
        "2020/04/17",
        "2020/04/18",
        "2020/04/19",
        "2020/04/20",
        "2020/04/21",
        "2020/04/22",
        "2020/04/23",
        "2020/04/24",
        "2020/04/25",
        "2020/04/26",
        "2020/04/27",
        "2020/04/28",
        "2020/04/29",
        "2020/04/30",
        "2020/05/01",
        "2020/05/02",
        "2020/05/03",
        "2020/05/04",
        "2020/05/05",
        "2020/05/06",
        "2020/05/07",
        "2020/05/08",
        "2020/05/09",
        "2020/05/10",
        "2020/05/11",
        "2020/05/12",
        "2020/05/13",
        "2020/05/14",
        "2020/05/15",
        "2020/05/16",
        "2020/05/17",
        "2020/05/18",
        "2020/05/19",
        "2020/05/20",
        "2020/05/21",
        "2020/05/22",
        "2020/05/23",
        "2020/05/24",
        "2020/05/25",
        "2020/05/26",
        "2020/05/27",
        "2020/05/28",
        "2020/05/29",
        "2020/05/30",
        "2020/05/31",
        "2020/06/01",
        "2020/06/02",
        "2020/06/03",
        "2020/06/04",
        "2020/06/05",
        "2020/06/06",
        "2020/06/07",
        "2020/06/08",
        "2020/06/09",
        "2020/06/10",
        "2020/06/11",
        "2020/06/12",
        "2020/06/13",
        "2020/06/14",
        "2020/06/15",
        "2020/06/16",
        "2020/06/17",
        "2020/06/18",
        "2020/06/19",
        "2020/06/20",
        "2020/06/21",
        "2020/06/22",
        "2020/06/23",
        "2020/06/24",
        "2020/06/25",
        "2020/06/26",
        "2020/06/27",
        "2020/06/28",
        "2020/06/29",
        "2020/06/30",
        "2020/07/01",
        "2020/07/02",
        "2020/07/03",
        "2020/07/05",
        "2020/07/06",
        "2020/07/07",
        "2020/07/08",
        "2020/07/09",
        "2020/07/10",
        "2020/07/11",
        "2020/07/12",
        "2020/07/13",
        "2020/07/14",
        "2020/07/15",
        "2020/07/16",
        "2020/07/17",
        "2020/07/18",
        "2020/07/19",
        "2020/07/20",
        "2020/07/21",
        "2020/07/22",
        "2020/07/23",
        "2020/07/24",
        "2020/07/25",
        "2020/07/26",
        "2020/07/27",
        "2020/07/28",
        "2020/07/29",
        "2020/07/30",
        "2020/07/31",
        "2020/08/01",
        "2020/08/02",
        "2020/08/03",
        "2020/08/04",
        "2020/08/05",
        "2020/08/06",
        "2020/08/07",
        "2020/08/08",
        "2020/08/09",
        "2020/08/10",
        "2020/08/11",
        "2020/08/12",
        "2020/08/13",
        "2020/08/14",
        "2020/08/15",
        "2020/08/16",
        "2020/08/17",
        "2020/08/18",
        "2020/08/19",
        "2020/08/20",
        "2020/08/21",
        "2020/08/22",
        "2020/08/23",
        "2020/08/24",
        "2020/08/25",
        "2020/08/26",
        "2020/08/27",
        "2020/08/28",
        "2020/08/29",
        "2020/08/30",
        "2020/08/31",
        "2020/09/01",
        "2020/09/02",
        "2020/09/03"
    ],
    "total": {
        "case": [
            1,
            1,
            5,
            6,
            18,
            47,
            98,
            191,
            359,
            670,
            947,
            1236,
            1529,
            1872,
            2433,
            3629,
            5698,
            7402,
            9217,
            10827,
            13531,
            15679,
            18135,
            20921,
            23934,
            27069,
            30217,
            34109,
            38226,
            42282,
            47029,
            52167,
            56956,
            61049,
            65111,
            69392,
            74193,
            78546,
            82329,
            86306,
            90980,
            95591,
            98674,
            101790,
            104912,
            107773,
            110130,
            112261,
            114653,
            117589,
            120204,
            122392,
            124375,
            126045,
            127659,
            129491,
            131744,
            133721,
            135569,
            137115,
            138657,
            139771,
            141475,
            143114,
            144749,
            146457,
            148067,
            149435,
            150593,
            151615,
            152587,
            153548,
            154500,
            155686,
            156827,
            157814,
            158762,
            159797,
            160979,
            162120,
            163103,
            163942,
            164769,
            165555,
            166422,
            167410,
            168340,
            169218,
            170132,
            171121,
            172114,
            173036,
            174023,
            175218,
            176677,
            178239,
            179831,
            181298,
            182727,
            184031,
            185245,
            186493,
            187685,
            188897,
            190165,
            191657,
            193115,
            194511,
            195883,
            197239,
            198613,
            199906,
            201098,
            202284,
            203456,
            205758,
            206844,
            207897,
            208938,
            209962,
            210965,
            211981,
            212993,
            214001,
            214993,
            215940,
            216873,
            217799,
            218717,
            219641,
            220572,
            221500,
            222402,
            223315,
            224252,
            225173,
            226100,
            227019,
            227982,
            228924,
            229891,
            230873,
            231869,
            232856,
            233851,
            234934,
            236112,
            237265,
            238450,
            239622,
            240804,
            241997,
            243180,
            244392,
            245635,
            246861,
            248117,
            249309,
            250524,
            251805,
            253108,
            254520,
            255723,
            257032,
            258249,
            259692,
            261194,
            262507,
            263998,
            265515,
            267064,
            268546,
            270133,
            271705,
            273301,
            274943
        ],
        "death": [
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            2,
            4,
            9,
            21,
            30,
            37,
            44,
            59,
            75,
            92,
            108,
            131,
            168,
            214,
            277,
            356,
            425,
            501,
            574,
            649,
            725,
            812,
            908,
            1006,
            1101,
            1198,
            1296,
            1403,
            1518,
            1643,
            1769,
            1890,
            2017,
            2140,
            2259,
            2376,
            2491,
            2600,
            2706,
            2805,
            2900,
            2992,
            3081,
            3174,
            3258,
            3336,
            3397,
            3461,
            3520,
            3584,
            3641,
            3689,
            3739,
            3786,
            3841,
            3894,
            3952,
            4007,
            4055,
            4096,
            4140,
            4171,
            4199,
            4222,
            4249,
            4276,
            4308,
            4340,
            4369,
            4397,
            4431,
            4461,
            4489,
            4515,
            4540,
            4563,
            4585,
            4609,
            4630,
            4648,
            4669,
            4692,
            4711,
            4729,
            4746,
            4763,
            4778,
            4792,
            4807,
            4825,
            4842,
            4861,
            4882,
            4905,
            4927,
            4950,
            4974,
            5001,
            5025,
            5046,
            5065,
            5082,
            5097,
            5115,
            5131,
            5150,
            5167,
            5186,
            5225,
            5241,
            5260,
            5282,
            5300,
            5323,
            5344,
            5363,
            5382,
            5402,
            5419,
            5440,
            5458,
            5475,
            5491,
            5508,
            5526,
            5545,
            5563,
            5580,
            5596,
            5613,
            5630,
            5645,
            5659,
            5674,
            5691,
            5710,
            5728,
            5747,
            5765,
            5784,
            5798,
            5813,
            5829,
            5844,
            5858,
            5873,
            5891,
            5912,
            5934,
            5955,
            5974,
            5996,
            6016,
            6039,
            6058,
            6080,
            6102,
            6121,
            6139,
            6163,
            6183,
            6209,
            6245,
            6284,
            6326,
            6370,
            6417,
            6462,
            6511
        ],
        "icuPatient": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            344,
            445,
            568,
            725,
            847,
            979,
            1101,
            1251,
            1311,
            1381,
            1415,
            1474,
            1492,
            1552,
            1667,
            1626,
            1665,
            1786,
            1809,
            1820,
            1854,
            1845,
            1894,
            1922,
            1909,
            1865,
            1814,
            1816,
            1790,
            1782,
            1776,
            1736,
            1621,
            1574,
            1514,
            1480,
            1445,
            1424,
            1384,
            1338,
            1278,
            1260,
            1219,
            1168,
            1154,
            1126,
            1045,
            998,
            963,
            944,
            906,
            914,
            903,
            882,
            877,
            820,
            800,
            775,
            769,
            756,
            739,
            723,
            683,
            662,
            649,
            648,
            651,
            633,
            612,
            602,
            592,
            591,
            613,
            625,
            642,
            631,
            643,
            664,
            684,
            717,
            722,
            732,
            745,
            755,
            769,
            781,
            803,
            846,
            893,
            914,
            941,
            963,
            984,
            996,
            1018,
            1026,
            1035,
            1067,
            1082,
            1127,
            1130,
            1152,
            1172,
            1179,
            1182,
            1194,
            1209,
            1223,
            1204,
            1206,
            1213,
            1226,
            1231,
            1246,
            1243,
            1246,
            1244,
            1251,
            1248,
            1252,
            1249,
            1263,
            1280,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null
        ],
        "intubatedPatient": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            241,
            309,
            394,
            523,
            622,
            692,
            783,
            867,
            909,
            935,
            966,
            987,
            995,
            1017,
            1062,
            1021,
            978,
            1063,
            1087,
            1052,
            1040,
            1014,
            1054,
            1031,
            1033,
            1006,
            985,
            982,
            929,
            900,
            883,
            882,
            845,
            831,
            803,
            818,
            778,
            766,
            727,
            707,
            669,
            665,
            653,
            628,
            598,
            578,
            576,
            535,
            508,
            490,
            474,
            468,
            463,
            455,
            445,
            424,
            401,
            388,
            385,
            371,
            338,
            331,
            339,
            324,
            308,
            287,
            283,
            271,
            261,
            265,
            269,
            264,
            274,
            261,
            281,
            280,
            266,
            282,
            284,
            290,
            291,
            303,
            306,
            311,
            310,
            318,
            327,
            345,
            362,
            356,
            369,
            382,
            366,
            381,
            375,
            368,
            362,
            372,
            374,
            392,
            395,
            400,
            406,
            399,
            402,
            401,
            409,
            402,
            396,
            401,
            394,
            402,
            394,
            398,
            385,
            379,
            381,
            378,
            379,
            386,
            387,
            392,
            403,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null
        ],
        "pneumoniaPercent": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            9.4,
            9.3,
            8.8,
            8.7,
            8.5,
            8.4,
            8.5,
            8.4,
            8.3,
            8.3,
            8.1,
            8.1,
            8.2,
            8.2,
            8.2,
            7.9,
            7.8,
            7.6,
            7.6,
            7.5,
            7.5,
            7.4,
            7.3,
            7.3,
            7.4,
            7.5,
            7.4,
            7.4,
            7.4,
            7.3,
            7.4,
            7.4,
            7.5,
            7.5,
            7.6,
            7.6,
            7.6
        ],
        "recovered": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            42,
            70,
            105,
            162,
            243,
            333,
            415,
            484,
            786,
            1042,
            1326,
            1582,
            1846,
            2142,
            2423,
            2965,
            3446,
            3957,
            4799,
            5674,
            7089,
            8631,
            10453,
            11976,
            13430,
            14918,
            16477,
            18491,
            21737,
            25582,
            29140,
            33791,
            38809,
            44022,
            48886,
            53808,
            58259,
            63151,
            68166,
            73285,
            78202,
            82984,
            86396,
            89480,
            92691,
            95780,
            98889,
            101715,
            104030,
            106133,
            108137,
            109962,
            111577,
            112895,
            113987,
            114990,
            116111,
            117602,
            118694,
            120015,
            121507,
            122793,
            124369,
            125963,
            126984,
            127973,
            128947,
            129921,
            130852,
            131778,
            133400,
            135322,
            137969,
            141380,
            144598,
            146839,
            147860,
            149102,
            150087,
            151417,
            152364,
            153379,
            154640,
            156022,
            157516,
            158828,
            169240,
            161533,
            162848,
            164234,
            165706,
            167198,
            169182,
            170595,
            171809,
            173111,
            175422,
            176965,
            178278,
            180680,
            182995,
            185292,
            187511,
            190390,
            191883,
            193217,
            194515,
            195671,
            196720,
            197733,
            198820,
            199834,
            201013,
            202010,
            203002,
            204011,
            205214,
            206365,
            207374,
            208477,
            209487,
            210469,
            211561,
            212557,
            213539,
            214535,
            215516,
            216494,
            217497,
            218491,
            219506,
            220546,
            221574,
            222656,
            223759,
            224970,
            226155,
            227089,
            228057,
            228980,
            229972,
            230969,
            231971,
            232913,
            233915,
            234797,
            235569,
            236370,
            237165,
            237908,
            238795,
            239797,
            240792,
            241809,
            242812,
            243839,
            244926,
            245929,
            246876,
            248087
        ],
        "seriouslyIllPatient": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            542,
            561,
            582,
            586,
            582,
            580,
            583,
            582,
            580,
            586,
            587,
            596,
            603,
            617,
            632,
            647,
            656,
            668,
            679,
            686,
            703,
            719,
            735,
            749,
            762,
            783,
            796,
            811,
            841,
            862,
            896,
            917,
            945,
            961,
            991,
            1017,
            1041
        ],
        "test": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            47823,
            55464,
            65446,
            76981,
            92403,
            106799,
            125556,
            141716,
            161380,
            181445,
            202845,
            222868,
            247768,
            276338,
            307210,
            340380,
            376100,
            410556,
            443626,
            477716,
            518143,
            558413,
            598933,
            634277,
            673980,
            713409,
            750944,
            791906,
            830257,
            868565,
            898742,
            918885,
            948115,
            991613,
            1033617,
            1075048,
            1111366,
            1135367,
            1171138,
            1204421,
            1234724,
            1265119,
            1298806,
            1334411,
            1370598,
            1403320,
            1440671,
            1474003,
            1508824,
            1547389,
            1589625,
            1624994,
            1650135,
            1675517,
            1696355,
            1729988,
            1767495,
            1807673,
            1832262,
            1853754,
            1873607,
            1894650,
            1928209,
            1964364,
            2003594,
            2039194,
            2070719,
            2103044,
            2155349,
            2209583,
            2267412,
            2303258,
            2338593,
            2377954,
            2415179,
            2451700,
            2500890,
            2541903,
            2586995,
            2632171,
            2674203,
            2721003,
            2773904,
            2822316,
            2863632,
            2904744,
            2945240,
            2986653,
            3029635,
            3083121,
            3135424,
            3186622,
            3231835,
            3280144,
            3331158,
            3381650,
            3433963,
            3483677,
            3535818,
            3630480,
            3682673,
            3733218,
            3782520,
            3832623,
            3881410,
            3930223,
            3975455,
            4021947,
            4065178,
            4107498,
            4149909,
            4191124,
            4232067,
            4273377,
            4316781,
            4359627,
            4403031,
            4446374,
            4489360,
            4532672,
            4572688,
            4617971,
            4665383,
            4711095,
            4454331,
            4800823,
            4845669,
            4885916,
            4927217,
            4973466,
            5027308,
            5081802,
            5138528,
            5202370,
            5263816,
            5326035,
            5387751,
            5454988,
            5521880,
            5592072,
            5659286,
            5725242,
            5800088,
            5882406,
            5969629,
            6061930,
            6154157,
            6247164,
            6327466,
            6423409,
            6521640,
            6621749,
            6727860,
            6835674,
            6937088,
            7028390,
            7138492,
            7247935,
            7355862,
            7466087
        ]
    }
}
```

#### Error Response

**Code:** `404 NOT FOUND`



### Typed Timeseries Dataset

Use to get daily or total timeseries data.

**URL:** `/timeseries/<string:datatype>/`

**URL:** `/timeseries/<string:datatype>/all/`

**Variables:** `datatype = ['daily', 'total']`

**Method:** `GET`

**Auth required:** No

#### Success Response

**Code:** `200 OK`

**Content example**

```json
{
    "cases": [
        "1",
        "1",
        "1",
        "5",
        "6",
        "18",
        "47",
        "98",
        "191",
        "359",
        "670",
        "947",
        "1236",
        "1529",
        "1872",
        "2433",
        "3629",
        "5698",
        "7402",
        "9217",
        "10827",
        "13531",
        "15679",
        "18135",
        "20921",
        "23934",
        "27069",
        "30217"
    ],
    "dateLabels": [
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8"
    ],
    "dates": [
        "10 MARCH 2020",
        "11 MARCH 2020",
        "12 MARCH 2020",
        "13 MARCH 2020",
        "14 MARCH 2020",
        "15 MARCH 2020",
        "16 MARCH 2020",
        "17 MARCH 2020",
        "18 MARCH 2020",
        "19 MARCH 2020",
        "20 MARCH 2020",
        "21 MARCH 2020",
        "22 MARCH 2020",
        "23 MARCH 2020",
        "24 MARCH 2020",
        "25 MARCH 2020",
        "26 MARCH 2020",
        "27 MARCH 2020",
        "28 MARCH 2020",
        "29 MARCH 2020",
        "30 MARCH 2020",
        "31 MARCH 2020",
        "1 APRIL 2020",
        "2 APRIL 2020",
        "3 APRIL 2020",
        "4 APRIL 2020",
        "5 APRIL 2020",
        "6 APRIL 2020",
        "7 APRIL 2020",
        "8 APRIL 2020"
    ],
    "deaths": [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "2",
        "4",
        "9",
        "21",
        "30",
        "37",
        "44",
        "59",
        "75",
        "92",
        "108",
        "131",
        "168",
        "214",
        "277",
        "356",
        "425",
        "501",
        "574",
        "649"
    ],
    "lastUpdated": "2020-04-06"
}
```

#### Error Response

**Code:** `404 NOT FOUND`

**Code**: `400 BAD REQUEST`

**Content Example:**

```
Timeseries data can only be ['daily', 'total']!
```



### Named Timeseries Dataset

Use to get named timeseries data.

**URL:** `/timeseries/daily/<string:dataname>`

**URL:** `/timeseries/total/<string:dataname>`

**Variables:** `For daily: dataname = ['test', 'case', 'death', 'recovered'] `

​					`For total: dataname =['test', 'case', 'death', 'recovered', 'icuPatient', 'intubatedPatient', 'pneumoniaPercent', 'seriouslyIllPatient'] `

**Method:** `GET`

**Auth required:** No

#### Success Response

**Code:** `200 OK`

**Content example**

```json
{
    "daily": {
        "case": [
            1,
            0,
            4,
            1,
            12,
            29,
            51,
            93,
            168,
            311,
            277,
            289,
            293,
            343,
            561,
            1196,
            2069,
            1704,
            1815,
            1610,
            2704,
            2148,
            2456,
            2786,
            3013,
            3135,
            3148,
            3892,
            4117,
            4056,
            4747,
            5138,
            4789,
            4093,
            4062,
            4291,
            4801,
            4353,
            3783,
            3977,
            4674,
            4611,
            3083,
            3116,
            3122,
            2861,
            2357,
            2131,
            2392,
            2936,
            2615,
            2188,
            1983,
            1670,
            1614,
            1832,
            2253,
            1977,
            1848,
            1546,
            1542,
            1114,
            1704,
            1639,
            1635,
            1708,
            1610,
            1368,
            1158,
            1022,
            972,
            961,
            952,
            1186,
            1141,
            987,
            948,
            1035,
            1182,
            1141,
            983,
            839,
            827,
            786,
            867,
            988,
            930,
            878,
            914,
            989,
            993,
            922,
            987,
            1195,
            1459,
            1562,
            1592,
            1467,
            1429,
            1304,
            1214,
            1248,
            1192,
            1212,
            1268,
            1492,
            1458,
            1396,
            1372,
            1356,
            1374,
            1293,
            1192,
            1186,
            1172,
            1148,
            1086,
            1053,
            1041,
            1024,
            1003,
            1016,
            1012,
            1008,
            992,
            947,
            933,
            926,
            918,
            924,
            931,
            928,
            902,
            913,
            937,
            921,
            927,
            919,
            963,
            942,
            967,
            982,
            996,
            987,
            995,
            1083,
            1178,
            1153,
            1185,
            1172,
            1182,
            1193,
            1183,
            1212,
            1243,
            1226,
            1256,
            1192,
            1223,
            1263,
            1303,
            1412,
            1203,
            1309,
            1217,
            1443,
            1502,
            1313,
            1491,
            1517,
            1549,
            1482,
            1587,
            1572,
            1596,
            1642
        ]
    },
    "dates": [
        "2020/03/11",
        "2020/03/12",
        "2020/03/13",
        "2020/03/14",
        "2020/03/15",
        "2020/03/16",
        "2020/03/17",
        "2020/03/18",
        "2020/03/19",
        "2020/03/20",
        "2020/03/21",
        "2020/03/22",
        "2020/03/23",
        "2020/03/24",
        "2020/03/25",
        "2020/03/26",
        "2020/03/27",
        "2020/03/28",
        "2020/03/29",
        "2020/03/30",
        "2020/03/31",
        "2020/04/01",
        "2020/04/02",
        "2020/04/03",
        "2020/04/04",
        "2020/04/05",
        "2020/04/06",
        "2020/04/07",
        "2020/04/08",
        "2020/04/09",
        "2020/04/10",
        "2020/04/11",
        "2020/04/12",
        "2020/04/13",
        "2020/04/14",
        "2020/04/15",
        "2020/04/16",
        "2020/04/17",
        "2020/04/18",
        "2020/04/19",
        "2020/04/20",
        "2020/04/21",
        "2020/04/22",
        "2020/04/23",
        "2020/04/24",
        "2020/04/25",
        "2020/04/26",
        "2020/04/27",
        "2020/04/28",
        "2020/04/29",
        "2020/04/30",
        "2020/05/01",
        "2020/05/02",
        "2020/05/03",
        "2020/05/04",
        "2020/05/05",
        "2020/05/06",
        "2020/05/07",
        "2020/05/08",
        "2020/05/09",
        "2020/05/10",
        "2020/05/11",
        "2020/05/12",
        "2020/05/13",
        "2020/05/14",
        "2020/05/15",
        "2020/05/16",
        "2020/05/17",
        "2020/05/18",
        "2020/05/19",
        "2020/05/20",
        "2020/05/21",
        "2020/05/22",
        "2020/05/23",
        "2020/05/24",
        "2020/05/25",
        "2020/05/26",
        "2020/05/27",
        "2020/05/28",
        "2020/05/29",
        "2020/05/30",
        "2020/05/31",
        "2020/06/01",
        "2020/06/02",
        "2020/06/03",
        "2020/06/04",
        "2020/06/05",
        "2020/06/06",
        "2020/06/07",
        "2020/06/08",
        "2020/06/09",
        "2020/06/10",
        "2020/06/11",
        "2020/06/12",
        "2020/06/13",
        "2020/06/14",
        "2020/06/15",
        "2020/06/16",
        "2020/06/17",
        "2020/06/18",
        "2020/06/19",
        "2020/06/20",
        "2020/06/21",
        "2020/06/22",
        "2020/06/23",
        "2020/06/24",
        "2020/06/25",
        "2020/06/26",
        "2020/06/27",
        "2020/06/28",
        "2020/06/29",
        "2020/06/30",
        "2020/07/01",
        "2020/07/02",
        "2020/07/03",
        "2020/07/05",
        "2020/07/06",
        "2020/07/07",
        "2020/07/08",
        "2020/07/09",
        "2020/07/10",
        "2020/07/11",
        "2020/07/12",
        "2020/07/13",
        "2020/07/14",
        "2020/07/15",
        "2020/07/16",
        "2020/07/17",
        "2020/07/18",
        "2020/07/19",
        "2020/07/20",
        "2020/07/21",
        "2020/07/22",
        "2020/07/23",
        "2020/07/24",
        "2020/07/25",
        "2020/07/26",
        "2020/07/27",
        "2020/07/28",
        "2020/07/29",
        "2020/07/30",
        "2020/07/31",
        "2020/08/01",
        "2020/08/02",
        "2020/08/03",
        "2020/08/04",
        "2020/08/05",
        "2020/08/06",
        "2020/08/07",
        "2020/08/08",
        "2020/08/09",
        "2020/08/10",
        "2020/08/11",
        "2020/08/12",
        "2020/08/13",
        "2020/08/14",
        "2020/08/15",
        "2020/08/16",
        "2020/08/17",
        "2020/08/18",
        "2020/08/19",
        "2020/08/20",
        "2020/08/21",
        "2020/08/22",
        "2020/08/23",
        "2020/08/24",
        "2020/08/25",
        "2020/08/26",
        "2020/08/27",
        "2020/08/28",
        "2020/08/29",
        "2020/08/30",
        "2020/08/31",
        "2020/09/01",
        "2020/09/02",
        "2020/09/03"
    ]
}
```

#### Error Response

**Code:** `404 NOT FOUND`

**Code:** `400 BAD REQUEST`

**Content Example:**

```
Timeseries daily data can only be ['test', 'case', 'death', 'recovered']!
or
Timeseries total data can only be ['test', 'case', 'death', 'recovered', 'icuPatient', 'intubatedPatient',
'pneumoniaPercent', 'seriouslyIllPatient']!
```

