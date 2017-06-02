#!/usr/bin/python

import os
import time
from slackclient import SlackClient
import urllib2
from bs4 import BeautifulSoup
import texttable

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else '\n' for i in text])

def print_schedule():

    URL = "https://ctftime.org/"
    response = urllib2.urlopen(URL+"event/list/upcoming")
    html = response.read()
    soup = BeautifulSoup(html, "lxml")

    ctf = [[]]

    elements = soup.find_all("td")
    links = soup.find_all("a")

    for i in range(7):
	
	ctf_info = []
	ctf_link = "N/A"
	
	#for k in range(4):

        ctf_name = remove_non_ascii_1(elements[7*i].get_text()).lstrip().replace("\n","") 
        ctf_time = remove_non_ascii_1(elements[7*i+1].get_text()).lstrip().replace("\n","")
        ctf_type = remove_non_ascii_1(elements[7*i+2].get_text()).lstrip().replace("\n","")
        ctf_loca = remove_non_ascii_1(elements[7*i+3].get_text()).lstrip().replace("\n","")
        
        ctf_type = ctf_type+"\n"+ctf_loca
	
        #ctf_info.append( remove_non_ascii_1(elements[7*i+k].get_text()).lstrip().replace("\n","") )

	link = str(links[i+49].get("href"))
	info_URL = URL+link[1:]
	small_soup = BeautifulSoup( urllib2.urlopen(info_URL).read(), "lxml")
	info = small_soup.find_all("p")
	for i in range(10):
	    if ("Official URL" in info[i].get_text()):
		ctf_link = info[i].get_text()[14:]

	ctf.append([ctf_name,ctf_time,ctf_type,ctf_link])

    table = texttable.Texttable()
    table.add_rows(ctf)
    table.set_cols_align(['l','r','r','l'])
    table.set_cols_width([20,28,18,32])
    table.header(['CTF','Time','Type','Link'])
    return "```" + table.draw() + "```"

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

# starterbot's ID as an environment variable
BOT_ID = "U5GPQHSS2" 
BOT_TOKEN = "xoxb-186806604886-fPXUChtMjUrCBnQqVpU7wl36"
# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "schedule"

# instantiate Slack & Twilio clients
slack_client = SlackClient(BOT_TOKEN)

if __name__ == "__main__":
    
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:

            command, channel = parse_slack_output(slack_client.rtm_read())
            print channel
            if command and channel:
                slack_client.api_call("chat.postMessage", channel=channel, text=print_schedule(), as_user=True)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
