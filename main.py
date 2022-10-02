
import configparser
import json
import tweepy
import requests

import configparser

# import config
config = configparser.ConfigParser()
config.read('config.ini')

# set twitter settings
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

try:
    # twitter
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # votos
    URL = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"
    response = requests.get(url=URL)
    data = response.json()

    # generate message
    total = data["pst"] + "%"

    lulapvap = ""
    bolsonaropvap = ""

    for cand in data["cand"]:
        if cand["nm"] == "LULA":
            lulapvap = cand["pvap"] + "%"
        if cand["nm"] == "JAIR BOLSONARO":
            bolsonaropvap = cand["pvap"] + "%"

    message = "% de votos apurados: " + total + \
        "\nLula: " + lulapvap + \
        "\nBolsonaro: " + bolsonaropvap

    print(message)

    message = input("additional message: ") + "\n\n" + message

except:
    print("Something went wrong")
else:
    api.update_status(status=message)
