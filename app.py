from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = "ioxbe5mefnp64gkCluPbVq6HBCWhmnyXk0vHwKKa0n3R7TtndZfWPPQgPLmO1lDL"
@app.route("/")
def index():
    url = "https://api.example.com/data"  # Replace with your actual API URL
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # raises error for bad HTTP status
        data = response.json()
    except Exception as e:
        print("API error:", e)
        # Show empty table or custom fallback
        data = [
            {"name": "John Doe", "email": "john@example.com", "phone": "123-456-7890"},
            {"name": "Jane Smith", "email": "jane@example.com", "phone": "987-654-3210"},
            {"name": "Alice Lee", "email": "alice@example.com", "phone": "555-123-4567"},
        ]

    return render_template("data.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
