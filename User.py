import requests,pyfiglet,time
import random,sys
#import haxkx
from random import choice
from colorama import Fore
from time import sleep
F = '\033[2;32m' 

Z = '\033[1;31m' 

C = '\033[2;35m' 

S = '\033[1;33m' 
haxkxbb = f"""{C}
⠀⠀⣸⣿⣿⣦⣿⣅⠀⢰⡟⠀⠘⡿⠛⣿⡿⠿⠿⠿⠿⠿⣿⡉⠉⠀⠀⠀⣸⣿
⣤⣾⣿⣿⣿⣿⣿⣿⣷⣿⣶⣶⣤⣷⣤⣿⣿⣀⡀⠀⠀⣀⣹⣷⣴⣶⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢏⣾⣿⣿⣿⢿⣿⣿⢋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣾⣿⣿⣿⢃⣿⡿⠃⢸⣿⣿⣿⣿⡟⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢈⣿⣿⣿⠼⣿⠧⠤⠼⠿⠿⠿⣿⡇⠻⠿⣿⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢀⣼⣿⣿⠠⣮⢯⠭⣗⣆⠀⠀⠀⠁⠀⠀⠉⠉⠒⠺⠭⣉⠻⣿⣿⣿⣿⣿⡟⡙
⠜⣿⣿⣿⠀⢣⣇⠀⢸⠣⠆⠀⠀⠀⠀⠀⣿⢶⣶⣼⣶⢄⠁⢻⣿⣿⣿⣿⡏⠀
⠀⣿⣿⣿⠀⠀⠙⠿⠷⠂⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⡏⡻⠆⠀⢿⣿⣿⣿⡇⠸
⢸⣿⣿⡿⡆⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠘⠻⠿⠍⠂⠀⠀⠀⠈⣿⣿⣿⣿⣴
⢸⣿⣿⣷⢷⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⢿
⢸⣿⣟⢔⢥⣇⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣠⡿⡻⣿⣿⣼
⢸⣿⢗⢕⢽⣿⣆⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡽⢊⣼⣿⣿⡟
⢸⡿⣢⠞⢽⣿⣿⣆⠀⠀⠉⠙⠱⠦⠄⠀⠀⠀⠀⠀⣀⢴⣿⠞⣱⣿⣿⣯⣿⠀
⢸⠃⡯⡪⣺⣿⢝⣿⣷⣄⠀⠀⠀⠀⠀⠀⢀⣀⣤⣾⣫⣷⣷⣿⣿⣿⡿⠟⢹⠀"""
print(haxkxbb)
TOKEN = input(f"{S}Enter TOKEN ➪ :  ")
print("")
İD = input("Enter ID ➪ : ")




vtl = pyfiglet.figlet_format(" haxkx")

tool = pyfiglet.figlet_format("                   haxkx")

def haxkx(z): 

   for e in z:

     sys.stdout.write(e) 

     sys.stdout.flush() 

     time.sleep(1/100)

haxkx(F+vtl+Z+tool)

colors = list (vars (Fore) . values ())

del colors [0]

msg =('_'*60)

text = str ()

for i in msg:

    text += i + choice (colors)

    print (text, end='\r')

    sleep (5/100)

print('   ') 

print('   ') 

colors = list (vars (Fore) . values ())

del colors [0]

msg =(    '  Please Wait... '  )

text = str ()

for i in msg:

    text += i + choice (colors)

    print (text, end='\r')

    sleep (7/100)

print('    ')

print('    ')

time.sleep(2)


link = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'

kullanci_ad = 'qwertyuiopasdfghjklzxcvbnm_.123456789._'

def haxkxcheck(kullanci_ad):

    sayi_ayarla = 5 

    number = ""

    while len(number) != sayi_ayarla:

        

        value = random.choice(kullanci_ad)

        number += value

    return number

istek = {

    'accept': '*/*',

    'accept-encoding': 'gzip, deflate, br',

    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

    'content-length': '365',

    'content-type': 'application/x-www-form-urlencoded',

    'origin': 'https://www.instagram.com',

    'referer': 'https://www.instagram.com/accounts/emailsignup/',

    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',

    'sec-ch-ua-mobile': '?0',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-origin',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',

    'x-asbd-id': '437806',

    'x-csrftoken': 'm2oFhkSBbCvBn3YrRgxEyDBdfWRL0WNH',

    'x-ig-app-id': '936619743392459',

    'x-ig-www-claim': 'hmac.AR1A5J3U1LoPNSPoW3tMou8rojZfx_8DmsIBsvSHSHv9okTO',

    'x-instagram-ajax': '478bcfd40589',

    'x-requested-with': 'XMLHttpRequest',

}





while True:

    username = (haxkxcheck(kullanci_ad))

    baslik = {

        'email': 'haxkx1@gmail.com',

        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:gwhvfgwvafhvwhgfv',

        'username': username,

        'first_name': 'haxkxbb',

}



    rq = requests.post(link, data=baslik, headers=istek).text



    if '{"username":' in rq:

        print(Z+f' Nhi Mila = username not availble : {username}'+Z)

        

    else:
        print(F+' HİT = username availble : '+username+F)
        vtltool= f"✅𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐇𝐈𝐓 ✅\n☯︎ 𝙐𝙎𝙀𝙍 : @{username}\n 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 : \n@Haxkx @toxic_tanji"
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={İD}&text='+vtltool)


        with open('Haxkx_ID.txt', 'a') as (HACK):

            HACK.write(' [+] 𝐔𝐒𝐄𝐑 𝐇𝐈𝐓  : {} \n\n@Haxkx'.format(username))
#haxkx1 
