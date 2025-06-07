from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Prometheus Monitoring Exercise!"

@app.route("/metrics")
def metrics():
    # Simulate a custom metric (e.g., "hits")
    hits = random.randint(1, 10)
    return f"myapp_hits_total {hits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
