import random
from time import sleep
import time
import json
from getpass import getpass
import os, signal, sys
import subprocess
import progressbar
from getpass import getpass
from cybercpm import CyberCPM
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Style, init
from pystyle import System as pySystem
from datacar import nomercar, namacar
from colorama import Fore, Style, init
import progressbar
import time

# © Lynx | DPR_LynX_Lovers — 2025
# No stealing. No tracing. No funny business.
# Engineered in the shadows by DPRLynX on June 16th, 2025

__CHANNEL_USERNAME__ = "DPR_LynXLovers"
__GROUP_USERNAME__   = "DPR_LynX"

init(autoreset=True)

init()

class COLOR:
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    BOLD = Style.BRIGHT
    ENDC = Style.RESET_ALL

os.environ['PYCHARM_HOSTED'] = '1'

def git_pull():
    try:
        result = subprocess.check_output(['git', 'pull']).decode('utf-8')
        if "Already up to date." in result:
            print(f"{Fore.GREEN}No updates. The script is already up to date.\n")
        else:
            print(f"\n{Fore.YELLOW}Update successful. The script has been updated.\n")
            print(f"{Fore.RED}Please restart the script.")
            sys.exit(0)
    except subprocess.CalledProcessError:
        print(f"\n{Fore.RED}Checking update failed.")
        try:
            os.remove(sys.argv[0])
        except:
            pass
        sys.exit(1)

git_pull()

def show_progress(message="Loading...", duration=1):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN]
    symbols = ['•', '•', '•']
    left_bracket = Fore.BLUE + Style.BRIGHT + '⟨' + Style.RESET_ALL
    right_bracket = Fore.BLUE + Style.BRIGHT + '⟩' + Style.RESET_ALL
    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL}{message} ", end="")
    print(left_bracket, end="", flush=True)
    start_time = time.time()
    steps = 15
    delay = duration / steps
    for i in range(steps):
        color = colors[i % len(colors)]
        symbol = color + symbols[i % len(symbols)] + Style.RESET_ALL
        print(symbol, end="", flush=True)
        time.sleep(delay)
    print(right_bracket + f" {Fore.GREEN}100%" + Style.RESET_ALL)
    print()



banner = """
╔════════════════════════════════════════════════════╗
║                                                    ║
║           ╔═══╗───╔╗──────╔═══╗                    ║
║           ║╔═╗║───║║──────║╔═╗║                    ║
║           ║║─╚╬╗─╔╣╚═╦══╦═╣║─╚╬══╦═╦══╗            ║
║           ║║─╔╣║─║║╔╗║║═╣╔╣║─╔╣╔╗║╔╣║═╣            ║
║           ║╚═╝║╚═╝║╚╝║║═╣║║╚═╝║╚╝║║║║═╣            ║
║           ╚═══╩═╗╔╩══╩══╩╝╚═══╩══╩╝╚══╝            ║
║           ────╔═╝║                                 ║
║           ────╚══╝                                 ║
╠════════════════════════════════════════════════════╣
║               ⚡ CyberCPM TOOLS ⚡                 ║
║           Car Parking Multiplayer Utilities        ║
║           Coded by: ɖքʀ•ʟʏռӼ | © 2025              ║
╚════════════════════════════════════════════════════╝
            [ Press Enter to continue ]
"""[1:]
Anime.Fade(Center.Center(banner), Colors.red_to_green, Colorate.Vertical, enter=True)
System.Clear()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
    print(Colorate.Horizontal(Colors.red_to_yellow, "CPM2 Tools Version: 1.02.4 || Author https://t.me/@DPR_LynX"))
    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
    print("< Wajib Logout Account CPM Sebelum Menggunakan Tools Ini >")

def load_key_data(cpm):
    data = cpm.get_key_data()
    print(Colorate.Horizontal(Colors.green_to_white, "=" * 20 + "[ Users Details ]" + "=" * 21))
    print(f"  >> Key Access  : {data.get('access_key')}")
    print(f"  >> Telegram ID : {data.get('telegram_id')}")
    print(f"  >> Balance     : {'Unlimited' if data.get('is_unlimited') else data.get('coins')}")

