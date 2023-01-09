import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
os.environ['SLACK_TOKEN']='xoxb-4609100328387-4602630824710-BRBtB62iYvsDYCIMIFLCinAV'
os.environ['SIGNING_SECRET']='ed06853f7aa10f5d63d832ef94c5a3db'
app=Flask(__name__)
slack_event_adapter=SlackEventAdapter(os.getenv('SIGNING_SECRET'),'/slack/events', app)
client=slack.WebClient(token=os.getenv('SLACK_TOKEN'))
BOT_ID=client.api_call("auth.test")['user_id']
@slack_event_adapter.on('message')
def message(payload):
    event=payload.get('event',{})
    channel_id=event.get('channel')
    user_id=event.get('user')
    text=event.get('text')
    f=open('bot.txt','a')
    if BOT_ID!=user_id:
        #client.chat_postMessage(channel=channel_id,text=text)
        print(text,file=f)
    f.close()
if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
