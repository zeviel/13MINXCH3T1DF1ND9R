#импорт колорамы для оформления кода
from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.BLUE)
print("Script by Zevi/Скрипт сделан Zevi")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄")
print("█▀█ █░█░█ █ █░▀█ █░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░")
print("░▐█▀█░▐█░▐█─░▄█▀▄─▒█▀█▀█░▐██░▐█▀█▄")
print("░▐█──░▐████░▐█▄▄▐█░░▒█░░─░█▌░▐█▌▐█")
print("░▐█▄█░▐█░▐█░▐█─░▐█░▒▄█▄░░▐██░▐█▄█▀")
print("█▀ ▀ █▄░█ █▀▄ █▀▀ █▀▀▄")
print("█▀ █ █░▀█ █░█ █▀▀ █▐█▀")
print("▀░ ▀ ▀░░▀ ▀▀░ ▀▀▀ ▀░▀▀")
#инпут почты и пароля
import amino
email=input("Email/Почта:")
password=input("Password/Пароль:")
#Логин бота в аккаунт
client = amino.Client()
client.login(email=email, password=password)
for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
    print(f"{name}: {id}")
comid = input("Выберите сообщество(id): ")
sub_client = amino.SubClient(comId=comid,profile=client.profile)
print('\nLogged in and finding chatids/Бот зашел и ищет чат айди')

chatInfo = sub_client.get_chat_threads(size=1000)
for title, chatId in zip(chatInfo.title, chatInfo.chatId):
    print(f"{title}: {chatId}")