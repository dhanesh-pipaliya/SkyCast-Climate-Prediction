# src/data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    try:
        df = pd.read_csv("data/climate_data.csv")
    except FileNotFoundError:
        print("❌ Dataset not found. Run previous stages.")
        return

    print("📊 Dataset Loaded Successfully")
    print(df.head())

    # Convert datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # ==============================
    # 📈 Temperature Trend
    # ==============================
    plt.figure()
    plt.plot(df['datetime'], df['temperature'])
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/temperature_trend.png")
    plt.close()

    # ==============================
    # 💧 Humidity Trend
    # ==============================
    plt.figure()
    plt.plot(df['datetime'], df['humidity'])
    plt.title("Humidity Trend Over Time")
    plt.xlabel("Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/humidity_trend.png")
    plt.close()

    # ==============================
    # 📊 Temperature Distribution
    # ==============================
    plt.figure()
    plt.hist(df['temperature'], bins=10)
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("images/temperature_distribution.png")
    plt.close()

    print("✅ All graphs saved in 'images/' folder!")

if __name__ == "__main__":
    analyze_data()