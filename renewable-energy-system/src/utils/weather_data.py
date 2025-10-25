def load_weather_data(file_path: str) -> pd.DataFrame:
    """Load weather data from a CSV file."""
    return pd.read_csv(file_path)

def get_solar_irradiance(weather_data: pd.DataFrame) -> np.ndarray:
    """Retrieve solar irradiance data from the weather dataset."""
    return weather_data['solar_irradiance'].values

def get_wind_speed(weather_data: pd.DataFrame) -> np.ndarray:
    """Retrieve wind speed data from the weather dataset."""
    return weather_data['wind_speed'].values