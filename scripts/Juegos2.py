import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

###API ########################


ckey = "6Zyv4XxVypDqHDpFoHwSTrMzX"
csecret = "3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC"
atoken = "153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq"
asecret = "WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO"

#####################################

class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:12345@192.168.1.2:5984/')
try: 
    db = server.create('juegos')

except:
    db = server['juegos']

'''===============LOCATIONS=============='''


twitterStream.filter(track=['Hero Soul: I Want to be a Hero! Demo','Mad Taxi',
'Demolition Expert - The Simulation','The Old House','Clea 2 Demo','REPTOMOM',
'Earth: 9000','TinShift','Artificer: Science of Magic','Rogue Star Rescue Demo','Rubber Toys Demo','Vampire: The Masquerade - Shadows of New York Soundtrack',
'Wildfire Demo'])
