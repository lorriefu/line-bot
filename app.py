# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 15:19:14 2021

@author: User
"""

#web app
#架設伺服器
#flask 寫的 網頁程式

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('RKck44Sp8MEbUfKmy8asr3eDBu6IG59WhwN0WEfWEw3TOJxjQKg2naSQgN2sIrOGrEBKQiZJ1xZ8alMZ76mQ4DP3FvFO4hejSydN5dHWOt+YWNRvBrVtEJCAXF9xu1zwTUQrjDRAzWK1uyYEFQ9S6gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5029b0ae969f565d4ddbe70ead33a7f5')



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()