import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

###API ########################
ckey = "CuIFG1DblkEC36JFzJByX5mi7"
csecret = "Nc8sgHQ1n2Fb1qpHma9LudER1wOELLP4tNzzpz6YAIQnmRF9Qh"
atoken = "1204786641635827712-XXmfW6V9O2i6CVS4X1SykT5Tp7GpjY"
asecret = "S76F2rIurjJnpwctfYQ9a2tprXp7pP8UNI8lYlfWSuqKW"
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
    db = server.create('messi')
except:
    db = server['messi']
'''===============LISTAS, NOMBRES Y REPRESENTANTES=============='''
twitterStream.filter(track=["lionel messi","messi","barcelona FC","barca"])