def count_saved_cars():
    folder_path = "dataplayer/cars"
    if not os.path.exists(folder_path):
        print("  >> Car Count   : 0")
        return
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
    print(f"  >> Car Count   : {len(files)}")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data', {})
        player_storage = data.get('PlayerStorage', {})
        wallet_data = data.get('WalletData', {})
        if ('Name' in player_storage and
            'LocalID' in player_storage and
            'Other' in player_storage and
            'Slots' in player_storage['Other'] and
            'Money' in wallet_data and
            'Coins' in wallet_data):
            total_slots = player_storage['Other'].get('Slots', 'UNDEFINED')
            print(Colorate.Horizontal(Colors.green_to_white, "=" * 18 + "[ Player Information ]" + "=" * 18))
            print(f"  >> Name        : {player_storage.get('Name', 'UNDEFINED')}")
            print(f"  >> LocalID     : {player_storage.get('LocalID', 'UNDEFINED')}")
            print(f"  >> Money       : {wallet_data.get('Money', 'UNDEFINED')}")
            print(f"  >> Coin        : {wallet_data.get('Coins', 'UNDEFINED')}")
            print(f"  >> Total Slots : {total_slots}")
            cpm.get_all_player_cars()
            count_saved_cars()
        else:
            print("{Fore.RED}  [!] Upss. Sepertinya ada yang salah dengan akun anda, Silakan gunakan akun lain.")
            exit(1)

def prompt_valid_value(content, tag, password=False):
    while True:
        value = input(f"{content}: " if not password else getpass(f"{content}: "))
        if not value or value.isspace():
            print(f"{Fore.RED}  ---[{Style.RESET_ALL} tidak boleh kosong Silakan coba lagi.")
        else:
            return value

def signal_handler(sig, frame):
    print(f'\n{Fore.RED}  ---[ Program dihentikan ]---\n')
    exit(0)

