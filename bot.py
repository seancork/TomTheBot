#!/usr/bin/python
from  configparser import SafeConfigParser
import praw
import random
import logging

logging.basicConfig(filename="simplelog.log",  format='%(asctime)s %(levelname)s %(message)s',level=logging.INFO)

config = SafeConfigParser()
config.read('config.ini')
tom_bot = praw.Reddit(user_agent=config.get('Bot', 'user_agent'),
				      client_id=config.get('Bot', 'client_id'),
				      client_secret=config.get('Bot', 'client_secret'),
				      username=config.get('Bot', 'username'),
				      password=config.get('Bot', 'password'))

AllNewMessages = tom_bot.inbox.unread(limit=None)
for message in AllNewMessages:
	   if "irishfact" in message.body.lower(): 
	   	  unread_messages = []
	   	  unread_messages.append(message)
	   	  print(unread_messages)
	   	  tom_bot.inbox.mark_read(unread_messages)
	   	  what_user = str(message.author)
	   	  logging.basicConfig(filename="simplelog.log",  format='%(asctime)s %(levelname)s %(message)s',level=logging.INFO)
	   	  logging.info('Message sent to: ' +what_user)
	   	  mgs = random.choice(list(open('facts.txt')))
	   	  tom_bot.redditor(what_user).message('random Fact', 'Hello ' +what_user+',\n\n Here is your Irish random fact: \n\n' +mgs)