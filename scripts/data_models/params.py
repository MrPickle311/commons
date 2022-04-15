
from pydantic import BaseModel


class DynamicParams(BaseModel):
    max_drone_battery_voltage: float
    min_drone_battery_voltage: float
    drone_battery_max_temp: float
    station_battery_max_temp: float
    tracker_battery_max_temp: float
    env_max_temp: float
    env_max_humidity: float
    env_max_rain_mm: float
    env_max_wind_speed: float
    env_max_gust: float
    min_solar_panels_voltage: float
    miranda_latt: float
    miranda_long: float
    landing_radius: float
    far_landing_radius: float
    follow_interval: float
