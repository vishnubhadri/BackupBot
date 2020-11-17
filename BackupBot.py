from praw import *
from praw.models import Message
from internetarchive import upload
import logging
import requests as requests
from urllib.parse import urlencode

from Vertification import *
from Uploader import *
from redditContentParser import *

BASE_URL="https://reddit.com"
class BackupBot:
    _reddit_url:str="";
    _threads={}
    def __init__(self,reddit: Reddit):
        for mention in reddit.inbox.mentions():#.stream
            self._reddit_url=BASE_URL+vars(mention)['context']
            print(self._reddit_url)
            url=redditContentParser.parse(self._reddit_url,reddit)
            self._threads[self._reddit_url]=Uploader(self._reddit_url,url,reddit)
            self._threads[self._reddit_url].start()
            print('File uploaded successfully')
            
            
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
for logger_name in ("praw", "prawcore",'requests'):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG)
   logger.addHandler(handler)

reddit = Reddit("backupBot")
backupBot=BackupBot(reddit)
