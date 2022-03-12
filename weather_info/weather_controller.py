import random

from weather_info.sol_day import SolDay


class WeatherController:
    def __init__(self):
        self.__weather_temperature = {"high": 0, "low": -120}
        self.__weather_pressure = {"high": 0, "low": -120}
        self.__weather_wind = {"high": 0, "low": -120}

    def get_weather(self):
        return SolDay((random.randint(self.__weather_temperature["low"], self.__weather_temperature["high"]),
                       random.randint(self.__weather_pressure["low"], self.__weather_pressure["high"]),
                       random.randint(self.__weather_wind["low"], self.__weather_wind["high"]))).__dict__
