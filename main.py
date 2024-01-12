
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
    from flask import Flask , send_file , render_template , redirect , session , request , json , abort
    from datetime import datetime
    import atexit 
    import threading
    
    import os
except Exception as e:
    print("Critical librarie(s) import failed error :")
    print(e)

# Config Import
try:
    from config import Loader_main_config as main_config
    from libs import jsonchecker

except Exception as e:
    print("Critical configuration files import failed error :")
    print(e)

def load_users():
    with open("data/users.json", 'r') as file:
        return json.load(file)

def save_users(users):
    with open("data/users.json", 'w') as file:
        json.dump(users, file, indent=2) 
app = Flask(__name__)

app.secret_key = main_config.NETHERCMS_SECRETKEY


@app.route('/')
def index():
    if main_config.MAINTENANCE:
        return render_template("/error/maintenance.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK)
    else:  
        return render_template("index.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK,server_description=main_config.SERVER_DESCRIPTION,MC_SERVER_IP=main_config.SERVER_IP,MC_SERVER_PORT=main_config.SERVER_PORT)
    
@app.route('/assets/<path:filename>')
def get_asset(filename):
    file_path = os.path.join("assets", filename)
    if os.path.exists(file_path) and not os.path.isdir(file_path):
        return send_file(file_path)
    else:
        return redirect("/404")
@app.route('/others/requirelogin')
def others_login_require():
    if 'username' in session:
        return render_template("/others/requirelogin.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK)
    else:
        return redirect("/auth/login") 
# AUTHENFICATION PART
@app.route('/auth/login', methods=['GET', 'POST'])
def auth_login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("login")
        users = load_users()

        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect('/')
        else:
            return("Invalid credientials")

    return render_template("/auth/login.html", title=main_config.SERVER_TITLE, datetime_render=str(datetime.now()),
                           logo_path=main_config.SERVER_LOGO, discord_link=main_config.DISCORD_SERVER_LINK,
                           server_description=main_config.SERVER_DESCRIPTION, MC_SERVER_IP=main_config.SERVER_IP,
                           MC_SERVER_PORT=main_config.SERVER_PORT)
@app.route('/auth/logout')
def auth_logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect('/')
    else:
        return redirect("/others/requirelogin")
@app.route('/auth/accountmenu')
def auth_accountmenu():
    if 'username' in session:
        return render_template("/auth/accountmenu.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK)
    else:
        return redirect("/auth/login")
    
@app.route('/auth/accountmanage')
def auth_accountmanage():
    if 'username' in session:
        return render_template("/auth/accountmanage/main.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK)
    else:
        return redirect("/auth/login")
    
@app.route('/auth/register', methods=['GET', 'POST'])
def auth_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        permissions = 1
        mcuuid = 0
        
        users = load_users()

        if username not in users:
            console.print_info(f"[NetherCMS/Accounts/Register] : New user : username : {username}")
            users[username] = {
                'password': password,
                'email': email,
                'permissions': permissions,
                'mcuuid': mcuuid,
            
            }

            save_users(users)
            session['username'] = username
            
            return render_template("others/complete.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK)

    return render_template('auth/register.html',title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK,server_description=main_config.SERVER_DESCRIPTION,MC_SERVER_IP=main_config.SERVER_IP,MC_SERVER_PORT=main_config.SERVER_PORT)

# Admin Panel :

@app.route('/admin')
def admin_main():
    if 'username' in session:
        username = session['username']
        users = load_users()

        if username in users and 'permissions' in users[username] and users[username]['permissions'] == 2:
            
            return render_template("/admin/main.html", title=main_config.SERVER_TITLE,
                                   datetime_render=str(datetime.now()), logo_path=main_config.SERVER_LOGO,
                                   discord_link=main_config.DISCORD_SERVER_LINK)
        else:
            
            abort(404)

    else:
        return redirect('/auth/login')

# Handling error :

@app.errorhandler(404) 
def not_found(e): 
    return render_template("error/404.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK) 
@app.errorhandler(500) 
def server_error(e): 
    return render_template("error/500.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK,errortext=e) 
@app.errorhandler(403) 
def notauthorized(): 
    return render_template("error/403.html",title=main_config.SERVER_TITLE,datetime_render=str(datetime.now()),logo_path=main_config.SERVER_LOGO,discord_link=main_config.DISCORD_SERVER_LINK) 

# API 

@app.route("/api/userlink/<id>")
def api_userlink():
    return("soon")
    

try:
    if __name__ == '__main__':
        def startwebserver():
            console.print_info("[ThreadManager] : Web server started !")
            app.run(debug=False, host=main_config.NETHERCMS_ADDRESS, port=main_config.NETHERCMS_PORT)
        atexit.register(print, "Exiting...")
        #Starting JSON RELOADING
        threadmanager_jsonreloadchecker = threading.Thread(target=jsonchecker.checkreload, args=("config/config.json",))
        threadmanager_jsonreloadchecker.daemon = True
        threadmanager_jsonreloadchecker.start()
        
        #Starting web server
        threadmanager_webserver = threading.Thread(target=startwebserver())
        threadmanager_webserver.daemon = True
        threadmanager_webserver.start()

except Exception as e:
    console.print_error("Failed to init webserver error :")
    console.print_error(e)
    exit(0)
