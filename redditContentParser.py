from praw import *
import requests as requests

class redditContentParser:
    def __init__(self):
        pass
    def parse(url:str,reddit: Reddit):
        old_url=url
        url=url.split('?')[0]+'.json?'+url.split('?')[1]
        #response=reddit.get(url)
        response=requests.get(url,headers = {"User-Agent": reddit.config.custom.get('user_agent')}).json()
        if type(response)==dict:
            return response
        else:
            return response[0].get('data').get('children')[0].get('data').get('url')
