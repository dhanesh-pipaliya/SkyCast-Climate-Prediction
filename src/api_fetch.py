# src/api_fetch.py

import requests
import pandas as pd
from datetime import datetime
import os

API_KEY = "ca826bb501b4c7c0133d0c276e9093a4"
CITY = "Rajkot"

def fetch_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print("❌ Error fetching data:", response.text)
        return None

    data = response.json()

    record = {
        "datetime": datetime.now(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"]
    }

    return record


def save_to_csv(record):
    if record is None:
        return

    file_path = "data/climate_data.csv"
    df = pd.DataFrame([record])

    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)

    print("✅ Data saved:", record)


if __name__ == "__main__":
    record = fetch_weather_data()
    save_to_csv(record)
