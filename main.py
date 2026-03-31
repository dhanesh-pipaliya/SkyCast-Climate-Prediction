from src.api_fetch import fetch_weather_data, save_to_csv
from src.data_processing import clean_data
from src.merge_data import merge_datasets
from src.data_analysis import analyze_data
from src.model import train_model

def main():
    print("🌍 SkyCast Full Pipeline Running...")

    record = fetch_weather_data()
    save_to_csv(record)

    clean_data()
    merge_datasets()
    analyze_data()
    train_model()

    print("✅ Full Pipeline Completed!")

if __name__ == "__main__":
    main()