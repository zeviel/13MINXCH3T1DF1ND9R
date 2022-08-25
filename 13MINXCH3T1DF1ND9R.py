import amino
from colorama import init, Fore
from pyfiglet import figlet_format
init()
print(f"""{Fore.YELLOW}Script by zeviel
Github : https://github.com/zeviel""")
print(figlet_format("13MINXCH3T1DF1ND9R", font="rectangles"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
print(
"""
[1] Get Joined Chats ChatId
[2] Get Public Chats ChatId
"""
)
select = int(input("-- Select::: "))

if select == 1:
    try:
        joined_chats = sub_client.get_chat_threads(start=0, size=100)
        for chat_id, title in zip(
                joined_chats.chatId, joined_chats.title):
            print(f"-- {chat_id}:{title}")
    except Exception as e:
        print(e)

elif select == 2:
    try:
        public_chats = client.get_public_chat_threads(start=0, size=100)
        for chat_id, title in zip(
                public_chats.chatId, public_chats.title):
            print(f"-- {chat_id}:{title}")
    except Exception as e:
        print(e)
