from flask import Flask, jsonify, request

from redis import RedisCustom
from weather_info.weather_controller import WeatherController

app = Flask(__name__)


@app.route("/")
def index():
    return api()


@app.route("/api.nasa.gov/insight_weather", methods=['GET'])
def api():
    longitude: str = request.args.get('longitude')
    latitude: str = request.args.get('latitude')
    print(longitude, latitude)

    weather = WeatherController(longitude, latitude, redis).get_weather()
    return jsonify(weather)


if __name__ == "__main__":
    redis = RedisCustom()
    redis.daemon = True
    redis.start()
    app.run(host="0.0.0.0", port=60)
