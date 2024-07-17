import random
from time import sleep
import time
from getpass import getpass
import os, signal, sys
import subprocess
import progressbar
from getpass import getpass
from cybercpm import CyberCPM
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Style, init
from pystyle import System as pySystem

# Copyright (C) Lynx <DPR_LynX_Lovers> - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Lynx <DPR_LynX_Lovers>, 09, juli, 2024.

__CHANNEL_USERNAME__ = "DPR_LynXLovers"
__GROUP_USERNAME__   = "DPRLynXxX"

# Inisialisasi colorama
init(autoreset=True)

os.environ['PYCHARM_HOSTED'] = '1'

class COLOR:  # Definisi class untuk warna
    YELLOW    = '\033[93m'
    GREEN     = '\033[92m'
    RED       = '\033[91m'
    BOLD      = '\033[1m'
    ENDC      = '\033[0m'

def progressbar_function():
    widgets=[
        '  [%] SavingData ',
        COLOR.YELLOW          , progressbar.Percentage()                        , COLOR.ENDC,
        COLOR.RED + COLOR.BOLD, progressbar.Bar(left=' ', marker='━', right=' '), COLOR.ENDC,
        COLOR.YELLOW          , progressbar.Timer()                             , COLOR.ENDC
    ]

    for i in progressbar.progressbar(range(100), widgets=widgets):
        time.sleep(0.01)
        if i == 99:
            widgets[4] = COLOR.GREEN

banner = """
  -----------.        .-----------
    ------    \  __  /    ------
      -----    \(  )/    -----
         ---   ' \/ `   ---
           --- :    : ---
             --`    '--
             `/`/..\`\`
          ====UU====UU====
              '//||\\`
                ''``
×××××××××× CyberCPM Tools ××××××××××
       Car Parking Multiplayer
         ©Copyright_ɖքʀ•ʟʏռӼ


       Press Enter To Continue
"""[
    1:
]
Anime.Fade(Center.Center(banner), Colors.red_to_green, Colorate.Vertical, enter=True)
System.Clear()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    text = "=" * 58
    print(Colorate.Horizontal(Colors.yellow_to_green,(text)))
    versi = "CyberCPM Version: 1.02.4 || Author https://t.me/@DPR_LynX"
    print(Colorate.Horizontal(Colors.red_to_yellow,(versi)))
    text = "=" * 58
    print(Colorate.Horizontal(Colors.yellow_to_green,(text)))
    print("< Wajib Logout Account CPM Sebelum Menggunakan Tools Ini >")

def load_key_data(cpm):
    data = cpm.get_key_data()
    text = "=" * 20 + "[ Users Details ]" + "=" * 21
    print(Colorate.Horizontal(Colors.yellow_to_green,(text)))
    print(f"  >> Key Access  : {data.get('access_key')}")
    print(f"  >> Telegram ID : {data.get('telegram_id')}")
    print(f"  >> Balance     : {'Unlimited' if data.get('is_unlimited') else data.get('coins')}")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
            text = "=" * 18 + "[ Player Information ]" + "=" * 18
            print(Colorate.Horizontal(Colors.yellow_to_green,(text)))
            print(f"  >> Name     : {data.get('Name', 'UNDEFINED')}")
            print(f"  >> LocalID  : {data.get('localID', 'UNDEFINED')}")
            print(f"  >> Money    : {data.get('money', 'UNDEFINED')}")
            print(f"  >> Coin     : {data.get('coin', 'UNDEFINED')}")
        else:
            print("{Fore.RED}  [!] Upss. Sepertinya ada yang salah dengan akun anda, Silakan gunakan akun lain.")
            exit(1)

def prompt_valid_value(content, tag, password=False):
    while True:
        value = input(f"{content}: " if not password else getpass(f"{content}: "))
        if not value or value.isspace():
            print(f"{Fore.RED}  [X] tidak boleh kosong Silakan coba lagi.")
        else:
            return value

