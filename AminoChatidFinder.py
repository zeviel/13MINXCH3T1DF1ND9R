import amino
import asyncio
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.YELLOW)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminochatId", font="graffiti"))
print(pyfiglet.figlet_format("finder", font="graffiti"))

async def main():
	client = amino.Client()
	email = input("Email >> ")
	password = input("Password >> ")
	await client.login(email=email, password=password)
	clients = await client.sub_clients(start=0, size=100)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	communityid = clients.comId[int(input("Select the community >> "))-1]
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	print("""[1] Get public chats chatId
[2] Get joined chats chatId""")
	thechatidfinder = input("Select >> ")
	if thechatidfinder == "1":
		try:
			print("Finding public chats chatId")
			chats = sub_client.get_public_chat_threads(size=100)
			for title, chatId in zip(chats.title, chats.chatId):
				print(f"{title} >> {chatId}")
		except:
			pass

	elif thechatidfinder == "2":
		try:
			print("Finding joined chats chatId")
			chats = sub_client.get_chat_threads(size=100)
			for title, chatId in zip(chats.title, chats.chatId):
				print(f"{title} >> {chatId}")
		except:
			pass

asyncio.get_event_loop().run_until_complete(main())
