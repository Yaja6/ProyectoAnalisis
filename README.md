# Proyecto de Análisis de Datos

Proceso detallado sobre el uso de scripts

## 1. Cosecha de datos 🚀

### Script 1: Política por Ciudades

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
 
Una vez expplicado el script, se procede a correr el mismo.
Para esto nos ubicamos en la carpeta donde se encuentra el script y abrimos la terminal y ejecutamos el comando: **python Politica1.py**

### Script 2: Política por Provincias

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

### Script 3: Juegos en línea

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


## Transformación de datos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Da un ejemplo
```

## MapReduce 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Dí cómo será ese paso_

```
Da un ejemplo
```

_Y repite_

```
hasta finalizar
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Creación de índices ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

## Creación de mapping 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Logstash ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



