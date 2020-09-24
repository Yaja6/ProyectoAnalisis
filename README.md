# Proyecto de Análisis de Datos

### Link de One Drive con Datasets, Scripts: https://epnecuador-my.sharepoint.com/personal/jonathan_armas_epn_edu_ec/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjonathan_armas_epn_edu_ec%2FDocuments%2FDataAnalisis&originalPath=aHR0cHM6Ly9lcG5lY3VhZG9yLW15LnNoYXJlcG9pbnQuY29tLzpmOi9nL3BlcnNvbmFsL2pvbmF0aGFuX2FybWFzX2Vwbl9lZHVfZWMvRXZuNXhTRXBaU1pLdnd5aExpRjN5dlVCd3p0ZVhCRjBjSFJIRW5XQnp4d0VYQT9ydGltZT1wMUJ1aFlsVDJFZw

**archivos JSON y CSV Finales:** https://mega.nz/file/vBEjTSpZ#iZidFwpiJi9ryKcBk8Eymwy0bNcU2eIo6_yLORXcbPg

Proceso detallado sobre el uso de scripts

## 1. Cosecha de datos 🚀

## Política por Ciudades

La referencia _FUENTE_ son los diferentes scripts usados por el equipo, el proceso detallado es similar en los scripts

### Script 1 (FUENTE 1): Politicaxciudad1.py

```
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

```

**Proceso** 
 En este caso se importaron librerías necesarias como twepy el cual nos permite recolectar los tweets en tiempo  real dentro de scripts de python. 
 Tenemos además las API KEY generadas desde Twitter Development las cuales nos permiten acceder a la API de twitter para extraer los datos.
 A continuación la sección ==couchdb== se utiliza la dirección donde se encuentra corriendo CouchDB, que es la Base de datos NO SQL en la que los datos recopilados se añadirán. Aquí le indicamos que se debe crear una base de datos llamada _politica2_  
 
Para el filtro de twitter usamos el filtro por palabras debido a que nos permite definir exactamente los temas relacionados a la política. Este apartado contiene aproximadamente 100 palabras como filtro, entre ellos:
 * Nombres de candidatos de las ciudades
 * Nombres de Movimientos y Listas candidatas
 * Nombres de las Ciudades 
 
Una vez explicado el script, se procede a correr el mismo.
Para esto nos ubicamos en la carpeta donde se encuentra el script y abrimos la terminal y ejecutamos el comando: **python Politica1.py**

### Script 2 (FUENTE 2): Políticaxciudad2.py

```
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
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('presidenciales_nacionales')
except:
    db = server['presidenciales_nacionales']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[-79.95912,-2.287573,-79.856351,-2.053362]) 
twitterStream.filter(track=["Andrés Arauz","Lucio Gutiérrez","David Norero","Gerson Almeida","Martha Villafuerte","Cristina Reyes","Diego Salgado","Isidro Romero","Sofía Merino", "Esteban Quirola", "Juan Carlos Machuca","Miguel Salem Kronfle","Gustavo Bucaram Ortiz", "Fabricio Correa","Marcia Yazbell","Xavier Hervas","María Sara Jijón", "Pedro José Freile","Byron Solís", "Yaku Pérez","Washington Pesántez","José Díaz","Gustavo Larrea","Alexandra Peralta","Guillermo Lasso","Alfredo Borrero", "Guillermo Celi","Verónica Sevilla","Juan Fernando Velasco","Ana María Pesantes", "Paúl Carrasco","Frank Vargas Anda", "Ximena Peña","Patricio Barriga","César Montúfar","Julio Villacreses"])
```
## Política por Provincias

### Script 3 (FUENTE 1): Políticaxprovincia1.py

