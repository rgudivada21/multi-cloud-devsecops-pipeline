from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "project": "Multi Cloud DevSecOps Pipeline",
        "status": "Running"
    }


@app.route("/health")
def health():
    return {
        "status": "Healthy"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
