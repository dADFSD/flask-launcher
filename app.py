from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
users = {}

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username in users:
        return jsonify({"status": "error", "message": "User exists"}), 400
    users[username] = generate_password_hash(password)
    return jsonify({"status": "success", "message": "Registered"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({"status": "error", "message": "Invalid credentials"}), 400
    return jsonify({"status": "success", "message": "Logged in"}), 200

if __name__ == "__main__":
    app.run()