def signal_handler(sig, frame):
    print('\n  [!] Program dihentikan.\n')
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner()
        text = "=" * 19 + "[ Login Account CPM ]" + "=" * 18
        print(Colorate.Horizontal(Colors.yellow_to_green,(text)))
        acc_email = prompt_valid_value("  [?] Email Akun", "Email", password=False)
        acc_password = prompt_valid_value("  [?] Kata Sandi Akun", "Kata Sandi", password=False)
        acc_access_key = prompt_valid_value("  [?] Key Access", "Kunci Akses", password=False)
        print(f"{Fore.CYAN}  [%] Mencoba Masuk. ", end=None)
        cpm = CyberCPM(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(f"{Fore.RED}  [X] AKUN TIDAK DITEMUKAN.")
                sleep(2)
                continue
            elif login_response == 101:
                print(f"{Fore.RED}  [X] KATA SANDI SALAH.")
                sleep(2)
                continue
            elif login_response == 103:
                print(f"{Fore.RED}  [X] KUNCI AKSES TIDAK VALID.")
                sleep(2)
                continue
            else:
                print(f"{Fore.RED}  [X] Email atau password tidak ditemukan.!")
                sleep(2)
                continue
        else:
            print(f"{Fore.GREEN}  [✓] BERHASIL MASUK.")
            sleep(2)

        while True:
            banner()
            load_key_data(cpm)
            load_player_data(cpm)
            choices = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"]
            text = "=" * 25 + "[ MENU ]" + "=" * 25
            print(Colorate.Horizontal(Colors.yellow_to_green,(text)))
            print(f"{Fore.GREEN}  [01]{Style.RESET_ALL} Change nama {Fore.YELLOW}1000")
            print(f"{Fore.GREEN}  [02]{Style.RESET_ALL} Custom ID {Fore.YELLOW}3000")
            print(f"{Fore.GREEN}  [03]{Style.RESET_ALL} Change Money {Fore.YELLOW}2000")
            print(f"{Fore.GREEN}  [04]{Style.RESET_ALL} Change Coins {Fore.YELLOW}2000")
            print(f"{Fore.GREEN}  [05]{Style.RESET_ALL} Delete Friends List {Fore.YELLOW}500")
            print(f"{Fore.GREEN}  [06]{Style.RESET_ALL} Change Race Win {Fore.YELLOW}2000")
            print(f"{Fore.GREEN}  [07]{Style.RESET_ALL} Change Race Lose {Fore.YELLOW}2000")
            print(f"{Fore.GREEN}  [08]{Style.RESET_ALL} Instan King Rank {Fore.YELLOW}5000")
            print(f"{Fore.GREEN}  [09]{Style.RESET_ALL} TuneUP 414HP All Cars {Fore.YELLOW}2000")
            print(f"{Fore.GREEN}  [10]{Style.RESET_ALL} Full Unlock Account {Fore.YELLOW}10000")
            print(f"{Fore.GREEN}  [11]{Style.RESET_ALL} Unlock Premium Cars {Fore.YELLOW}2000")
            print(f"{Fore.GREEN}  [12]{Style.RESET_ALL} Inject Get All Cars {Fore.YELLOW}3000")
            print(f"{Fore.GREEN}  [13]{Style.RESET_ALL} Unlock Siren All Cars {Fore.YELLOW}2000")
            print(f"{Fore.GREEN}  [14]{Style.RESET_ALL} Cloning Account {Fore.YELLOW}6000")
            print(f"{Fore.GREEN}  [00]{Style.RESET_ALL} Keluar Dari Tools ")
            text = "=" * 58
            print(Colorate.Horizontal(Colors.yellow_to_green,(text)))
            service = input("  [?] Input menu [01-13]: ").strip()
            
            if service == "00": #Exit program
                print(f"  [!] Terima kasih telah menggunakan program kami... \n  [!] Telegram group: @{__CHANNEL_USERNAME__}.\n")
                sys.exit()
            elif service == "01": #Menu change name
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Masukkan Nama baru Anda.")
                print("  [!] Maksimal 50 karakter.")
                new_name = prompt_valid_value("  [?] Nama", "Name")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)
                if 0 <= len(new_name) <= 50:
                    if cpm.set_player_name(new_name):
                        progressbar_function()
                        print(f"{Fore.GREEN}  [✓] BERHASIL.")
                        text = "=" * 58
                        print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                        sleep(2)
                    else:
                        print(f"{Fore.RED}  [X] GAGAL.")
                        print(f"{Fore.RED}  [!] Silakan coba lagi.")
                        sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Gunakan nilai yang valid.")
                    sleep(2)
            elif service == "02": #Menu custom id
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Masukkan ID baru Anda.")
                print("  [!] Minimal 8 karakter dan maksimal 15 karakter.")
                new_id = prompt_valid_value("  [?] ID", "ID")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)    
                if 8 <= len(new_id) <= 15:
                    if cpm.set_player_localid(new_id):
                        progressbar_function()
                        print(f"{Fore.GREEN}  [✓] BERHASIL.")
                        text = "=" * 58
                        print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                        sleep(2)
                    else:
                        print(f"{Fore.RED}  [X] GAGAL.")
                        print(f"{Fore.RED}  [!] Silakan coba lagi.")
                        sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Gunakan ID yang valid.")
                    sleep(2)
            elif service == "03": #Menu change money
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Masukkan Money yang anda inginkan.")
                print("  [!] Maksimal 50000000 Money.")
                amount = prompt_valid_value("  [?] Money", "Money")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)    
                if 0 <= len(amount) <= 50000000:
                    if cpm.set_player_money(amount):
                        progressbar_function()
                        print(f"{Fore.GREEN}  [✓] BERHASIL.")
                        text = "=" * 58
                        print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                        sleep(2)
                    else:
                        print(f"{Fore.RED}  [X] GAGAL.")
                        print(f"{Fore.RED}  [!] Silakan coba lagi.")
                        sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Gunakan nilai yang valid.")
                    sleep(2)
            elif service == "04": #Menu change coins
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Masukkan Coins yang anda inginkan.")
                print("  [!] Maksimal 30000 coins.")
                amount = prompt_valid_value("  [?] Coins", "Coins")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)    
                if 0 <= len(amount) <= 30000:
                    if cpm.set_player_coins(amount):
                        progressbar_function()
                        print(f"{Fore.GREEN}  [✓] BERHASIL.")
                        text = "=" * 58
                        print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                        sleep(2)
                    else:
                        print(f"{Fore.RED}  [X] GAGAL.")
                        print(f"{Fore.RED}  [!] Silakan coba lagi.")
                        sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Gunakan nilai yang valid.")
                    sleep(2)
            elif service == "05": #Menu delete friends list
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Delete Friends List.")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)
                if cpm.delete_player_friends():
                    progressbar_function()
                    print(f"{Fore.GREEN}  [✓] BERHASIL.")
                    text = "=" * 58
                    print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                    sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Silakan coba lagi.")
                    sleep(2)
            elif service == "06": #Menu change race win
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Masukkan Race win yang anda inginkan.")
                print("  [!] Maksimal 1000.")
                amount = prompt_valid_value("  [?] Race Win", "Race Win")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)    
                if 0 <= len(amount) <= 1000:
                    if cpm.set_player_wins(amount):
                        progressbar_function()
                        print(f"{Fore.GREEN}  [✓] BERHASIL.")
                        text = "=" * 58
                        print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                        sleep(2)
                    else:
                        print(f"{Fore.RED}  [X] GAGAL.")
                        print(f"{Fore.RED}  [!] Silakan coba lagi.")
                        sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Gunakan nilai yang valid.")
                    sleep(2)
            elif service == "07": #Menu change race lose
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Masukkan Race lose yang anda inginkan.")
                print("  [!] Maksimal 1000.")
                amount = prompt_valid_value("  [?] Race Lose", "Race Lose")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)    
                if 0 <= len(amount) <= 1000:
                    if cpm.set_player_loses(amount):
                        progressbar_function()
                        print(f"{Fore.GREEN}  [✓] BERHASIL.")
                        text = "=" * 58
                        print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                        sleep(2)
                    else:
                        print(f"{Fore.RED}  [X] GAGAL.")
                        print(f"{Fore.RED}  [!] Silakan coba lagi.")
                        sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Gunakan nilai yang valid.")
                    sleep(2)
            elif service == "08": #Menu instan king rank
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Inject King Rank.")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)
                if cpm.set_player_rank():
                    progressbar_function()
                    print(f"{Fore.GREEN}  [✓] BERHASIL.")
                    text = "=" * 58
                    print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                    sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Silakan coba lagi.")
                    sleep(2)
            elif service == "09": #Menu inject siren all cars
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Inject TuneUP All Cars.")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)
                if cpm.tune_up():
                    progressbar_function()
                    print(f"{Fore.GREEN}  [✓] BERHASIL.")
                    text = "=" * 58
                    print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                    sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Silakan coba lagi.")
                    sleep(2)
            elif service == "10": #Menu Full unlock
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Full unlock account.")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)
                if cpm.full_unlock():
                    progressbar_function()
                    print(f"{Fore.GREEN}  [✓] BERHASIL.")
                    text = "=" * 58
                    print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                    sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Silakan coba lagi.")
                    sleep(2)
            elif service == "11": #Menu unlock premium cars
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Inject Premium Cars.")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)
                if cpm.unlock_paid_cars():
                    progressbar_function()
                    print(f"{Fore.GREEN}  [✓] BERHASIL.")
                    text = "=" * 58
                    print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                    sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Silakan coba lagi.")
                    sleep(2)
            elif service == "12": #Menu unlock all cars
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Inject Get All Cars.")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)
                if cpm.unlock_all_cars():
                    progressbar_function()
                    print(f"{Fore.GREEN}  [✓] BERHASIL.")
                    text = "=" * 58
                    print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                    sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Silakan coba lagi.")
                    sleep(2)
            elif service == "13": #Menu inject siren all cars
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Inject Siren All Cars.")
                print(f"{Fore.CYAN}  [%] Wait Process... ", end=None)
                if cpm.unlock_all_cars_siren():
                    progressbar_function()
                    print(f"{Fore.GREEN}  [✓] BERHASIL.")
                    text = "=" * 58
                    print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                    sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Silakan coba lagi.")
                    sleep(2)
            elif service == "14": #Menu clone account
                text = "=" * 58
                print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                print("  [!] Masukkan detail account.")
                to_email = prompt_valid_value("  [?] Account Email", "Email", password=False)
                to_password = prompt_valid_value("  [?] Account Password", "Password", password=False)
                print(f"{Fore.CYAN}  [%] Prosess Cloning Account.", end=None)
                if cpm.account_clone(to_email, to_password):
                    progressbar_function()
                    print(f"{Fore.GREEN}  [✓] BERHASIL.")
                    text = "=" * 58
                    print(Colorate.Horizontal(Colors.yellow_to_green, (text)))
                    sleep(2)
                else:
                    print(f"{Fore.RED}  [X] GAGAL.")
                    print(f"{Fore.RED}  [!] Silakan coba lagi.")
                    sleep(2)