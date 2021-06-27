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
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
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
    msg=event.message.text
    r= '很抱歉，您說什麼'
    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id= '1',
            sticker_id= '1'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message()
        return
    if msg in ['hi', 'hi']:
        r = '嗨'
    elif msg== '你吃飯了嗎':
        r = '還沒'
    elif msg== '你是誰':
        r='我是機器人'
 
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))
 

if __name__ == "__main__":
    app.run()