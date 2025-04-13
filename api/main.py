from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "OK", "message": "Hello from Python API!"})

@app.route("/api/data")
def get_data():
    return jsonify({"data": [1, 2, 3]})

# Важно: Vercel требует явного экспорта приложения
handler = app