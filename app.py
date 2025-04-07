from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://jsonplaceholder.typicode.com/users"  # Real public API

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print("API error:", e)
        # Dummy fallback data
        data = [
            {"name": "John Doe", "email": "john@example.com", "phone": "123-456-7890"},
            {"name": "Jane Smith", "email": "jane@example.com", "phone": "987-654-3210"},
            {"name": "Alice Lee", "email": "alice@example.com", "phone": "555-123-4567"},
        ]

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
