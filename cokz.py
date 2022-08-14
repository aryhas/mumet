import requests, re, random, time, sys, json, os
from bs4 import BeautifulSoup as par
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
warna = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
#-------- LOADING ANIMASI -----------
class Login:

    def __init__(self):
        prints(Panel(f"""[{warna}01[/]]. Login menggunakan cookie
[{warna}02[/]]. Cookie gratis (gak semuanya valid)
[{warna}03[/]]. Cara mendapatkan cookie"""))
        p = input(f"  [{K}?{N}] pilih : ")
        if p =="":
           print(f"\n  [{M}!{N}] Jangan kosong");time.sleep(3);Login() 
        elif p in["1","01"]:
            self.login_cookie()
        elif p in["2","02"]:
            self.cok()
        elif p in["3","03"]:
            exit(" sabar lagi bikin vidionya")
        else:
           print(f"\n  [{M}!{N}] input yang benar.");time.sleep(3);Login()

    def loading(self):
        animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
        print("")
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write(f"\r  {N}[{O}▪{N}] {H}proses...{N} " + animation[i % len(animation)] +"\x1b[0m ")
            sys.stdout.flush()
        print()

    def cok(self):
        ses=requests.Session()
        url = par(ses.get("https://www.facebook.com/100032386028880/posts/674525870303608/?app=fbl").text,"html.parser")
        data = re.findall('"text":"(.*?)"',str(url))
        cokxyz = []
        n = 0
        for mmk in data:
            if len(mmk)>=20:
                try:
                    if mmk in cokxyz:pass
                    else:
                        n +=1
                        cokxyz.append(mmk)
                        prints(Panel(f"""[{n}]. [bold green]{mmk}[/]""", width=50))
                except:continue
        ahh = input(f"  [?] nomor : ")
        try:
            cookie = cokxyz[int(ahh)-1]
            self.login_cokie(cookie)
        except Exception:
            exit("  [!] gagal mengambil cookie")

    def login_cookie(self):
        prints(Panel("      [[green]°[/]] masukan cookie facebook anda [[green]°[/]]"))
        coki = input(f"  [{O}?{N}] cookie fb :{H} ")
        self.login_cokie(coki)

    def login_cokie(self, cok):
        self.loading()
        ses=requests.Session()
        try:
            data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cok})
            find_token = re.search("(EAAG\w+)", data.text)
            get = ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(find_token.group(1)),cookies={"cookie": cok})
            jsx = json.loads(get.text)
            nama = jsx["name"]
            open('.token.txt', 'a').write(find_token.group(1))
            open('.cokie.txt', 'a').write(cok)
            prints(Panel(f"""[[green]âœ“[/]] selamat [green]{nama}[/] cookie kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!"""));time.sleep(0.3)
            exit(f"\n  [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
        except requests.exceptions.ConnectionError:
            prints(Panel("😭­[bold red] Tidak ada koneksi internet"));exit()
        except (KeyError,AttributeError):
            prints(Panel("😯[bold red] Cookie kamu invalid"));exit()