```
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
    db = server.create('porprovincias')
except:
    db = server['porprovincias']

'''===============LISTAS, NOMBRES Y REPRESENTANTES=============='''
twitterStream.filter(track=['Movimiento Autonómico Regional','Teresa Rodas','José Sánchez','Carolina Álvarez','Arlington Márquez','Alba Bravo','José Felipe Martínez','Génesis Vaca','Mauricio Ortiz',' Rosario Sigüenza','Jorge Palacios','Abg. Luis Alberto Morocho García',' Cristina Pérez Córdova','José Granda Palomino','Marcela Valencia Rentería',' Fernando Delgado Gordillo','Jaqueline Anzóategui Peláez','Flavio Corozo Castro',' María Cristina Farez','Bryan Erazo Mora','Zulema Veintimilla Castillo','Movimiento Unión Ecuatoriana','Betzabeth Liliana Herrera Chalán','Ángel García Ramón','Irene Victoria Valdivieso Montero','Jorge Vaca Jervez','María Matilde Suriaga Vicente','Palmer Delgado Echeverría', 'Digna Emedica Granda Castro','Ayrton Joao Almache Izquierdo', 'Laura Mariela Tinitana Aguilar', 'Miguel Ángel Vicente Gaona','Movimiento CREO','Francisco Vera Domínguez', 'Mirtha Aristeguieta Logroño','Vicente Guzmán Barbotó',' Rosa Román Zambrano','Washington Romero Añazco',  'Evelyn Escaleras Ríos','José Quimí Arias','Lidia Arias Torres','Santiago Romero Granda','Mirelis Tituana Asanza', 'Movimiento unidad popular','Jessica González Cabrera','Ulbio Torres','Lady León','Galo Jiménez',' María Isabel Farez','Vicente Naranjo',' Carmen Guerrero','Jonthan Paladines','Maritza Herrera','Bolívar Bravo','Movimiento Sur Unido Regional', 'Abg. Galo Suquilanda Jara', 'Abg. Lucía Ramos', 'Lucio Minchala Calderón', 'Silvana Maldonado Peláez','Carlos Guzmán Solano','candidatos de Avanza', 'Lista 8', 'Danny Nieto Macas',' Nathaly Teresa Puertas Paladines', 'Wilson Merino Sánchez', 'Analy Estefanía Carbache Hernández', 'José Ayala Chamba', 'Francy Aracely González Morales', 'Gonzalo Arturo Ortega Pereira', 'Karen Estefanía Beltrán Apolo',' Darwin Samuel Cárdenas Robles','Kerly Taimy Cueva Celi','movimiento Democracía Sí', 'Lista 20','Elizabeth Falconí Niemes', 'Rolando Fernando Ayoví Rodríguez',' Paulette Pulla Carrión', 'Luis Mendía Armijos', 'Julia María Rentería German','Jefferson Ruilova Niemes', 'Alejandra León Ordóñez', 'Segundo Daniel Jumbo Ramírez', 'Normandy Feliza Ayoví Rodríguez','Cristian Ardila Rivera','IZQUIERDA DEMOCRÁTICA','Johanna Nicole Moreira Córdova', 'Jesús Alberto Motoche Apolo', 'Valeria Estefanía Elizalde Maza', 'Jaime Hurtado Gándara Pizarro', 'Karen Espinoza Castro','Joseph Geovanny Villacreses Quevedo', 'Jenny Requene Bravo', 'Álvaro Gustavo Ulloa Jaramillo', 'Monica Nathaly Cobos Daúl','Mario Eduardo Narváez','movimiento Concertación', 'Lista 51','Verónica Arreaga',' Hugo Juca', 'Mireya León', 'José Ochoa',' Ana Contreras','Marco Torres', 'Lorena Orellana', 'David Ordóñez', 'Bélgica Jiménez', 'Leonardo Castro', 'Miguel Ángel Garzón Villacrés', 'Adriana Lisbeth Rivilla Ortega', 'Roger Max Medina Espinar', 'María García Domínguez', 'Gerardo Acuña Jara', 'Sisy Alison Armijos Bustamante', 'Gilbert Adrián Pontón Jiménez', 'Laura Yolanda Naula Rodríguez',' Marlos Onassis Reyes Chamba', 'Ana María Matute Cedeño','Movimiento Ecuatoriano Unido','Susana Estefanía Solórzano Astudillo', 'Dorian Damián Flores Aguilera', 'Jazmín Cecibel Cheme Fernández', 'Luis Alberto Leiva Romero','María Fernanda Carrión Limones','Emilio Efrén Cruz Cazares', 'Vanessa Portilla Tituana', 'Juan Carlos Flor Girón', 'Angie Mishell Yaguachi Camacho', 'Jimmy Alexander Añazco','PARTIDO SOCIALISTA', 'lista 17 ', 'César Valarezo Romero', 'Leysi López', 'Eudaldo Jadán Veriñaz', 'Karla Suárez','Fernando Quirola Anzoátegui' ,'Carlos Falquez Batallas','alterna Karen Noblecilla','Rosa María Loaiza', 'Enrique Orellana Cueva','Movimiento Alianza País', 'Lista 35', 'Rosa Orellana','Jorge Paredes', 'Cristhian Dumas','alterna Irina Alvarado','Movimiento de Unidad Plurinacional Pachakutik', 'lista 18', 'Darwin Pereira Chamba', 'María Leonila Armijos Yunga', 'Antonio Geovanny Almache Guarderas', 'Nayelhi Mayte Chuchuca Marín', 'Oscar Aldo Sánchez Romero', 'María Carreño Chamba',' Alejandro Fabricio Romero Espinoza', 'Marlín Anabel Avelino Granda', 'Petter Andrés Armijos Yaure','Maritza Amaya Torres','Movimiento SIII', 'Lista 88', 'Aldo Favio Romazzo Guzmán', 'Grace Amanda Encalda Sánchez', 'Mario Farah Rodríguez', 'Dahara Balcázar Robles','Cristhian Omar Chalaco Celi','Margarita Aracely Ortíz Maza', 'Antony Agenor León Espinoza', 'Karin Ernestina Ollague Guzmán', 'Juan Francisco Ramírez Loayza','Roxana Nuñez Rodríguez','Partido Sociedad Patriótica', 'Marco Antonio Gallardo Suárez', 'Carolina Elizabeth Vivanco Cueva',' Carlos Alfredo Loja Sagbay', 'Michelli Zambrano Cruz', 'Rubén Eudofilio Zhunio Malla', 'María José Lomás Cerezo', 'Segundo Manuel Balcázar Naranjo', 'María José Díaz Ludeña', 'Erick Mauricio Molina Oviedo', 'Indira Priscilla Sacco Freire','Centro Democrático','Lista 1', 'UNES', 'Carlos Víctor Zambrano Landín', 'María Fernanda Astudillo Barrezueta', 'Fernando Javier Guamán Andrade', 'Gloria Esterfilia Espinoza Vásquez' , 'Giancarlo Mora Peñarreta', 'Sara Noemí Cabrera Chacón', 'Jorge Ariel Quevedo Pinta', 'Diana Verónica Chuquisala Pinza', 'Kevin Samuel Jiménez Barreto','Ariana de Lourdes Pineda Encalada','Jimmy Candell','Lista 63', 'Winston Ajoy','Eduardo Rugel','Verónica Palma','Bolívar Fajardo','Abrahan Segarra','Luis Hemeregildo'])
```

 **Proceso** 
 Como se puede ver, hemos usado el mismo script de python para recolectar tweets sobre este tema. Solo cambian algunas variantes
