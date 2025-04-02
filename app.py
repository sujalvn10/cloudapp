from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", "Delhi")  # Default city
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
