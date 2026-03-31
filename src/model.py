# src/model.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def train_model():
    try:
        df = pd.read_csv("data/final_climate_data.csv")
    except FileNotFoundError:
        print("❌ Dataset not found. Run merge step first.")
        return

    print("📊 Dataset Loaded:", df.shape)

    # Convert datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Drop missing values
    df = df.dropna()

    # Convert time to numeric (important for ML)
    df['time'] = df['datetime'].astype(int) // 10**9

    # Features & Target
    X = df[['time']]
    y = df['temperature']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    print("✅ Model Trained Successfully!")

    # Predict future (next 5 hours)
    future_times = []
    last_time = df['time'].iloc[-1]

    for i in range(1, 6):
        future_times.append([last_time + i * 3600])

    predictions = model.predict(future_times)

    print("🔮 Future Predictions:")
    for i, pred in enumerate(predictions):
        print(f"Hour +{i+1}: {pred:.2f} °C")

    # ==========================
    # 📈 Visualization
    # ==========================
    plt.figure()

    # Actual data
    plt.plot(df['datetime'], df['temperature'], label="Actual")

    # Predicted points
    future_dates = pd.to_datetime(future_times, unit='s')
    plt.plot(future_dates, predictions, 'ro', label="Predicted")

    plt.title("Temperature Prediction")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("images/prediction_graph.png")
    plt.close()

    print("📊 Prediction graph saved!")

if __name__ == "__main__":
    train_model()
    
