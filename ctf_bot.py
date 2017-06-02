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

        ctf_name = remove_non_ascii_1(elements[7*i].get_text()).lstrip().replace("\n","") 
        ctf_time = remove_non_ascii_1(elements[7*i+1].get_text()).lstrip().replace("\n","")
        ctf_type = remove_non_ascii_1(elements[7*i+2].get_text()).lstrip().replace("\n","")
        ctf_loca = remove_non_ascii_1(elements[7*i+3].get_text()).lstrip().replace("\n","")
        
        ctf_type = ctf_type+"\n"+ctf_loca

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
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    
    BOT_ID = "xxxxxxxxx" 
    BOT_TOKEN = "xxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx"
    
    AT_BOT = "<@" + BOT_ID + ">"
    EXAMPLE_COMMAND = "showschedule" 
    READ_WEBSOCKET_DELAY = 1

    slack_client = SlackClient(BOT_TOKEN)
    
    if slack_client.rtm_connect():
        print("Conenction etablished")
        print("CTF Bot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                print("Calling from channel:", channel)
                slack_client.api_call("chat.postMessage", channel=channel, text=print_schedule(), as_user=True)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
