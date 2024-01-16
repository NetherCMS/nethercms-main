from libs import console
import os
import json
import time
from datetime import datetime
from config import Loader_main_config

def checkreload(file_path):
    try: 
        console.print_info("[ThreadManager] >> CheckReload Thread is activated !")

        last_modified = os.path.getmtime(file_path)

        while True:
            time.sleep(2)
            current_modified = os.path.getmtime(file_path)

            if current_modified != last_modified:
                console.print_warning("[JsonReloading] : JSON live time reloading is currently unstable !")
                Loader_main_config.MAINTENANCE, Loader_main_config.NETHERCMS_PORT, Loader_main_config.NETHERCMS_ADDRESS, Loader_main_config.NETHERCMS_SECRETKEY, Loader_main_config.SERVER_TITLE, Loader_main_config.SERVER_DESCRIPTION, Loader_main_config.SERVER_LOGO, Loader_main_config.DISCORD_SERVER_LINK, Loader_main_config.SERVER_IP, Loader_main_config.SERVER_PORT = Loader_main_config.load_json()
                last_modified = current_modified
    except Exception as e:
        console.print_error("[ThreadManager] >> An error occurred in CheckReload...")
        console.print_error(e)