import requests as requests
from urllib.parse import urlencode
from praw import *

class Verification:
   def __init__(self,reddit: Reddit):
      self.reddit=reddit
      
   def createVerificationURL(self,reddit):
      properties=reddit.config.custom
      url=properties.get('mixdrop_url')
      api=properties.get('mixdrop_verification_api')
      key=properties.get('mixdrop_key')
      email=properties.get('mixdrop_email')
      query=urlencode({'key':key,'email':email,'id':self.threadID})
      return url+'/'+api+'?'+query
   def run(self):
      print('verifying',self.threadID)
      UPLOAD_URL=self.createVerificationURL(self.reddit)
      req=requests.get(UPLOAD_URL)
      response=req.json()
      print(response)
      if(response.get('success')==True):
         print("Completed",response.get('result').get('completed'))
         print('FILE URL',response.get('result').get('fileurl'))
         return response.get('result')
