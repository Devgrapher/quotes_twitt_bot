from lib.twitt_bot import *
from book_db import *
from datetime import datetime
from unittest import mock
import sys

twitt_num = 0
g_log_file = None

def log(msg):
	time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	outstring = "[%s] %s" % (time, msg)
	print(outstring)

def onTwittMsg(msg):
	'''callback on twitt posting'''
	global twitt_num
	log("%d, %s" % (twitt_num, msg))
	if '#' in msg: # skip it when it's long msg
		twitt_num += 1

def main(path, interval_sec):

	log('initializing...')

	log('load db...')
	db = BookDB.fromFile(path)
	for a in db.parsed:
		print(a)

	log('load twitt bot...')
	bot = TwittBot(db=db.parsed, interval_sec=interval_sec, callback=onTwittMsg)
	TwittBot.oauth_token = '1866109896-vPQPQiwu4TF9ohelvtC7qDdHK7L6RSay0yBQMfa'
	TwittBot.oauth_secret = 'V38V7ALgjnj1iuMRFfTKTxDTYstindaSKZ8NlZufVsI'
	TwittBot.consumer_key = 'NtH2XF9rRmowtQRGSfSz7g'
	TwittBot.consumer_secret = '4DdjR4NHzd7diS9GIWu4eAHruzVx7dnU5KZVDz6Im68'

	log('running...')
	bot.startFrom(twitt_num)

	bot.join() 
	log('terminating...')

if __name__ == "__main__":
	if len(sys.argv) == 3:
		start_index = sys.argv[2] # when fixed the index of db.
		twitt_num = int(start_index)
	if len(sys.argv) >= 2:
		path = sys.argv[1]
	else:
		# for test
		path = '../db/db.json'

	#TwittBot._TwittBot__twittAPI = mock.MagicMock()
	main(path, 60 * 90) # 90 minutes

