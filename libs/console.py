import datetime

def info(text):
    formatted_text = f"\033[91m[INFO] \033[0m : {text} "
    print(f"[\033{datetime.datetime.now()} \033[0m] {formatted_text}")

def alert(text):
    formatted_text = f"\033[91m[ALERT] \033[0m : {text} "
    print(f"[\033{datetime.datetime.now()} \033[0m] {formatted_text}")
