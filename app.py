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

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()  # Assuming it returns a list of items
        return render_template("data.html", data=data)
    else:
        return f"Error fetching data: {response.status_code}"

if __name__ == "__main__":
    app.run(debug=True)