La sección ==couchdb== se utiliza la dirección donde se encuentra corriendo CouchDB, que es la Base de datos NO SQL en la que los datos recopilados se añadirán. Aquí le indicamos que se debe crear una base de datos llamada _porprovincias_  
 
Para el filtro de twitter usamos el filtro por palabras debido a que nos permite definir exactamente los temas relacionados a la política. Este apartado contiene aproximadamente 300 palabras como filtro, entre ellos:
 * Nombres de candidatos por provincias
 * Nombres de Movimientos y Listas candidatas
 * Nombres de las provincias
 
Una vez expplicado el script, se procede a correr el mismo.
Para esto nos ubicamos en la carpeta donde se encuentra el script y abrimos la terminal y ejecutamos el comando: **python Politica2.py**



## JUEGOS EN LÍNEA

Primero se detalla el script juegos.py usado para el webscrapping dentro de la página Steam

### Script 4: juegos.py

```
import scrapy
from scrapy import Spider
from scrapy import Selector
from Steam.items import SteamItem
from scrapy.spiders import CrawlSpider
    
class JuegosSpider(CrawlSpider):
    name = 'juegos'
    allowed_domains = ['steampowered.com']
    start_urls = [
    "https://store.steampowered.com/search/?sort_by=Released_DESC&sort_order=DESC&page=%d" % i for i in range(1,2845)]


    def parse(self, response):
    	games=Selector(response).xpath('//*[@id="search_resultsRows"]/a')
    	for game in games:
    		item=SteamItem()
    		item['nombre']=game.xpath('div[2]/div[1]/span/text()').extract()[0]
    		item['link']=game.xpath('@href').extract()[0]
    		item['fecha']=game.xpath('div[2]/div[2]/text()').extract()[0]
    		item['precio']=game.xpath('div[2]/div[4]/div[2]/text()').extract()[0]
    		yield item
```
**Proceso**
A continuación usamos la plataforma de venta de videojuegos  **Steam** 
En esta página se realiza webscrapping junto con el framework scrapy para lo que luego de tener descargado, lo importamos dentro del script.
El sitio cuenta con 2845 páginas por lo que se utilizó un for dentro de la URL y así raspar todo el contenido. 
```
    start_urls = [
    "https://store.steampowered.com/search/?sort_by=Released_DESC&sort_order=DESC&page=%d" % i for i in range(1,2845)]
```
La función Selector nos permite obtener los XPath de los componentes dentro de Steam
```
games=Selector(response).xpath('//*[@id="search_resultsRows"]/a')
```
Donde: 

