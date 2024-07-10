import random
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import subprocess
from cybercpm import CyberCPM

__CHANNEL_USERNAME__ = "DPR_LynXLovers"
__GROUP_USERNAME__   = "DPRLynXxX"

def git_pull():
    try:
        # Lakukan git pull secara diam-diam dengan parameter -q atau --quiet
        result = subprocess.check_output(['git', 'pull', '-q'])
        print("Updating check")
        print(result.decode('utf-8'))

    except subprocess.CalledProcessError as e:
        print("Updating failed")
        delete_script_file()

def delete_script_file():
    script_file = os.path.abspath(sys.argv[0])
    try:
        os.remove(script_file)
        print("Deleted script file")
        sys.exit(1)  # Keluar dari skrip setelah menghapus file
    except OSError as e:
        print("Error deleting script file")

if __name__ == "__main__":
    git_pull()

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("\t   < [ xxxx ©Copyright_ɖքʀ•ʟʏռӼ≝ xxxx ] >")
    console.print(f"       < [ Telegram: @{__CHANNEL_USERNAME__} OR @{__GROUP_USERNAME__} ] >")
    console.print("[bold red]==============================================================[bold red]")
    console.print("  < Wajib Logout Account CPM Sebelum Menggunakan Tools Ini >", end="\n\n")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
            console.print("[bold][red]========[/red][ PLAYER DETAILS ][red]========[/red][bold]\n")
            console.print(f">>> [bold green]Name   [bold white]: { (data.get('Name') if 'Name' in data else 'UNDEFINED') }")
            console.print(f">>> [bold green]LocalID[bold white]: { (data.get('localID') if 'localID' in data else 'UNDEFINED') }")
            console.print(f">>> [bold green]Money  [bold white]: { (data.get('money') if 'money' in data else 'UNDEFINED') }")
            console.print(f">>> [bold green]Coins  [bold white]: { (data.get('coin') if 'coin' in data else 'UNDEFINED') }", end="\n\n")
        else:
            console.print("[bold red]! ERROR[bold red]: new accounts most be signed-in to the game at least once !.")
            exit(1)
    else:
        console.print("[bold red]! ERROR[bold red]: seems like your login is not properly set !.")
        exit(1)

