# src/data_processing.py

import pandas as pd

def clean_data():
    file_path = "data/climate_data.csv"

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("❌ Dataset not found. Run API first.")
        return

    print("📊 Original Data Shape:", df.shape)

    # 🔹 Convert datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # 🔹 Remove duplicates
    df = df.drop_duplicates(subset='datetime')

    # 🔹 Sort by time
    df = df.sort_values(by='datetime')

    # 🔹 Handle missing values (FIXED)
    df = df.ffill()

    # 🔹 Feature engineering (important for ML 🔥)
    df['hour'] = df['datetime'].dt.hour
    df['day'] = df['datetime'].dt.day

    # 🔹 Reset index
    df = df.reset_index(drop=True)

    # 🔹 Save cleaned data
    df.to_csv(file_path, index=False)

    print("✅ Cleaned Data Shape:", df.shape)
    print("🧹 Data cleaning completed successfully!")

if __name__ == "__main__":
    clean_data()