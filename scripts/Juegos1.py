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
server = couchdb.Server('http://admin:couchy@localhost:5984/')
try: 
    db = server.create('juegos')

except:
    db = server['juegos']

'''===============LIST OF GAMES=============='''
twitterStream.filter(track=["OkunoKA Madness", "School of Mythology","Gump","No Game No LIFE","Pandemic Bunny","The Rule of Land: Pioneers","The Final Boss Demo","Chickens Madness","World Process","Capital Simulator","Hungry Horace","The Last Show of Mr. Chardish: Demo","Rangok Skies Demo","Bounty Battle","Tamarin","Guild of Darksteel Demo","Microodyssey","AeternoBlade","Knight Arena","Poly Pirates","Alice Sisters","Crown of the Empire","Asian Riddles 2","Sweet Tooth 2","Idle Expanse","Human Diaspora","Beat Flip","Arcanion: Tale of Magi","SpermDash Soundtrack","Sakura Dimensions","Outbreak New Dawn", "Adriatic Pizza","HOLIDAYS","Sunset Shapes","Arabian Treasures: Midnight Match","Immersion Demo","Pro Gymnast","CreepWars TD","Mimicry","FAST & FURIOUS CROSSROADS: Launch Pack","Nightmare Puppeteer Demo","Midnight's Curse","Anime Feet","The Grand Lord","Super Glitter Rush","League of Angels-Heaven's Fury","Star Renegades","RPG Maker MV - Yokai Parade","Sightbringer","Ultimate Wall Defense Force","HYPERBOLIC Arcade Trading","Food Chain","DPS IDLE","Hoops Madness","Squares Rage Soundtrack","Omina Mortis","Pixel Kunoichi"])