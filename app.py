from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Function to load JSON data
def load_json_data(filename):
    with open(f"src/data_generation/{filename}", "r") as file:
        return json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/activities")
def get_activities():
    activities = load_json_data("activities.json")
    return jsonify(activities)

@app.route("/user_profiles")
def get_user_profiles():
    users = load_json_data("user_profiles.json")
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
