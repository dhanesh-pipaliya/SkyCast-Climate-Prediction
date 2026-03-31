# src/merge_data.py

import pandas as pd
import os

def merge_datasets():
    try:
        historical = pd.read_csv("data/historical_data.csv")
    except FileNotFoundError:
        print("❌ historical_data.csv not found")
        return

    live_path = "data/climate_data.csv"

    if not os.path.exists(live_path) or os.stat(live_path).st_size == 0:
        print("⚠️ Live dataset is empty. Run API first.")
        return

    live = pd.read_csv(live_path)

    # 🔹 Normalize column names
    historical.columns = historical.columns.str.lower()
    live.columns = live.columns.str.lower()

    print("📊 Historical Columns:", historical.columns)
    print("📊 Live Columns:", live.columns)

    # =========================
    # 🔥 FIX: Map your dataset
    # =========================

    # Rename columns based on your dataset
    historical.rename(columns={
        'last_updated': 'datetime',
        'temperature_celsius': 'temperature',
        'pressure_mb': 'pressure'
    }, inplace=True)

    # Check datetime
    if 'datetime' not in historical.columns:
        print("❌ No datetime column found even after mapping")
        return

    # Convert datetime
    historical['datetime'] = pd.to_datetime(historical['datetime'], errors='coerce')
    live['datetime'] = pd.to_datetime(live['datetime'], errors='coerce')

    # Keep required columns only
    required_cols = ['datetime', 'temperature', 'humidity', 'pressure']

    for col in required_cols:
        if col not in historical.columns:
            historical[col] = None
        if col not in live.columns:
            live[col] = None

    historical = historical[required_cols]
    live = live[required_cols]

    # Merge datasets
    combined = pd.concat([historical, live])

    # Clean data
    combined = combined.sort_values(by='datetime')
    combined = combined.drop_duplicates(subset='datetime')
    combined = combined.ffill()
    combined = combined.reset_index(drop=True)

    # Save final dataset
    combined.to_csv("data/final_climate_data.csv", index=False)

    print("✅ Hybrid dataset created successfully!")
    print("📊 Final Shape:", combined.shape)


if __name__ == "__main__":
    merge_datasets()