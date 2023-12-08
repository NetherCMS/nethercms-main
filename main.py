
NETHERCMS_VERSION = "0.1"

#----------------------#
#       NETHERCMS      #
#----------------------#
# Created by EletrixTime
# Main file

print(f"NetherCMS @ V{NETHERCMS_VERSION}")

# IMPORTANT library import :

try:
    from libs import console
    from libs import telemetry
    from flask import Flask , send_file , render_template , redirect
    from datetime import datetime

    import os
except Exception as e:
    print("Critical librarie(s) import failed error :")
    print(e)

# Config Import
try:
    from config import main_config
except Exception as e:
    print("Critical configuration files import failed error :")
    print(e)

    
app = Flask(__name__)
@app.route('/')
def index():
    if main_config.MAINTENANCE:
        return render_template("/error/maintenance.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK)
    else:  
        return render_template("index.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK,server_description=main_config.SERVER_DESCRIPTION,MC_SERVER_IP=main_config.SERVER_IP,MC_SERVER_PORT=main_config.SERVER_PORT)

@app.errorhandler(404) 
def not_found(e): 
    return render_template("error/404.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK) 

@app.route('/assets/<path:filename>')
def get_asset(filename):
    file_path = os.path.join("assets", filename)
    if os.path.exists(file_path) and not os.path.isdir(file_path):
        return send_file(file_path)
    else:
        return redirect("/404")
try:
    if __name__ == '__main__':
        app.run(debug=True,host=main_config.NETHERCMS_ADDRESS,port=main_config.NETHERCMS_PORT)
except Exception as e:
    console.alert("Failed to init webserver error :")
    console.alert(e)
    exit(0)