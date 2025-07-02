import requests
import zipfile
from io import BytesIO
import os
import time
from datetime import datetime, timedelta
import pandas
import shutil



#zip_file_url="https://data.binance.vision/data/spot/daily/klines/BTCUSDT/1m/BTCUSDT-1m-2025-06-29.zip"


DATA_PARAMS = {
    "START_DATE" : datetime(2017, 8, 17),
    "END_DATE" : datetime(2025, 6 , 29),
    "BASE_URL" : "https://data.binance.vision/data/spot/daily/klines/BTCUSDT/1m/BTCUSDT-1m-"
}


def get_date_range(start, end, interval="days"):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def get_price_data():
    u = DATA_PARAMS["BASE_URL"] + DATA_PARAMS["START_DATE"].strftime("%Y-%m-%d") + ".zip"
    r = requests.get(u, stream=True)
    z = zipfile.ZipFile(BytesIO(r.content))
    z.extractall(path="/home/rodrigo/desktop/BTCUSDT-1m")