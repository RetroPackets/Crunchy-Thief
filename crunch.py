
from colorama import Fore,Style
import os
import src.checker

os.system("clear")

banner = f"""\033[1m {Fore.WHITE}
⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗         {Fore.RED}😈{Fore.WHITE} ʟᴇᴛꜱ ꜱᴛᴇᴀʟ ꜱᴏᴍᴇ ᴄʀᴜɴᴄʜʏʀᴏʟʟ {Fore.RED}😈{Fore.WHITE}
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄ {Fore.YELLOW} █▀▀ █▀█ █░█ █▄░█ █▀▀ █░█ █▄█   {Fore.WHITE}▀█▀ █░█ █ █▀▀ █▀▀
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄  █▄▄ █▀▄ █▄█ █░▀█ █▄▄ █▀█ ░█░   {Fore.CYAN}░█░ █▀█ █ ██▄ █▀░{Fore.WHITE}
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄  {Fore.RED}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Fore.WHITE}
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄    {Fore.MAGENTA}DEVELOPER {Fore.RED}: {Fore.WHITE}RetroPackets
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴      {Fore.MAGENTA}DISCORD {Fore.RED}: {Fore.WHITE}https://discord.gg/YkwJWJTGqs 
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿       {Fore.MAGENTA}GITHUB {Fore.RED}: {Fore.WHITE}https://github.com/RetroPackets
"""
print (banner)

def main():
    
    if not os.path.exists('result'):
        os.makedirs('result')
    filename = input(f"\033[1m{Fore.BLUE} 𝗘𝗡𝗧𝗘𝗥 𝗧𝗛𝗘 𝗡𝗔𝗠𝗘 𝗢𝗥 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛{Fore.YELLOW} :{Fore.WHITE} ")
    #print("")
    if os.path.isfile(filename):
        src.checker.CrunchyrollChecker.create(filename)
    else:
        print(f"{Fore.RED}File not found{Fore.YELLOW}.{Fore.WHITE}")


### yeaaahhhh!!!!
if __name__ == "__main__":
    main()