**[@id="search_resultsRows"]/a:** Es el componente principal donde se encuentran los elementos rastrear.
**item['nombre']=game.xpath('div[2]/div[1]/span/text()').extract()[0]:** Indica que se extraerá el texto de la etiqueta span
**item['link']=game.xpath('@href').extract()[0]:** Se extrae los links dentro de las etiquetas _a_
**item['fecha']=game.xpath('div[2]/div[2]/text()').extract()[0]:** Se extrae las fechas dentro de la etiqueta div
**item['precio']=game.xpath('div[2]/div[4]/div[2]/text()').extract()[0]:** Por ultimo se extraen los precios de los videojuegos que se encuentra en la etiqueta div


**A continuación, se extrae datos de twitter relacionados con los videojuegos encontrados dentro de Steam

## Script 5 (FUENTE 1): Juegos1.py

```
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
```

## Script 5 (FUENTE 2): Juegos2.py

```
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
```
## Noticia evento mundial: COVID

En este caso se hizo uso de un solo script para extraer los datos
## Script 6 : covid1.py

```
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
    db = server.create('covid')
except:
    db = server['covid']

'''===============LISTAS, NOMBRES Y REPRESENTANTES=============='''
#twitterStream.filter(locations=[-79.95912,-2.287573,-79.856351,-2.053362]) 
twitterStream.filter(track=["covid-19","COVID","Cuarentena por covid","Latinoamérica covid-19","Coronavirus"])
```

## Tema libre: Salida de Messi de Barcelona

En este caso se hizo uso de un solo script para extraer los datos

```
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
```

## Script 7 : messi1.py


## Transformación de datos 📋

En cuanto a la tranformación de datos de la base de datos CouchDB, se usaron los siguientes comandos:

## Se tomó los datos de la base de datos _politica2_ que hace referencia a los tweets tomando por ciudades. Se los exporta en archivo JSON

```
curl -X GET http://admin:couchy@127.0.0.1:5984/politica2/_all_docs?include_docs=true > C:/Users/politicaCiudades.json
```

## Se tomó los datos de la base de datos _porprovincias_ que hace referencia a los tweets tomando por provincias. Se los exporta en archivo JSON

```
curl -X GET http://admin:couchy@127.0.0.1:5984/porprovincias/_all_docs?include_docs=true > C:/Users/politicaProvincias.json
```

## Se tomó los datos de la base de datos _covid_ que hace referencia a los tweets tomados acerca de la pandemia del Coronavirus. Se los exporta en archivo JSON

```
curl -X GET http://admin:couchy@127.0.0.1:5984/covid/_all_docs?include_docs=true > C:/Users/covid.json
```

