from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "cloud server running",
        "message": "Hello from Render cloud"
    })


@app.route("/test", methods=["POST"])
def test():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "PC")
    message = data.get("message", "")

    return jsonify({
        "received_from": name,
        "received_message": message,
        "reply": f"Hello {name}, your request reached the cloud successfully."
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
