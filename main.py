#Posting a picture to twitter using tweepy
import tweepy
import os
import coinmarketcap
import urllib
from exchanges.coindesk import CoinDesk
import time
ACCESS_KEY = 'XXXXXXX'
ACCESS_SECRET = 'XXXXXXX'
CONSUMER_KEY = 'XXXXXXX'
CONSUMER_SECRET = 'XXXXXXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
while True:
    urllib.urlretrieve("http://bitcoinity.org/markets/image?span=24h&size=medium&currency=USD&exchange=coinbase", "price.gif")
    btcprice = str(CoinDesk().get_current_price())
    btcchange = str(coinmarketcap.cap_change_24h('bitcoin'))
    fn = os.path.abspath("price.gif")
    status = ("The bitcoin price is $" + btcprice + ". With a change over the last 24h of " + btcchange + ". #Bitcoin #Price")
    api.update_with_media(fn, status=status)
    time.sleep(1800)

