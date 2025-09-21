from flask import Flask, jsonify

application = Flask(__name__)   # EB looks for 'application' by default

@application.route("/")
def index():
    return jsonify(message="Hello from Flask on Elastic Beanstalk!")

@application.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
