import threading
import requests as requests
from urllib.parse import urlencode
from praw import *

from Vertification import *

class Uploader(threading.Thread):
    def __init__(self, threadID, name,reddit: Reddit):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.reddit=reddit
    def createUploadURL(self,reddit):
        properties=reddit.config.custom
        url=properties.get('mixdrop_url')
        api=properties.get('mixdrop_upload_api')
        key=properties.get('mixdrop_key')
        email=properties.get('mixdrop_email')
        query=urlencode({'key':key,'email':email,'url':self.name})
        return url+'/'+api+'?'+query

    def run(self):
        UPLOAD_URL=self.createUploadURL(self.reddit)
        response=requests.get(UPLOAD_URL).json()
        if type(response)==list:
            print('Uploading',self.threadID)
            FILE_UPLOAD_ID=response.get('result').get('id')
            if(response.get('success')==True):
                print('Uploaded',response.get('result').get('id'))
                print('Verifying',self.threadID)
                verification=Verification(reddit)
            else:
                print('response',response)
