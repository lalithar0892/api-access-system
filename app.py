from flask import Flask, request, jsonify

app = Flask(__name__)

# simple memory storage
access_db = {}

# ➕ Add Access
@app.route('/add', methods=['POST'])
def add_access():
    data = request.get_json()
    user = data.get("user")

    access_db[user] = "granted"
    return jsonify({"message": f"Access granted to {user}"})


# ❌ Remove Access
@app.route('/remove', methods=['POST'])
def remove_access():
    data = request.get_json()
    user = data.get("user")

    if user in access_db:
        access_db[user] = "removed"
        return jsonify({"message": f"Access removed for {user}"})

    return jsonify({"message": "User not found"}), 404


# 🔍 Status API
@app.route('/status/<user>', methods=['GET'])
def status(user):
    status = access_db.get(user, "no access")
    return jsonify({"user": user, "status": status})


if __name__ == "__main__":
    app.run(debug=True)