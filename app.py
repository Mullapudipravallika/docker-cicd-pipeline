from flask import Flask
import socket

app = Flask(__name__)

@app.get("/")
def home():
    return {
        "application": "DevOps Demo Application",
        "status": "running",
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
