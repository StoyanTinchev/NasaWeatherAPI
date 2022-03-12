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

    if longitude is not None and latitude is not None and redis.contains(longitude + latitude):
        return jsonify(redis.get(longitude + latitude))

    result = dict()
    result["sol_keys"] = list()
    for i in range(6):
        weather = WeatherController().get_weather()
        result["sol_keys"].append(weather)

    if longitude is not None and latitude is not None:
        redis.set(longitude + latitude, result)

    return jsonify(result)


if __name__ == "__main__":
    redis = RedisCustom()
    redis.daemon = True
    redis.start()
    app.run(host="0.0.0.0", port=60)
