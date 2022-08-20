#/root/geowawa/bin/python
import googlemaps
import json
gmaps = googlemaps.Client(key='AIzaSyCz5vsQW9b60WheYfW8OBD5VQaHYObFGXM')
# Implementando resgate de coordenadas com base no endereco
def resgataCoordenadas(q):
    geocode_result = gmaps.geocode(q)[0]
    print(geocode_result)
   
    if geocode_result['geometry']['location']:
        print(geocode_result['geometry']['location']['lat'])
        return {"lat": geocode_result['geometry']['location']['lat'],"lng": geocode_result['geometry']['location']['lng']}
    else:
        return false


# Criar funcao que le cada linha de um arquivo
def leArquivo(faile):
    f = open(faile, 'r')
    escreveArquivo(f) 
        



def escreveArquivo(f):
    str = ''
    id=0
    str += defineCabecalho()
    for line in f:
        nome,crm,telefone,bairro,endereco,numero,estado,cidade = line.split(",")
        id+=1
        str += '{\n'
        geo = resgataCoordenadas(','.join([endereco,cidade,estado]))
        if geo:
            lat = geo['lat'] 
            lng = geo['lng']

        str+= '"geometry": {\n'
        str+= '"type": "Point",\n'
        str+= '"coordinates": [\n'
        str+= '{0},{1}\n'.format(lng,lat)
        str+= ']\n'
        str+= '},\n'
        str+= '"type": "Feature",\n'
        str+= '"properties": {\n'
        str+= '"nome": "{0}",\n'.format(nome)
	str+= '"crm": "{0}",\n'.format(crm)
        str+= '"telefone": "{0}",\n'.format(telefone)
        str+= '"bairro": "{0}",\n'.format(bairro)
        str+= '"rua": "{0}",\n'.format(endereco)
        str+= '"numero": "{0}",\n'.format(numero)
        str+= '"estado": "{0}",\n'.format(estado)
        str+= '"municipio": "{0}"\n'.format(cidade.rstrip())
        str+= '},\n'
        str+= '"id": {0}\n'.format(id)
        str+= '},\n'
    str += defineRodape()
    print(str)
    m = open('../www/mundo.js','w')
    m.write(str)

def defineCabecalho():
    str = 'var pontos = {\n'
    str += '"type": "FeatureCollection",\n'
    str += '"features": [\n'
    return str


def defineRodape():
    str  = ']\n'
    str += '};'
	
	#string number.
	
    return str
leArquivo('teste.csv')
