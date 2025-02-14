from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/update-location", methods=["POST"])
def update_location():
    data = request.get_json()
    lat, lon = data["latitude"], data["longitude"]

    with open("live_location.txt", "w") as file:
        file.write(f"{lat}, {lon}\n")

    return jsonify({"message": "Location updated!"})

if __name__ == "__main__":
    app.run(debug=True)
