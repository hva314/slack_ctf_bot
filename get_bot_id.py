#!/usr/bin/python

import os
from slackclient import SlackClient

BOT_NAME = str(raw_input("Enter your bot name: "))
BOT_TOKEN = str(raw_input("Enter your bot token: "))

slack_client = SlackClient(BOT_TOKEN)

api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
        if 'name' in user and user.get('name') == BOT_NAME:
            print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
else:
    print("could not find bot user with the name " + BOT_NAME)
