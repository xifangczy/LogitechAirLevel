import ctypes
import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, proxy="127.0.0.1:8080")

LGS = ctypes.windll.LoadLibrary( 'LogitechLedEnginesWrapper.dll' )
LGS.LogiLedInit()

sec = 600

def getAirLevel():
    text = api.get_user('CGChengduAir').timeline()[0].text
    air = int( text.split(';')[3] )
    red,green,blue = 0,0,0
    if air <= 55:
        red,green,blue = 0,0,100
    elif air <= 150:
        red,green,blue = 100,50,0
    elif air <= 250:
        red,green,blue = 100,30,0
    else:
        red,green,blue = 100,0,0
    return red,green,blue

while True:
    try:
        red,green,blue = getAirLevel()
        LGS.LogiLedSetLighting(red, green, blue)
        time.sleep(sec)
    except:
        LGS.LogiLedSetLighting(0,0,0)
        time.sleep(sec)
        pass