from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    return jsonify({"data": [1, 2, 3]})

handler = app  # Важно!