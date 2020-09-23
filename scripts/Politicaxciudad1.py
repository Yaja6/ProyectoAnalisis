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
    db = server.create('politica2')
except:
    db = server['politica2']
'''===============LISTAS, NOMBRES Y REPRESENTANTES=============='''
twitterStream.filter(track=['Quito candidatos','Ecuador','Machala','Portoviejo','Esmeraldas','Ciudad de Milagro','Babahoyo','Latacunga','Guillermo Alberto Santiago Lasso Mendoza','Fabricio Correa Delgado','Wilson Gustavo Larrea Cabrera','Lucio Gutiérrez Borbúa','Andrés David Aráuz Galarza','Guillermo Alejandro Celi Santos','Yaku Sacha Pérez Guartambel','Cesar Montúfar Mancheno','Isidro Romero Carbo','Carlos Gerson Almedia Espinoza','Ximena Peña Pacheco','Paúl Ernesto Carrasco Carpio','Esteban Leopoldo Quirola Bustos','Miguel Salem Kronfle','Cristina Reyes','Xavier Hervas','Pedro José Freile','Juan Fernando Velasco Torres','Washington Arturo Pesántez Muñoz','Unión Ecuatoriana','Pachakutik','Partido Social Patriota','Consejo Nacional Electoral Ecuador','Centro democrático','Pierina Correa Delgado','Geovanni Atarihuana','Unión Popular','Ecuador unido','Rocío Juca', 'Partido Social Cristiano','Henry Kronfle', 'Javier Ortiz', 'Libertad es Pueblo','Fernando Balda','Fuerza EC','Abdalá Bucaram Ortiz', 'Democracia Sí','Xavier Zavala Egas','César Monge','Alianza PAIS',  'César Litardo','Fernando Villavicencio'])

'''===============GEOLOCALIZACIÓN: QUITO=============='''
#twitterStream.filter(locations=[-78.619545,-0.365889,-78.441315,-0.047208])