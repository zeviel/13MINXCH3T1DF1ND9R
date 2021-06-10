import amino
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.YELLOW)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminochatId", font="graffiti"))
print(pyfiglet.figlet_format("finder", font="graffiti"))
client = amino.Client()
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)
print("""1.Получить chatId публичных чатов/Get public chats chatId
2.Получить chatId чатов в которых вы находитесь/Get the chatId of the chats you are in""")
thechatidfinder = input("Type Number/Введите цифру: ")
if thechatidfinder == "1":
	try:
		print('\nLogged in and finding public chat chatids/Бот зашел и ищет chatId публичных чатов')
		chatInfo = sub_client.get_public_chat_threads(size=1000)
		for title, chatId in zip(chatInfo.title, chatInfo.chatId):
			print("Public ChatIds: ")
			print(f"{title}: {chatId}")
	except:
		pass

elif thechatidfinder == "2":
	try:
		print('\nLogged in and finding chatids of the chats you are in/Бот зашел и ищет chatId чатов')
		chatInfo = sub_client.get_chat_threads(size=1000)
		for title, chatId in zip(chatInfo.title, chatInfo.chatId):
			print("Chatids of the chats you are in: ")
			print(f"{title}: {chatId}")
	except:
		pass