def cariid(urutan):
    for mydatacar in nomercar:
        if mydatacar["urutan"] == urutan:
            return mydatacar["id"]

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner()
        print(Colorate.Horizontal(Colors.green_to_white, "=" * 17 + "[ LOGIN TO CPM ACCOUNT ]" + "=" * 17))
        acc_email = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Email", "Email", False)
        acc_password = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Password", "Password", False)
        acc_access_key = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Access Key", "Access Key", False)
        print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Attempting login... ", end="")
        cpm = CyberCPM(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)

        if login_response != 0:
            if login_response == 100:
                print(f"{Fore.RED}  ACCOUNT NOT FOUND.")
                sleep(2)
                continue
            elif login_response == 101:
                print(f"{Fore.RED}  WRONG PASSWORD.")
                sleep(2)
                continue
            elif login_response == 103:
                print(f"{Fore.RED}  INVALID ACCESS KEY.")
                sleep(2)
                continue
            else:
                print(f"{Fore.RED}  Email or password not recognized!")
                sleep(2)
                continue
        else:
            print(f"{Fore.GREEN} Login Successful.")
            show_progress(f" Loading your data...", duration=2)
            sleep(2)

        while True:
            banner()
            load_key_data(cpm)
            load_player_data(cpm)
            cpm.save_player_slots_collection()
            print(Colorate.Horizontal(Colors.green_to_white, "=" * 25 + "[ MENU ]" + "=" * 25))
            print(f"  [{Fore.GREEN}01{Style.RESET_ALL}] Change Name {Fore.YELLOW}Free")
            print(f"  [{Fore.GREEN}02{Style.RESET_ALL}] Change Money {Fore.YELLOW}3000")
            print(f"  [{Fore.GREEN}03{Style.RESET_ALL}] Finish All Levels Done {Fore.YELLOW}10000")
            print(f"  [{Fore.GREEN}04{Style.RESET_ALL}] Remove Male Face {Fore.YELLOW}3000")
            print(f"  [{Fore.GREEN}05{Style.RESET_ALL}] Remove Female Face {Fore.YELLOW}3000")
            print(f"  [{Fore.GREEN}06{Style.RESET_ALL}] Unlock All Male Attributes {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}07{Style.RESET_ALL}] Unlock All Female Attributes {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}08{Style.RESET_ALL}] Unlock All Animations {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}09{Style.RESET_ALL}] Unlock All Homes {Fore.YELLOW}20000")
            print(f"  [{Fore.GREEN}10{Style.RESET_ALL}] Unlock All Paints {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}11{Style.RESET_ALL}] Unlock All Wheels {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}12{Style.RESET_ALL}] Unlock Brakes {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}13{Style.RESET_ALL}] Unlock Calipers {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}14{Style.RESET_ALL}] Unlock Sound Police {Fore.YELLOW}7500")
            print(f"  [{Fore.GREEN}15{Style.RESET_ALL}] Unlock Police {Fore.YELLOW}10000")
            print(f"  [{Fore.GREEN}16{Style.RESET_ALL}] Unlock Bodykits {Fore.YELLOW}10000")
            print(f"  [{Fore.GREEN}17{Style.RESET_ALL}] Unlock Cars {Fore.YELLOW}3000")
            print(f"  [{Fore.GREEN}18{Style.RESET_ALL}] Swap Gearbox AWD {Fore.YELLOW}10000")
            print(f"  [{Fore.GREEN}00{Style.RESET_ALL}] Exit Tool")
            print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
            choice = input(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Select menu [01-18]: ").strip()

            if choice == "00":
                print(f"{Fore.CYAN}  ---[ Thanks for using our tool!\n ---[  Join our Telegram group: @DPR_LynX")
                sys.exit()

            elif choice == "01":
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Enter your new name.")
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Max 50 characters.")
                new_name = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Name", "Name")
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                if 0 < len(new_name) <= 50:
                    if cpm.save_player_name(new_name):
                        show_progress(f" Applying changes...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                else:
                    print(f"{Fore.RED}  Invalid input.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "02":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 3000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Enter your desired amount of money.")
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Max 50,000,000.")
                amount = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Money", "Money")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if amount.isdigit() and 0 < int(amount) <= 50000000:
                        if cpm.save_player_money(amount):
                            show_progress(f" Applying changes...", duration=2)
                            print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                        else:
                            print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                    else:
                        print(f"{Fore.RED}  Invalid amount.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "03":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 10000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Complete all levels.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.levels_done():
                        show_progress(f" Applying...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "04":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 3000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Remove male face.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.face_male():
                        show_progress(f" Removing...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfully!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "05":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 3000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Remove female face.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.face_female():
                        show_progress(f" Removing...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "06":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all male attributes.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.attribute_male():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "07":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all female attributes.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.attribute_female():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "08":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all animations.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_animations_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "09":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 20000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all homes.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_home_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "10":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all paints.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_paints_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "11":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all wheels.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_wheels_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "12":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock brakes.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_brakes_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "13":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock calipers.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_calipers_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "14":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 7500
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock sound police.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_sound_police_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)

            elif choice == "15":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 10000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 21 + "[ Unlock Police ]" + "=" * 21))
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    sleep(2)
                else:
                    print("  Cars List:")
                    print(namacar)
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    input_ids = input(f"{Fore.CYAN} ---[{Style.RESET_ALL} Input number car: ").strip()
                    if not input_ids:
                        print(f"{Fore.RED} ---[ Input tidak boleh kosong.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    else:
                        nomor_list = [n.strip() for n in input_ids.split(",") if n.strip().isdigit()]
                        for i, nomor in enumerate(nomor_list, 1):
                            urutan = int(nomor)
                            car_entry = next((item for item in nomercar if item["urutan"] == urutan), None)
                            if not car_entry:
                                print(f"{Fore.RED} ---[ Please enter the correct car number.")
                                continue
                            carid = str(car_entry["id"])
                            carname = car_entry.get("name", f"Car ID {carid}")
                            filepath = f"dataplayer/cars/{carid}"
                            if not os.path.isfile(filepath):
                                print(f"{Fore.RED} ---[ You don't have a car with CarID {carid}")
                                continue
                            with open(filepath, "r") as f:
                                data = json.load(f)
                            car_id = data["data"].get("CarID", "???")
                            print(f"{Fore.CYAN} ---[{Style.RESET_ALL} Injecting CarID: {car_id} ({i}/{len(nomor_list)})...", end=" ")
                            result = cpm.unlocked_police(data["data"])
                            if result:
                                print(f"{Fore.GREEN} Successfuly!")
                            else:
                                print(f"{Fore.RED} Failed.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)

            elif choice == "16":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 10000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 21 + "[ Unlock Bodykits ]" + "=" * 21))
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    sleep(2)
                else:
                    print("  Cars List:")
                    print(namacar)
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    input_ids = input(f"{Fore.CYAN} ---[{Style.RESET_ALL} Input number car: ").strip()
                    if not input_ids:
                        print(f"{Fore.RED} ---[ Input tidak boleh kosong.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    else:
                        nomor_list = [n.strip() for n in input_ids.split(",") if n.strip().isdigit()]
                        for i, nomor in enumerate(nomor_list, 1):
                            urutan = int(nomor)
                            car_entry = next((item for item in nomercar if item["urutan"] == urutan), None)
                            if not car_entry:
                                print(f"{Fore.RED} ---[ Please enter the correct car number.")
                                continue
                            carid = str(car_entry["id"])
                            carname = car_entry.get("name", f"Car ID {carid}")
                            filepath = f"dataplayer/cars/{carid}"
                            if not os.path.isfile(filepath):
                                print(f"{Fore.RED} ---[ You don't have a car with CarID {carid}")
                                continue
                            with open(filepath, "r") as f:
                                data = json.load(f)
                            car_id = data["data"].get("CarID", "???")
                            print(f"{Fore.CYAN} ---[{Style.RESET_ALL} Injecting CarID: {car_id} ({i}/{len(nomor_list)})...", end=" ")
                            result = cpm.unlocked_bodykits(data["data"])
                            if result:
                                print(f"{Fore.GREEN} Successfuly!")
                            else:
                                print(f"{Fore.RED} Failed.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)

            elif choice == "17":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 3000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 21 + "[ Unlock Cars ]" + "=" * 22))
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    sleep(2)
                else:
                    print("  Cars List:")
                    print(namacar)
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    input_ids = input(f"{Fore.CYAN} ---[{Style.RESET_ALL} Input number car: ").strip()
                    if not input_ids:
                        print(f"{Fore.RED} ---[ Input tidak boleh kosong.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    else:
                        nomor_list = [n.strip() for n in input_ids.split(",") if n.strip().isdigit()]
                        for i, nomor in enumerate(nomor_list, 1):
                            urutan = int(nomor)
                            car_entry = next((item for item in nomercar if item["urutan"] == urutan), None)
                            if not car_entry:
                                print(f"{Fore.RED} ---[ Please enter the correct car number.")
                                continue
                            carid = str(car_entry["id"])
                            carname = car_entry.get("name", f"Car ID {carid}")
                            filepath = f"datacars/cars/{carid}"
                            if not os.path.isfile(filepath):
                                print(f"{Fore.RED} ---[ You don't have a car with CarID {carid}")
                                continue
                            with open(filepath, "r") as f:
                                data = json.load(f)
                            car_id = data["data"].get("CarID", "???")
                            print(f"{Fore.CYAN} ---[{Style.RESET_ALL} Injecting CarID: {car_id} ({i}/{len(nomor_list)})...", end=" ")
                            result = cpm.save_player_car(data["data"])
                            if result:
                                print(f"{Fore.GREEN} Successfuly!")
                            else:
                                print(f"{Fore.RED} Failed.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    
            elif choice == "18":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 10000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 18 + "[ Swap Gearbox To AWD ]" + "=" * 17))
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    sleep(2)
                else:
                    print("  Cars List:")
                    print(namacar)
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    input_ids = input(f"{Fore.CYAN} ---[{Style.RESET_ALL} Input number car: ").strip()
                    if not input_ids:
                        print(f"{Fore.RED} ---[ Input tidak boleh kosong.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    else:
                        nomor_list = [n.strip() for n in input_ids.split(",") if n.strip().isdigit()]
                        for i, nomor in enumerate(nomor_list, 1):
                            urutan = int(nomor)
                            car_entry = next((item for item in nomercar if item["urutan"] == urutan), None)
                            if not car_entry:
                                print(f"{Fore.RED} ---[ Please enter the correct car number.")
                                continue
                            carid = str(car_entry["id"])
                            carname = car_entry.get("name", f"Car ID {carid}")
                            filepath = f"dataplayer/cars/{carid}"
                            if not os.path.isfile(filepath):
                                print(f"{Fore.RED} ---[ You don't have a car with CarID {carid}")
                                continue
                            with open(filepath, "r") as f:
                                data = json.load(f)
                            car_id = data["data"].get("CarID", "???")
                            print(f"{Fore.CYAN} ---[{Style.RESET_ALL} Injecting CarID: {car_id} ({i}/{len(nomor_list)})...", end=" ")
                            result = cpm.swap_gearbox_awd(data["data"])
                            if result:
                                print(f"{Fore.GREEN} Successfuly!")
                            else:
                                print(f"{Fore.RED} Failed.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
