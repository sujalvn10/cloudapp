from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", "Delhi")  # Default city
    url = f"{https://openweathermap.org/api/one-call-3}?q={city}&appid={https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}}&units=metric"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
