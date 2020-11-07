"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import request, abort
from python_webapp_flask import app
import os

from linebot import(
    LineBotApi, WebhookHandler
)

from linebot.exceptions import(
    InvalidSignatureError
)

from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage
)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route('/')
def hello_world():
   return "hellow world!"

@app.route("/callback", methods=["POST"])
def callback():
    signature = 
