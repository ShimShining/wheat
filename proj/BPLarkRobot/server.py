#!/usr/bin/env python3.8
import json
import os
import logging
import requests
from api import MessageApiClient
from event import MessageReceiveEvent, UrlVerificationEvent, EventManager, MessageEvent
from flask import Flask, jsonify
from dotenv import load_dotenv, find_dotenv
from utils import *

# load env parameters form file named .env
load_dotenv(find_dotenv())

app = Flask(__name__)

# load from env
APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
ENCRYPT_KEY = os.getenv("ENCRYPT_KEY")
LARK_HOST = os.getenv("LARK_HOST")


# init service
message_api_client = MessageApiClient(APP_ID, APP_SECRET, LARK_HOST)
event_manager = EventManager()


@event_manager.register("url_verification")
def request_url_verify_handler(req_data: UrlVerificationEvent):
    # url verification, just need return challenge
    app.logger.info(f"req_data={req_data}")
    if req_data.event.token != VERIFICATION_TOKEN:
        raise Exception("VERIFICATION_TOKEN is invalid")
    return jsonify({"challenge": req_data.event.challenge})


@event_manager.register("message")
def message_event_handler(req_data: MessageEvent):

    return jsonify()


@event_manager.register("im.message.receive_v1")
def message_receive_event_handler(req_data: MessageReceiveEvent):
    sender_id = req_data.event.sender.sender_id  #open_id union_id user_id
    # sender = req_data.event.sender   # 'sender_id', 'sender_type'
    message = req_data.event.message
    if message.message_type != "text":
        logging.warn("Other types of messages have not been processed yet")
        return jsonify()
        # get open_id and text_content
    open_id = sender_id.open_id
    text_content = message.content
    msg_id = message.message_id
    # chat_id = message.chat_id
    chat_type = message.chat_type
    # print(f"message.message_id={message.message_id}")
    # print(f"message.chat_id={message.chat_id}")
    print(f"message.chat_type={message.chat_type}")
    # print(text_content)

    # echo text message
    if chat_type == "p2p":
        content = message_handler(text_content, msg_id)
        # message_api_client.send_message(event, content)
        if content:
            msg = dict()
            msg['text'] = content
            reply = json.dumps(msg)
            message_api_client.send_text_with_open_id(open_id, reply)
            return jsonify()
    if chat_type == "group":
        try:
            mentions = message.mentions
            mention_names = [m.name for m in mentions]
            print(f"mention_name={mention_names}")
        except Exception:
            return jsonify()
        if len(mention_names) >= 2:
            return jsonify()
        if "" in mention_names or "BP 小Q" in mention_names:
            content = message_handler(text_content, msg_id)
            # message_api_client.send_message(event, content)
            if content:
                msg = dict()
                msg['text'] = content
                reply = json.dumps(msg)
                # print("群聊触发自动化任务执行 ===>")
                message_api_client.reply(msg_id, "text", reply)
                return jsonify()
        return jsonify()


@app.errorhandler
def msg_error_handler(ex):
    # app.logger.info(f"msg_error_handler======>VERIFICATION_TOKEN:{VERIFICATION_TOKEN}")
    # app.logger.info(f"msg_error_handler======>ENCRYPT_KEY:{ENCRYPT_KEY}")
    logging.error(ex)
    response = jsonify(message=str(ex))
    response.status_code = (
        ex.response.status_code if isinstance(ex, requests.HTTPError) else 500
    )
    return response


@app.route("/larkbot", methods=["POST"])
def callback_event_handler():
    # init callback instance and handle
    # app.logger.info("开始进入callback_event_handler")
    event_handler, event = event_manager.get_handler_with_event(VERIFICATION_TOKEN, ENCRYPT_KEY)
    return event_handler(event)


if __name__ == "__main__":
    # init()
    # docker run --env-file .env -p 30001:30001 -it BPlarkbottest:v1
    app.run(host="0.0.0.0", port=30001, debug=True)