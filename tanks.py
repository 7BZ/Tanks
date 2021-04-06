import discord, os, time, requests, json
from colorama import Fore
from pypresence import Presence
from discord.ext import commands

os.system(f'cls & mode 77,22 & title Tanks - Configuration')
token = input(f'[{Fore.BLUE}+{Fore.RESET}] Token{Fore.BLUE}: {Fore.RESET}')
rpresence = input(f'[{Fore.BLUE}+{Fore.RESET}] Rich Presence (Y \ N){Fore.BLUE}: {Fore.RESET}')

def RichPresence():
    if rpresence.upper() == "y" or rpresence.lower() == "y":
        try:
            RPC = Presence("829084497655234571")
            RPC.connect()
            RPC.update(large_image="8",details="Cry with me?",buttons=[{"label":"Github","url":"https://github.com/7BZ"}],start=time.time())
        except:
            pass
rpresence = RichPresence()

client = commands.Bot(command_prefix='>',self_bot=True,intents=discord.Intents.all())
client.remove_command('help')

class Tanks:
    def __init__(self):
        pass

    def tPFP(self):
        userid = input(f"[{Fore.BLUE}+{Fore.RESET}] User ID{Fore.BLUE}: {Fore.RESET}")
        user = client.get_user(int(userid))
        with open(f'{user.name}.gif','wb') as f:
            f.write(requests.get(user.avatar_url).content)
            f.close()

    def tSave(self):
        userid = input(f"[{Fore.BLUE}+{Fore.RESET}] User ID{Fore.BLUE}: {Fore.RESET}")
        user = client.get_user(int(userid))
        r = requests.get(f'https://discord.com/api/v8/users/{int(userid)}/profile',headers={"Authorization":token})
        r1 = requests.get(f'https://discord.com/api/v8/users/{int(userid)}/relationships',headers={"Authorization":token})
        if r.json()['connected_accounts'] != None:
            connected_accounts = '\n'.join(json.dumps(d) for d in r.json()['connected_accounts'])
        else:
            connected_accounts == "None"
        if r.json()['mutual_guilds'] != None:
            mutual_guilds = '\n'.join(json.dumps(d) for d in r.json()['mutual_guilds'])
        else:
            mutual_guilds == "None"
        if r.json()['premium_since'] != None:
            premium_since = f"{r.json()['premium_since']}"
        else:
            premium_since == "None"
        if r.json()['user'] != None:
            user = {"id":user.id,"avatar":user.avatar_url,"public_flags":user.public_flags}
        else:
            user == "None"
        if r1.text != []:
            friends = r1.text
        else:
            friends == "None"

        with open(f"{r.json()['user']['username']}#{r.json()['user']['discriminator']}.txt",'a') as f:
            f.write(f"User: {user}\n\nMutual Guilds: {mutual_guilds}\n\nConnected Accounts: {connected_accounts}\n\nPremium Since: {premium_since}\n\nMutual Friends: {friends}")
            f.close()


    def Menu(self):
        os.system(f'cls & mode 77,22 & title Tanks - {client.user}')
        print(f'''
                {Fore.LIGHTBLACK_EX}▄▄▄█████▓▄▄▄      ███▄    █ ██ ▄█▀ ██████
                ▓  ██▒ ▓▒████▄    ██ ▀█   █ ██▄█▒▒██    ▒
                ▒ ▓██░ ▒▒██  ▀█▄ ▓██  ▀█ ██▓███▄░░ ▓██▄
                ░ ▓██▓ ░░██▄▄▄▄██▓██▒  ▐▌██▓██ █▄  ▒   ██▒
                  ▒██▒ ░ ▓█   ▓██▒██░   ▓██▒██▒ █▒██████▒▒
                  ▒ ░░   ▒▒   ▓▒█░ ▒░   ▒ ▒▒ ▒▒ ▓▒ ▒▓▒ ▒ ░
                    ░     ▒   ▒▒ ░ ░░   ░ ▒░ ░▒ ▒░ ░▒  ░ ░
                  ░       ░   ▒     ░   ░ ░░ ░░ ░░  ░  ░
                              ░  ░        ░░  ░        ░

 {Fore.BLUE}╔═════════════════════════════════╗     {Fore.BLUE}╔═════════════════════════════════╗
 {Fore.BLUE}║       {Fore.RESET}C O M M A N D S           {Fore.BLUE}║     ║         {Fore.RESET}C R E D I T S           {Fore.BLUE}║
 {Fore.BLUE}║                                 {Fore.BLUE}║     ║                                 {Fore.BLUE}║
 {Fore.BLUE}║  PFP             {Fore.RESET}Steals PFP     {Fore.BLUE}║     ║    {Fore.BLUE}GITHUB: {Fore.RESET}7BZ                  {Fore.BLUE}║
 {Fore.BLUE}║  SAVE            {Fore.RESET}Save UserInfo  {Fore.BLUE}║     ║                                 {Fore.BLUE}║
 {Fore.BLUE}╚═════════════════════════════════╝     ╚═════════════════════════════════╝
{Fore.RESET}''')
        lmao = input(f"[{Fore.BLUE}+{Fore.RESET}] Choice{Fore.BLUE}: {Fore.RESET}")
        if lmao.upper() == "pfp" or lmao.lower() ==  "pfp":
            self.tPFP()
            time.sleep(2)
            self.Menu()
        elif lmao.upper() == "save" or lmao.lower() == "save":
            self.tSave()
            time.sleep(2)
            self.Menu()
        else:
            time.sleep(2)
            self.Menu()

@client.event
async def on_error(error):
    with open('errors.txt','a') as f:
        f.write(f'Error Location: {error}\n')
        f.close()
    time.sleep(2)
    Tanks().Menu()

@client.event
async def on_ready():
    Tanks().Menu()

try:
    client.run(token,bot=False)
except Exception as e:
    with open('errors.txt','a') as f:
        f.write(f'Error: {e}')
        f.close()
