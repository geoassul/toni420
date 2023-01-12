import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re

clave_api = False
# Si tienes una clave API de Google Places, ingresala aquÃ­
# clave_api = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if clave_api is False:
    clave_api = 42
    url_de_servicio = 'http://py4e-data.dr-chuck.net/json?'
else :
    url_de_servicio = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    direccion = input('Ingresa una ubicaciÃ³n: ')
    if len(direccion) < 1: break

    parms = dict()
    parms['address'] = direccion
    if clave_api is not False: parms['key'] = clave_api
    url = url_de_servicio + urllib.parse.urlencode(parms)

    print('Recuperando', url)
    uh = urllib.request.urlopen(url, context=ctx)
    datos = uh.read().decode()
    
    print('Recuperados', len(datos), 'caracteres')

    try:
        js = json.loads(datos)
    except:
        js = None
        
    try:        
        if len(js['results'][0]['address_components'][2]['short_name']) == 2:
            print('ok')
        else:
            print('bro')
    except:
            print('bro')
            
    for dic in js['results'][0]['address_components']:
        if len(dic['short_name']) == 2:
            print(dic['short_name']an)
            
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Error al Recuperar ====')
        #print(datos)
        continue

    #anprint(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)