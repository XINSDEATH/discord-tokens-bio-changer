import time
from colorama import Fore
import requests

def get_all_tokens(filename):
    all_tokens = []
    with open(filename, 'r') as f:
            t = f.read()
            tt = t.splitlines()

            for i in tt:
                all_tokens.append(i)

    return all_tokens

def changebio(bio):
  tokens = get_all_tokens(f'tokens.txt')
  for token in tokens:
    start_time = time.time()
    if baka == baka:
        baka = True
    r = requests.Session()
    # gets cookies (100% delicious 😋)
    url = "https://discord.com/api/v9/experiments"
    k = r.get(url)
    
    # sends sex request
    url = "https://canary.discord.com/api/v9/users/%40me/profile"
    headers = {"accept": "/",
  
    "authorization": token,
  
    }
    body = {"bio": bio}
    
    
    r.patch(url, headers=headers, json=body)
    print(Fore.GREEN,f"[-] {token} [-] changed bio to {bio} - [-] {(time.time() - start_time)}s")


print('''XIN BIO CHANGER''')

bio = input("input new bio -> ")

changebio(bio)