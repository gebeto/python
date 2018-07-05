# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template

import requests
import json
from vk_header import u_header

from urls import get_group_members_url, get_user_url, wall_post_delete_url, u_message_send_url, message_send_url

import os
import re


modules = [f.replace('.py', '') for f in os.listdir('callback_types') if re.match(r'[a-z][\w_]+\.py\b', f)]
callback_types = __import__('callback_types', fromlist=modules)


def action_by_type(cb_type):
    has = hasattr(callback_types, cb_type)
    if has:
        getattr(callback_types, cb_type).run()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join_leave_log', methods=['GET', 'POST'])
def parse_request():

    access_token = "ACCESS_TOKEN"
    confirmation_token = "CONFIRMATION_TOKEN"
    peer_id = "PEER_ID"

    args = request.args

    if args:
        is_group_dialog = True if args.get('group_dialog') else False
        access_token = args.get('access_token')
        peer_id = args.get('peer_id')
        peer_id = (int(peer_id) + 2000000000) if is_group_dialog else peer_id
        confirmation_token = args.get('confirmation_token')
        if not all([access_token, confirmation_token]):
            return "Need all arguments!"

    data = request.get_json()
    if not data and data["type"]:
        return "Need VK Callback!"

    data = request.get_json()
    if data["type"] == "confirmation":
        return confirmation_token

    elif data["type"] == "group_join":
        data["object"]["lang"] = "ru"
        user = requests.get(get_user_url % data["object"]).json()["response"][0]
        members = requests.get(get_group_members_url % {"group_id": data["group_id"]}).json()["response"]["count"]
        user["members"] = members
        msg = u"[id%(id)s|%(first_name)s %(last_name)s] подписался! Нас уже %(members)s!" % user
        requests.get(message_send_url % {
            "message": msg,
            "peer_id": peer_id,
            "access_token": access_token
        })
        return "ok"

    elif data["type"] == "group_leave":
        data["object"]["lang"] = "ru"
        user = requests.get(get_user_url % data["object"]).json()["response"][0]
        members = requests.get(get_group_members_url % {"group_id": data["group_id"]}).json()["response"]["count"]
        user["members"] = members
        msg = u"[id%(id)s|%(first_name)s %(last_name)s] отписался нахрен. Нас уже %(members)s!" % user
        requests.get(message_send_url % {
            "message": msg,
            "peer_id": peer_id,
            "access_token": access_token
        })
        return "ok"

    elif data["type"] == "group_officers_edit":
        levels = ["простолюдином", "модератором", "редактором", "администратором"]
        admin = requests.get(get_user_url % {"user_id": data["object"]["admin_id"], "lang": "ru"}).json()["response"][0]

        msg = u"[id%(id)s|%(first_name)s %(last_name)s] назначил тебя " % admin
        msg += levels[data["object"]["level_new"]]
        msg = requests.get(u_message_send_url % {
            "message": msg,
            "user_id": data["object"]["user_id"],
            "access_token": access_token,
        }).text

    elif data["type"] == "wall_reply_new":
        trusted_groups = [data["object"]["post_owner_id"], -140842621, -150026500]
        if data["object"]["from_id"] < 0 and not data["object"]["from_id"] in trusted_groups:
            requests.get(wall_post_delete_url % {
                "owner_id": data["object"]["post_owner_id"],
                "comment_id": data["object"]["id"],
                "access_token": access_token,
            })

    return "ok"



@app.route('/header', methods=['GET','POST'])
def header_uploader():
    group_id = "GROUP_ID"
    access_token = "ACCESS_TOKEN"
    confirmation_token = "CONFIRMATION_TOKEN"

    args = request.args

    if args:
        access_token = args.get('access_token')
        confirmation_token = args.get('confirmation_token')
        if not all([access_token, confirmation_token]):
            return "Need all arguments!"

    data = request.get_json()
    if not data:
        return "Need VK Callback!"

    group_id = data["group_id"]
    if data["type"] == "confirmation":
        u_header("CONFIRMATION!", access_token, group_id)
        return confirmation_token
    elif data["type"] == "group_join":
        data["object"]["lang"] = "ru"
        user = requests.get(get_user_url % data["object"]).json()["response"][0]
        msg = u"%(first_name)s %(last_name)s подписался!" % user
        u_header(msg, access_token, group_id, bg="#2ecc71")

    elif data["type"] == "group_leave":
        data["object"]["lang"] = "ru"
        user = requests.get(get_user_url % data["object"]).json()["response"][0]
        msg = u"%(first_name)s %(last_name)s отписался нахрен!" % user
        u_header(msg, access_token, group_id)

    elif data["type"] == "wall_post_new":
        msg = data["object"]["text"]
        if data["object"]["from_id"] == data["object"]["owner_id"] and msg.find("SMS:") == 0:
            msg = msg.replace("SMS:", "")
            msg = msg.replace(" \\n ", "\n")
        else:
            user = requests.get(get_user_url % {
                "user_id": data["object"]["from_id"],
                "lang": "ru"
            }).json()["response"][0]
            msg = u"%(first_name)s %(last_name)s создал пост!" % user
        u_header(msg, access_token, group_id, bg="#3498db")

    else:
        u_header("%s" % (json.dumps(data, indent=4)), access_token, group_id, bg="#9b59b6", font_size=26, align="left")

    return "ok"




def check_online(domain):
    # online_check_url = "http://m.vk.com/%s" % domain
    online_check_url = "https://api.vk.com/method/users.get?fields=online&v=5.67&user_ids=%s" % (domain)
    res = requests.get(online_check_url).json()
    res = res["response"][0]
    return (True if res["online"] == 1 else False), res

@app.route('/online', methods=['GET','POST'])
def online():
    bot_token = "GROUP_ID"
    chat_id = "ACCESS_TOKEN"
    msg_send_url = "https://api.telegram.org/bot%(bot_token)s/sendMessage?chat_id=%(chat_id)s&text=%(text)s"

    args = request.args

    if args:
        bot_token = args.get('bot_token')
        chat_id = args.get('chat_id')
        vk_domain = args.get('vk_domain')

        if not all([bot_token, chat_id, vk_domain]):
            return "Need all arguments! bot_token, chat_id, vk_domain"
        online, data = check_online(vk_domain)
        if online:
            requests.get(msg_send_url % {
                "bot_token": bot_token,
                "chat_id": chat_id,
                "text": "User %(first_name)s %(last_name)s https://vk.com/id%(id)s is online!" % data
            })
            return "User %(first_name)s %(last_name)s https://vk.com/id%(id)s is online!" % data
        else:
            return "User %(first_name)s %(last_name)s https://vk.com/id%(id)s is offline! :(" % data
    return str(args)













