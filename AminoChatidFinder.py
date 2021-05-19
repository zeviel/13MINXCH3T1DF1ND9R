#импорт колорамы для оформления кода
from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.BLUE)
print("""Script by Zevi/Скрипт сделан Zevi
┌────────────────────────────────────┐
│Author :  LilZevi                   │
│Github : https://github.com/LilZevi │
└────────────────────────────────────┘
YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ
Telegram: @NowNameBo
▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄
█▀█ █░█░█ █ █░▀█ █░█
▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░
░▐█▀█░▐█░▐█─░▄█▀▄─▒█▀█▀█░▐██░▐█▀█▄
░▐█──░▐████░▐█▄▄▐█░░▒█░░─░█▌░▐█▌▐█
░▐█▄█░▐█░▐█░▐█─░▐█░▒▄█▄░░▐██░▐█▄█▀
█▀ ▀ █▄░█ █▀▄ █▀▀ █▀▀▄
█▀ █ █░▀█ █░█ █▀▀ █▐█▀
▀░ ▀ ▀░░▀ ▀▀░ ▀▀▀ ▀░▀▀""")
communities = {}
import amino
email = input("Email/Почта:")
password = input("Password/Пароль:")
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
x = 0
for name, id in zip(clients.name, clients.comId):
    print(f"{x + 1}.{name}")
    communities[x] = str(id)
    x+=1
communityid = communities[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)

print('\nLogged in and finding chatids/Бот зашел и ищет чат айди')

chatInfo = sub_client.get_chat_threads(size=1000)
for title, chatId in zip(chatInfo.title, chatInfo.chatId):
    print(f"{title}: {chatId}")
