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