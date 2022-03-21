class StationStateIndicator:
    STATION_NOT_INITIALIZED = "station_not_initialized"
    STATION_INITIALIZED = "station_initialized"
    READY_FOR_NEW_MISSIONS = 'ready_for_new_missions'
    DRONE_READY_TO_START = "station_ready_to_start"
    MOVED_POSITIONERS_APART = 'moved_positioners_apart'
    ROOF_OPENED = 'roof_opened'
    DRONE_STARTED = "drone_started"
    DRONE_READY_FOR_LANDING = "drone_ready_for_landing"
    DRONE_LANDED = "drone_landed"
    DRONE_SERVICED = "drone_serviced"
    STATION_ERROR = "station_error"


class StationErrors:
    CANNOT_OPEN_ROOF = 'cannot_open_roof'


class CheckEnum:
    CHECK_DRONE_BATTERY_TEMPERATURE = 0
    CHECK_STATION_BATTERY_TEMPERATURE = 1
    CHECK_TRACKER_TEMPERATURE = 2
    CHECK_AUTOMATION_CONNECTION = 3
    CHECK_POWER_MANAGEMENT_CONNECTION = 4
    CHECK_TRACKER_CONNECTION = 5
    CHECK_WEATHER = 6
    CHECK_SOLAR_PANELS_VOLTAGE = 7
    CHECK_CHARGING_CURRENT = 8
