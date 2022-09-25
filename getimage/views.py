from django.shortcuts import render
import pandas as pd
from lodstorage.sparql import SPARQL
from lodstorage.csv import CSV
import ssl
import json
import math
import random
from urllib.error import HTTPError
from urllib.request import urlopen
from alive_progress import alive_bar
from time import sleep

ssl._create_default_https_context = ssl._create_unverified_context

df_sparql = pd.read_csv("manifestenDMG.csv")
iiifmanifesten = df_sparql['1'].tolist()
print(iiifmanifesten[0])

def image(request):
    x = random.randint(0, len(iiifmanifesten))
    manifest = iiifmanifesten[x]

    try:
        response = urlopen(manifest)
    except ValueError:
        return image(request)
    except HTTPError:
        return image(request)
    else:
        print(response)
        data_json = json.loads(response.read())
        print(data_json)
        iiif_manifest = data_json["sequences"][0]['canvases'][0]["images"][0]["resource"]["@id"]
        print(iiif_manifest)
        afbeelding = iiif_manifest.replace("full/full/0/default.jpg","full/1000,/0/default.jpg")
        label = data_json["label"]['@value']
        #beschrijving = data_json["description"]
        manifestje = data_json["@id"]
        rechtentype = data_json["sequences"][0]['canvases'][0]["images"][0]["license"]
        attributie = data_json["sequences"][0]['canvases'][0]["images"][0]["attribution"]
        objectnummer = manifestje.rpartition('/')[2]
        webplatform = "https://data.collectie.gent/entity/" + objectnummer
        print(webplatform)
        print(label)
        if 'stam' in manifest:
            instelling = 'STAM'
        elif 'hva' in manifest:
            instelling = 'Huis van Alijn'
        elif 'dmg' in manifest:
            instelling = 'Design Museum Gent'
        elif 'industriemuseum' in manifest:
            instelling = 'Industriemuseum'
        else:
            instelling = 'Archief Gent'
        print(instelling)
        return render(request, 'image.html', {'iiif_manifest': afbeelding, 'instelling': instelling, 'label': label, 'manifest': manifestje, 'webplatform': webplatform, 'rechtentype': rechtentype, 'attributie': attributie})










##wishlist: filter de list > enkel DMGs eruit halen (of dat pas bij ophalen niveau doen?
##mooiere layout en meer info > link webplatform mogelijk te halen uit manifest, alles na manifest/
## zo erbij zetten, direct ook met rechteninfo bij
