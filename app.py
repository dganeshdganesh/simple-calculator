from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"message": "Ganesh Calculator backend is running"})

if __name__ == "__main__":
    app.run(debug=True)
