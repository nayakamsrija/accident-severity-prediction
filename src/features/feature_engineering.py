import pandas as pd


def add_time_features(df: pd.DataFrame, time_col: str = "Start_Time") -> pd.DataFrame:
    out = df.copy()
    out[time_col] = pd.to_datetime(out[time_col], errors="coerce")

    out["year"] = out[time_col].dt.year
    out["month"] = out[time_col].dt.month
    out["day"] = out[time_col].dt.day
    out["hour"] = out[time_col].dt.hour
    out["dow"] = out[time_col].dt.dayofweek

    out["is_weekend"] = (out["dow"] >= 5).astype(int)
    out["is_morning_peak"] = ((out["hour"] >= 6) & (out["hour"] <= 9)).astype(int)
    out["is_evening_peak"] = ((out["hour"] >= 16) & (out["hour"] <= 19)).astype(int)

    return out


def add_weather_flags(df: pd.DataFrame, weather_col: str = "Weather_Condition") -> pd.DataFrame:
    out = df.copy()
    if weather_col not in out.columns:
        out["is_rain"] = 0
        out["is_snow"] = 0
        out["is_fog"] = 0
        out["is_thunder"] = 0
        out["is_wind"] = 0
        return out

    weather = out[weather_col].fillna("").astype(str).str.lower()
    out["is_rain"] = weather.str.contains(r"rain|drizzle|shower", regex=True).astype(int)
    out["is_snow"] = weather.str.contains(r"snow|sleet|ice|wintry", regex=True).astype(int)
    out["is_fog"] = weather.str.contains(r"fog|mist|haze", regex=True).astype(int)
    out["is_thunder"] = weather.str.contains(r"thunder|t-storm|storm", regex=True).astype(int)
    out["is_wind"] = weather.str.contains(r"wind", regex=True).astype(int)
    return out


def add_is_night_flag(
    df: pd.DataFrame,
    sunrise_sunset_col: str = "Sunrise_Sunset",
    hour_col: str = "hour",
) -> pd.DataFrame:
    out = df.copy()
    if sunrise_sunset_col in out.columns:
        out["is_night"] = (out[sunrise_sunset_col] == "Night").astype(int)
        return out

    if hour_col not in out.columns:
        out["is_night"] = 0
        return out

    out["is_night"] = ((out[hour_col] < 6) | (out[hour_col] >= 20)).astype(int)
    return out

