
import tweepy
import logging
from time import sleep
import time
import os


logging.basicConfig()
logger = logging.getLogger("BOT")
logger.setLevel(logging.DEBUG)


consumer_key = "consumer_key"
consumer_secret = "secret"
key = "token"
secret = "token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
print("Welcome {}".format(api.me().screen_name) )
BLACKLIST_WORDS = [
  'RT'
]

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api_handle):
      self.found_retweets = 0
      self.api = api_handle
      self.retweeted = 0
      self.retweet_limit = 2400
    
    def retweet(self, tweet_id):
      rt = self.api.retweet(tweet_id)
      if rt:
        return True
      return False
    def plusOneRT(self):
      currentDay = time.strftime("%d%b") #04Apr
      limitsInFile = None 
      with open(currentDay, 'r') as f:
        limitsInFile = f.read()
      with open(currentDay, 'w') as f:
        count = str(int(limitsInFile) - 1)
        f.write(count)
    def inLimits(self):
      logger.info("Checking Limits")
      currentDay = time.strftime("%d%b") #04Apr
      if os.path.exists(currentDay):
        logger.info("Information file found")
        with open(currentDay, 'r') as f:
          logger.debug(int(f.read()) == 0)
          return not int(f.read()) == 0
      else:
        logger.info("Info file not found. Creating One.")
        with open(currentDay,'w') as f:
          f.write( str( self.retweet_limit ) )
          logger.info("Initial Info Saved!")
          return True

    def on_status(self, status):
      if not self.inLimits():
        logger.info("All Done For Today! Limits are over!")
        return
      else:
        try:
            logger.info("All Ok! Proceeding..")
            if status.lang != 'en':
                logger.warning("Foriegn Language Detected :{}".format(status.lang))
                return
            status_text = status.text
            if "RT" in status_text:
              logger.warning("Skipped Retweet")
              self.found_retweets += 1
              return
            publish = None
            for w in BLACKLIST_WORDS:
              if w.lower() in status_text.lower():
                logger.warning("Skipped For Word: {}".format(w))
                publish = False
                return
            if publish:
              tweet_id = status.id
              try:
                sleep(2)
                self.retweet(tweet_id)  
                self.plusOneRT()
                logger.info("Retweeted {}".format(status_text))
              except Exception as e :
                logger.warning(e)
        except Exception as e:
            logger.warning(e)
    def on_error(self, status_code):
        print("Some Error")
        logger.error(status_code)
               
myStreamListener = MyStreamListener(api)
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['#100DaysOfCode'], languages=['en'], async=True)