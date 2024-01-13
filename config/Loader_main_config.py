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
    NETHERCMS_ADDRESS = data.get("NETHERCMS_ADDRESS")
    NETHERCMS_SECRETKEY = data.get("NETHERCMS_SECRETKEY")

    # Others

    SERVER_TITLE = data.get("SERVER_TITLE")
    SERVER_DESCRIPTION = data.get("SERVER_DESCRIPTION")
    SERVER_LOGO = data.get("SERVER_LOGO")
    DISCORD_SERVER_LINK = data.get("DISCORD_SERVER_LINK")
    SERVER_IP = data.get("SERVER_IP")
    SERVER_PORT = data.get("SERVER_PORT")

    
    return MAINTENANCE, NETHERCMS_PORT, NETHERCMS_ADDRESS, NETHERCMS_SECRETKEY, SERVER_TITLE, SERVER_DESCRIPTION, SERVER_LOGO, DISCORD_SERVER_LINK, SERVER_IP, SERVER_PORT

MAINTENANCE, NETHERCMS_PORT, NETHERCMS_ADDRESS, NETHERCMS_SECRETKEY, SERVER_TITLE, SERVER_DESCRIPTION, SERVER_LOGO, DISCORD_SERVER_LINK, SERVER_IP, SERVER_PORT = load_json()