## Se tomó los datos de la base de datos _juegos_ que hace referencia a los tweets tomandos por nombres de juegos encontrados desde el webscrapping. Se los exporta en archivo CSV para su debido análisis

```
curl -X GET http://admin:couchy@127.0.0.1:5984/juegos/_all_docs?include_docs=true > C:/Users/juegosOnline.CSV
```

## Se tomó los datos de la base de datos _messi_ que hace referencia a los tweets sobre la salida del jugador Leo Messi del Barcelona. Se los exporta en archivo JSON

```
curl -X GET http://admin:couchy@127.0.0.1:5984/messi/_all_docs?include_docs=true > C:/Users/messi.json
```

## A continuación, para pasar los datos del webscrapping realizado de Steam y el Dataset sobre COVID a la base de datos MYSQL se sigue el siguiente proceso:

## Pasar datos de Dataset tomando de opendataset hacia MYSQL:

**1. Creación de tablas dentro de la base de datos covid
```
use covid;
CREATE TABLE canada (
	case_id int,
    province_death_id VARCHAR(45),
    age VARCHAR(45),
    sex VARCHAR(20),
    health_region VARCHAR(45),
    province VARCHAR(45),
    country VARCHAR(45),
    date_death_report date,
    
    
    constraint canadapk PRIMARY KEY (case_id)
);
CREATE TABLE paises_covid (
Id int,	
País varchar(45),	
Frecuencia	varchar(45),
Fecha_de_Inicio	varchar(20),
Fecha_Final varchar (20),	
Año	varchar(4),
Mes	int,
Semana	varchar(45),
Muertes	int,
Muertes_Esperadas int,	
Exceso_de_Muertes	int,
Linea_Base varchar(45),
    
    constraint paisespk PRIMARY KEY (Id)
);
```

**2. Uso de comando para importar los datos del archivo Libro1.CSV hacia la base de datos creada

```
load data local infile 'C:/Users/l_jan/Documents/Desarrollo de Software/Cuarto Semestre/Analisis de Datos/Proyecto Final/Covid Dataset/Datos para Power BI/Libro1.csv' into table paises_covid fields terminated by ';' lines terminated by '\r\n';
```
## MapReduce 🔧

El MapReduce fue realizado con las herramientas Kibana y PowerBI por lo que se encuentra en la documentación.

## Mapping ⚙️

El mapping dentro de cada índice fueron los siguientes:

Dentro de los índices: messiBarcelona, politicaxprivincia se usa el script **mapping.conf**

```
{
    "mappings": {
        "properties": {
          "created_at": {
            "type": "date",
            "format": "EE MMM d HH:mm:ss Z yyyy||dd/MM/yyyy||dd-MM-yyyy||date_optional_time"
          },
          "location": {
            "type": "geo_point"
          }
}
```

## Creación de índices (Logstash y Elasticsearch) ⚙️

Una vez extraídos los datos, se procede a pasarlos a Elasticsearch para posterior a ello crear visualizaciones.
Para pasar estos datos se hace uso de la herramietna logstash con los siguientes scripts:

**Script 1: ciudades.conf** 

Se creará un índice dentro de elasticsearch llamado _datos_ el cual contendrá los documentos de la base de datos _politica2_  de couchDB

```
input{
couchdb_changes{
db=>"poltica2"
} }
output {
 elasticsearch {
 index => "datos"
 
 } 
}
```
**Script 1: politica.conf** 

Se creará un índice dentro de elasticsearch llamado _politicaporprovincia_ el cual contendrá los documentos de la base de datos _porprovincias_ de couchDB

```
input{
couchdb_changes{
db=>"porprovincias"
} }
output {
 elasticsearch {
 index => "politicaxprovincia"
 
 } 
}
```
**Script 1: messi.conf** 

Se creará un índice dentro de elasticsearch llamado _messibarcelona_ el cual contendrá los documentos de la base de datos _messi_

```
input{
couchdb_changes{
db=>"messi"
} }
output {
 elasticsearch {
 index => "jmessibarcelona"
 
 } 
}
```

## Autores ✒️

* **Alejandro Armas** 
* **Yajaira Cuatis** 
* **Christian Llumquinga** 





