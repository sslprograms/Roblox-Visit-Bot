import requests
import subprocess
import random
import time
import sys
import os


cookies = open('cookies.txt', 'r').read().splitlines()
visit_amount = int(input('Visits -> '))
placeId = int(input('Experience ID -> '))


os.system('start https://discord.gg/5TDERWxr9w')
subprocess.getoutput('title v1.0.0 Great Life')

visit_count = 0
while True:
    for cookie in cookies:

        with requests.session() as session:

            session.cookies['.ROBLOSECURITY'] = cookie

            session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
            session.headers['referer'] = 'https://www.roblox.com/'
            session.headers['origin'] = 'https://www.roblox.com'

            csrf = session.get(f'https://www.roblox.com/games/{placeId}').text.split('<meta name="csrf-token" data-token="')[1].split('">')[0].split('" />')[0]
            session.headers['x-csrf-token'] = csrf

            try:
                client_assertion = session.get(
                    'https://auth.roblox.com/v1/client-assertion/'
                ).json()['clientAssertion']

                authentication_ticket = session.post(
                    'https://auth.roblox.com/v1/authentication-ticket/',
                    json={
                        'clientAssertion':client_assertion
                    }
                ).headers['rbx-authentication-ticket']
            except:
                print('Possibly bad cookie :(')
                continue

            print(f'Launching Token...')
            visit_count += 1

            ticket = f'start roblox-player:1+launchmode:play+gameinfo:{authentication_ticket}+launchtime:{random.randint(1111111111111, 99999999999999)}+placelauncherurl:https%3A%2F%2Fwww.roblox.com%2FGame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{random.randint(1111111111111, 99999999999999)}%26placeId%3D{placeId}%26+robloxLocale:en_us+gameLocale:en_us+channel:+LaunchExp:InApp'
            os.system(ticket)
            print('Launched!')
            time.sleep(13)
            print(f'Visit Count: {visit_count}')

            if visit_count >= visit_amount:
                os.system('taskkill /f /im robloxplayerbeta.exe')
                os.system('cls')
                print(f'Attempted to add {visit_amount}!' )
                print('New Visit bot that will bypass the IP block soon.')
                input()
                sys.exit()