def load_key_data(cpm):
    data = cpm.get_key_data()
    console.print("[bold][red]======[/red][ ACCESS KEY DETAILS ][red]======[/red][bold]\n")
    console.print(f">>> [bold green]Access Key [bold white]: { data.get('access_key') }")
    console.print(f">>> [bold green]Telegram ID[bold white]: { data.get('telegram_id') }")
    console.print(f">>> [bold green]Balance    [bold white]: { (data.get('coins') if not data.get('is_unlimited') else 'Unlimited') }", end="\n\n")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(f"{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Account Email[bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Account Password[bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Access Key[bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Trying to Login[bold cyan]: ", end=None)
        cpm = CyberCPM(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]ACCOUNT NOT FOUND[bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]WRONG PASSWORD[bold red].")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red]INVALID ACCESS KEY[bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]TRY AGAIN[bold red].")
                console.print("[bold yellow]! Note[bold yellow]: make sure you filled out the fields !.")
                sleep(2)
                continue
        else:
            console.print("[bold green]SUCCESSFUL[bold green].")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            choices = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
            console.print("[bold red]=============[bold white][ MENU ][bold red]=============[bold white]")
            console.print("[bold green][01][bold white] Change money [bold yellow]1000[bold white]")
            console.print("[bold green][02][bold white] Change coins [bold yellow]2000[bold white]")
            console.print("[bold green][03][bold white] Instan king rank [bold yellow]4000[bold white]")
            console.print("[bold green][04][bold white] Custom ID [bold yellow]3000[bold white]")
            console.print("[bold green][05][bold white] Change name [bold yellow]100[bold white]")
            console.print("[bold green][06][bold white] Change rainbow name [bold yellow]100[bold white]")
            console.print("[bold green][07][bold white] Number plates [bold yellow]1000[bold white]")
            console.print("[bold green][08][bold white] Delete account [bold yellow]FREE[bold white]")
            console.print("[bold green][09][bold white] Register account [bold yellow]FREE[bold white]")
            console.print("[bold green][10][bold white] Delete friends list [bold yellow]100[bold white]")
            console.print("[bold green][11][bold white] Unlock premium cars [bold yellow]2000[bold white]")
            console.print("[bold green][12][bold white] Unlock all cars [bold yellow]3000[bold white]")
            console.print("[bold green][13][bold white] Unlock siren all cars [bold yellow]2000[bold white]")
            console.print("[bold green][14][bold white] Unlock engine W16 [bold yellow]2000[bold white]")
            console.print("[bold green][15][bold white] Unlock horns [bold yellow]2000[bold white]")
            console.print("[bold green][16][bold white] Disable engine damage [bold yellow]2000[bold white]")
            console.print("[bold green][17][bold white] Unlock unlimited fuel [bold yellow]2000[bold white]")
            console.print("[bold green][18][bold white] Unlock house [bold yellow]2000[bold white]")
            console.print("[bold green][19][bold white] Unlock smoke [bold yellow]2000[bold white]")
            console.print("[bold green][20][bold white] Change race win [bold yellow]2000[bold white]")
            console.print("[bold green][21][bold white] Change race lose [bold yellow]2000[bold white]")
            console.print("[bold green][22][bold white] Clone account to other account [bold yellow]4000[bold white]")
            console.print("[bold green][00][bold white] Exit tools[bold white]", end="")
            console.print("\n[bold red]===================================[bold white]")
            service = IntPrompt.ask(f"\n[bold][?] Input menu [01-22]", choices=choices, show_choices=False)
            if service == 0: # Exit
                console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
            elif service == 1: # Increase Money
                console.print("[bold cyan][!] Input money[bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[bold]")
                console.print("[bold cyan][%] Saving your data[bold cyan]: ", end=None)
                if amount > 0 and amount <= 50000000:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]SUCCESSFUL.[bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[bold red]")
                        console.print("[bold yellow][!] Please try again.[bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please use valid values.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                console.print("[bold cyan][!] Insert input coins.[bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[bold]")
                console.print("[bold cyan][%] Saving your data[bold cyan]: ", end=None)
                if amount > 0 and amount <= 90000:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]SUCCESSFUL.[bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[bold red]")
                        console.print("[bold yellow][!] Please try again.[bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please use valid values.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold cyan][%] Instan king rank.[bold cyan]: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print("[bold cyan][!] Enter your new ID.[bold cyan]")
                console.print("[bold cyan][!] Min ID 9 Character Max 14[bold cyan]")
                new_id = Prompt.ask("[bold][?] ID[bold]")
                console.print("[bold cyan][%] Saving your data[bold cyan]: ", end=None)
                if len(new_id) >= 9 and len(new_id) <= 14 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        console.print("[bold green]SUCCESSFUL.[bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[bold red]")
                        console.print("[bold yellow][!] Please try again.[bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please use valid ID.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print("[bold cyan][!] Enter your new Name.[bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[bold]")
                console.print("[bold cyan][%] Saving your data[bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(new_name):
                        console.print("[bold green]SUCCESSFUL.[bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[bold red]")
                        console.print("[bold yellow][!] Please try again.[bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please use valid values.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                console.print("[bold cyan][!] Enter your new Rainbow Name.[bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[bold]")
                console.print("[bold cyan][%] Saving your data[bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print("[bold green]SUCCESSFUL.[bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[bold red]")
                        console.print("[bold yellow][!] Please try again.[bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please use valid values.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[bold cyan][%] Giving you a Number Plates[bold cyan]: ", end=None)
                if cpm.set_player_plates():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                console.print("[bold cyan][!] After deleting your account there is no going back !!.[bold cyan]")
                answ = Prompt.ask("[bold cyan][?] Do You want to Delete this Account ?![bold cyan]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print("[bold cyan][%] Deleting Your Account[bold cyan]: [bold green]SUCCESSFUL.[bold green].")
                    console.print("==================================")
                    console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                else: continue
            elif service == 9: # Account Register
                console.print("[bold cyan][!] Registring new Account.[bold cyan]")
                acc2_email = prompt_valid_value("[bold][?] Account Email[bold]", "Email", password=False)
                acc2_password = prompt_valid_value("[bold][?] Account Password[bold]", "Password", password=False)
                console.print("[bold cyan][%] Creating new Account[bold cyan]: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    console.print(f"[bold red]! INFO[bold red]: In order to tweak this account with CyberCPM")
                    console.print("you most sign-in to the game using this account.")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] This email is already exists !.[bold yellow]")
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[bold cyan][%] Deleting your Friends[bold cyan]: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[bold cyan][%] Unlocking All Paid Cars[bold cyan]: ", end=None)
                if cpm.unlock_paid_cars():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[bold cyan][%] Unlocking All Cars[bold cyan]: ", end=None)
                if cpm.unlock_all_cars():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[bold cyan][%] Unlocking All Cars Siren[bold cyan]: ", end=None)
                if cpm.unlock_all_cars_siren():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[bold cyan][%] Unlocking w16 Engine[bold cyan]: ", end=None)
                if cpm.unlock_w16():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[bold cyan][%] Unlocking All Horns[bold cyan]: ", end=None)
                if cpm.unlock_horns():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[bold cyan][%] Unlocking Disable Damage[bold cyan]: ", end=None)
                if cpm.disable_engine_damage():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[bold cyan][%] Unlocking Unlimited Fuel[bold cyan]: ", end=None)
                if cpm.unlimited_fuel():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[bold cyan][%] Unlocking House 3[bold cyan]: ", end=None)
                if cpm.unlock_houses():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[bold cyan][%] Unlocking Smoke[bold cyan]: ", end=None)
                if cpm.unlock_smoke():
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 20: # Change Races Wins
                console.print("[bold cyan][!] Input race win.[bold cyan]")
                console.print("[bold cyan][!] Max 1000.[bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[bold]")
                console.print("[bold cyan][%] Changing your data[bold cyan]: ", end=None)
                if amount > 0 and amount <= 1000:
                    if cpm.set_player_wins(amount):
                        console.print("[bold green]SUCCESSFUL.[bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[bold red]")
                        console.print("[bold yellow][!] Please try again.[bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please use valid values.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 21: # Change Races Loses
                console.print("[bold cyan][!] Input race lose.[bold cyan]")
                console.print("[bold cyan][!] Max 1000.[bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[bold]")
                console.print("[bold cyan][%] Changing your data[bold cyan]: ", end=None)
                if amount > 0 and amount <= 1000:
                    if cpm.set_player_loses(amount):
                        console.print("[bold green]SUCCESSFUL.[bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[bold red]")
                        console.print("[bold yellow][!] Please try again.[bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please use valid values.[bold yellow]")
                    sleep(2)
                    continue
            elif service == 22: # Clone Account
                console.print("[bold cyan]Please Enter Account Detalis[bold cyan]:")
                to_email = prompt_valid_value("[bold][?] Account Email[bold]", "Email", password=False)
                to_password = prompt_valid_value("[bold][?] Account Password[bold]", "Password", password=False)
                console.print("[bold cyan][%] Cloning your account[bold cyan]: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    console.print("[bold green]SUCCESSFUL.[bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[bold red]")
                    console.print("[bold yellow][!] Please try again.[bold yellow]")
                    sleep(2)
                    continue
            else: continue
            break
        break
