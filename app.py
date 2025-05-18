from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_json()
    print("受信したイベント:", body)
    return 'OK'

@app.route("/", methods=["GET"])
def index():
    return "LINE Webhook Server is running."

if __name__ == "__main__":
    app.run()
