from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.json
        print(f"Received POST data: {data}")
        return {"status": "success", "message": "POST received"}, 200
    return {"status": "running", "message": "Service is running"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
