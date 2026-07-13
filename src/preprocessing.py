from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "mobile_app_usage.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "screensense_clean.csv"


SELECTED_COLUMNS = [
    "record_id",
    "year",
    "month",
    "day_of_week",
    "country",
    "age_group",
    "gender",
    "app_category",
    "app_name",
    "subscription_type",
    "daily_screen_time_minutes",
    "session_duration_minutes",
    "sessions_per_day",
    "app_opens_per_day",
    "notifications_received_per_day",
    "notification_settings",
    "primary_usage_time",
    "sleep_disruption_from_phone",
    "screen_time_concern",
    "mental_health_impact",
    "digital_wellbeing_feature_used",
]


def load_data(path=RAW_DATA_PATH):
    return pd.read_csv(path)


def clean_data(df):
    df = df[SELECTED_COLUMNS].copy()

    df["sleep_disruption_from_phone"] = (
        df["sleep_disruption_from_phone"]
        .fillna("Not Reported")
    )

    return df


def save_data(df, path=OUTPUT_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def main():
    df = load_data()
    df = clean_data(df)
    save_data(df)

    print("Cleaned dataset saved.")
    print("Final Shape:", df.shape)
    print("Total Missing Values:", df.isnull().sum().sum())


if __name__ == "__main__":
    main()