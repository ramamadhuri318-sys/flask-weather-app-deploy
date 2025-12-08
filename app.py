from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "REPLACE_WITH_YOUR_OWN_KEY"  # just replace with a valid one

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."
        else:
            try:
                url = (
                    "https://api.openweathermap.org/data/2.5/weather"
                    f"?q={city}&appid={API_KEY}&units=metric"
                )
                resp = requests.get(url, timeout=5)

                if resp.status_code == 200:
                    data = resp.json()
                    weather_data = {
                        "city": data["name"],
                        "temp": data["main"]["temp"],
                        "feels_like": data["main"]["feels_like"],
                        "description": data["weather"][0]["description"].title(),
                    }
                else:
                    try:
                        details = resp.json().get("message", "")
                    except Exception:
                        details = resp.text[:200]
                    error = f"API error (status {resp.status_code}): {details}"
            except Exception as exc:
                error = f"Error calling weather API: {exc}"

    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
