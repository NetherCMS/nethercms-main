#----------------------#
#       NETHERCMS      #
#----------------------#
# Created by EletrixTime
# Loader Main Config file

import json
from libs import console
def load_json():
    console.print_info("[JSON] : (RE)Loaded JSON !")
    f = open('config/config.json')

    data = json.load(f)
    f.close()  

    MAINTENANCE = data.get("MAINTENANCE", False)

    # WebServer
    NETHERCMS_PORT = data.get("NETHERCMS_PORT", 80)
    NETHERCMS_ADDRESS = data.get("NETHERCMS_ADDRESS", "0.0.0.0")
    NETHERCMS_SECRETKEY = data.get("NETHERCMS_SECRETKEY", "")

    # Others

    SERVER_TITLE = "Test"
    SERVER_DESCRIPTION = "Lorem Ipsum"
    SERVER_LOGO = "/assets/basic/img/minecraft.png"
    DISCORD_SERVER_LINK = "dsc.gg/eletrixteam"
    SERVER_IP = "0.0.0.0"  # Define your minecraft server IP
    SERVER_PORT = 25005  # Define your minecraft server PORT


    return MAINTENANCE, NETHERCMS_PORT, NETHERCMS_ADDRESS, NETHERCMS_SECRETKEY, SERVER_TITLE, SERVER_DESCRIPTION, SERVER_LOGO, DISCORD_SERVER_LINK, SERVER_IP, SERVER_PORT

MAINTENANCE, NETHERCMS_PORT, NETHERCMS_ADDRESS, NETHERCMS_SECRETKEY, SERVER_TITLE, SERVER_DESCRIPTION, SERVER_LOGO, DISCORD_SERVER_LINK, SERVER_IP, SERVER_PORT = load_json()
