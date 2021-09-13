import AminoLab
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.YELLOW)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminochatidfinder", font="rectangles"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]

print("""[1] Get Joined Chats ChatId
[2] Get Public Chats ChatId""")
select = input("Select >> ")

if select == "1":
    try:
        joined_chats = client.my_chat_threads(ndc_Id=ndc_Id, size=100)
        for title, thread_Id in zip(
                joined_chats.title, joined_chats.thread_Id):
            print(f"{title} >> {thread_Id}")
    except Exception as e:
        print(e)

elif select == "2":
    try:
        public_chats = client.get_public_chat_threads(ndc_Id=ndc_Id, size=100)
        for title, thread_Id in zip(
                public_chats.title, public_chats.thread_Id):
            print(f"{title} >> {thread_Id}")
    except Exception as e:
        print(e)
