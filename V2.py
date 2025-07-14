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
    lazycfg(star, "/wp-config.php.swp")
    lazycfg(star, "/wp-config.save")
    lazycfg(star, "/wp-config-backup.txt")
    lazycfg(star, "/wp-config.php.orig")
    lazycfg(star, "/wp-config.php.save")
    lazycfg(star, "/wp-config.php.backup")
    lazycfg(star, "/wp-config.php.bk")
    lazycfg(star, "/.env.backup")
    lazycfg(star, "/.env.local")
    lazycfg(star, "/.env.production")
    lazycfg(star, "/.env.dev")
    lazycfg(star, "/.env.staging")
    lazycfg(star, "/.env.development")
    lazycfg(star, "/.env.old")
    lazycfg(star, "/.env.swp")
    lazycfg(star, "/.env.bak")
    lazycfg(star, "/.env~")
    lazycfg(star, "/.env.dist")
    lazycfg(star, "/.env.defaul")
    lazycfg(star, "/credentials.ini")
    lazycfg(star, "/.ftpconfig")
    lazycfg(star, "/configuration.php")
    lazycfg(star, "/configuration.php.bak")
    lazycfg(star, "/configuration.php.old")
    lazycfg(star, "/configuration.php.backup")
    lazycfg(star, "/configuration.php.save")
    lazycfg(star, "/configuration.php~")
    lazycfg(star, "/configuration.php.dist")
    lazycfg(star, "/configuration.php.orig")
    lazycfg(star, "/configuration.php.swp")
    lazycfg(star, "/configuration.php.tmp")
    lazycfg(star, "/configuration.php.bk")
    lazycfg(star, "/configuration.php-backup")
    lazycfg(star, "/configuration.php.bak1")
    lazycfg(star, "/configuration.php.bak2")
    lazycfg(star, "/configuration.php.back")
    lazycfg(star, "/configuration.php.old1")
    lazycfg(star, "/configuration.php.old2")
    lazycfg(star, "/configuration.php.1")
    lazycfg(star, "/configuration.php.2")
    lazycfg(star, "/configuration.txt")
    lazycfg(star, "/configuration.inc.php")
    lazycfg(star, "/configuration.php.inc")
    lazycfg(star, "/configuration.php.original")
    lazycfg(star, "/configuration.php.backup1")
    lazycfg(star, "/configuration.php.backup2")
    lazycfg(star, "/config/configuration.php")
    lazycfg(star, "/includes/configuration.php")
    lazycfg(star, "/administrator/configuration.php")
    lazycfg(star, "/sites/default/settings.php")
    lazycfg(star, "/sites/default/settings.php.bak")
    lazycfg(star, "/sites/default/settings.php.old")
    lazycfg(star, "/sites/default/settings.php.backup")
    lazycfg(star, "/sites/default/settings.php~")
    lazycfg(star, "/sites/default/settings.php.dist")
    lazycfg(star, "/sites/default/settings.php.orig")
    lazycfg(star, "/sites/default/settings.php.swp")
    lazycfg(star, "/sites/default/settings.php.tmp")
    lazycfg(star, "/sites/default/settings.php.save")
    lazycfg(star, "/app/config/parameters.php.bak")
    lazycfg(star, "/app/config/parameters.php.old")
    lazycfg(star, "/app/config/parameters.php.backup")
    lazycfg(star, "/app/config/parameters.php~")
    lazycfg(star, "/app/config/parameters.php.dist")
    lazycfg(star, "/app/config/parameters.php.orig")
    lazycfg(star, "/app/config/parameters.php.save")
    lazycfg(star, "/app/config/parameters.php.tmp")


    


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
