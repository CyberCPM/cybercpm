t='[bold cyan][%] Changing your data[bold cyan]: '
s='[bold cyan][!] Max 1000.[bold cyan]'
r='[bold][?] Name[bold]'
q='__main__'
k='Password'
j='[bold][?] Account Password[bold]'
i='Email'
h='[bold][?] Account Email[bold]'
g=True
f='\n\n'
e=tuple
d=enumerate
c=max
a='[bold][?] Amount[bold]'
Z=int
W='[bold cyan][%] Saving your data[bold cyan]: '
U='[bold yellow][!] Please use valid values.[bold yellow]'
T=print
Q=False
P=len
N='[bold cyan][?] Do You want to Exit ?[bold cyan]'
M='[bold yellow][!] Please try again.[bold yellow]'
L='[bold green]SUCCESSFUL.[bold green]'
K='=================================='
J=None
F='[bold red]FAILED.[bold red]'
C='n'
B='y'
import random as l
from time import sleep as E
import os,signal as m,sys as b
from rich.console import Console as u
from rich.prompt import Prompt as G,IntPrompt as V
from rich.text import Text
from rich.style import Style
import subprocess as n
from cybercpm import CyberCPM as v
__CHANNEL_USERNAME__='DPR_LynXLovers'
__GROUP_USERNAME__='DPRLynXxX'
def w():
	try:A=n.check_output(['git','pull','-q']);T('Updating check');T(A.decode('utf-8'))
	except n.CalledProcessError as B:T('Updating failed');x()
def x():
	A=os.path.abspath(b.argv[0])
	try:os.remove(A);T('Deleted script file');b.exit(1)
	except OSError as B:T('Error deleting script file')
if __name__==q:w()
def y(sig,frame):T('\n Bye Bye...');b.exit(0)
def AB(text,colors):
	B=colors;C=text.splitlines();F=P(C);G=c(P(A)for A in C);A=Text()
	for(H,I)in d(C):
		for(J,D)in d(I):
			if D!=' ':E=Z((J/(G-1 if G>1 else 1)+H/(F-1 if F>1 else 1))*.5*(P(B)-1));E=min(c(E,0),P(B)-1);K=Style(color=B[E]);A.append(D,style=K)
			else:A.append(D)
		A.append('\n')
	return A
def o(console):A=console;os.system('cls'if os.name=='nt'else'clear');A.print('\t   < [ xxxx ©Copyright_ɖքʀ•ʟʏռӼ≝ xxxx ] >');A.print(f"       < [ Telegram: @{__CHANNEL_USERNAME__} OR @{__GROUP_USERNAME__} ] >");A.print('[bold red]==============================================================[bold red]');A.print('  < Wajib Logout Account CPM Sebelum Menggunakan Tools Ini >',end=f)
def z(cpm):
	H='Name';F='coin';E='money';D='localID';C='UNDEFINED';G=cpm.get_player_data()
	if G.get('ok'):
		B=G.get('data')
		if'floats'in B and D in B and E in B and F in B:A.print('[bold][red]========[/red][ PLAYER DETAILS ][red]========[/red][bold]\n');A.print(f">>> [bold green]Name   [bold white]: {B.get(H)if H in B else C}");A.print(f">>> [bold green]LocalID[bold white]: {B.get(D)if D in B else C}");A.print(f">>> [bold green]Money  [bold white]: {B.get(E)if E in B else C}");A.print(f">>> [bold green]Coins  [bold white]: {B.get(F)if F in B else C}",end=f)
		else:A.print('[bold red]! ERROR[bold red]: new accounts most be signed-in to the game at least once !.');exit(1)
	else:A.print('[bold red]! ERROR[bold red]: seems like your login is not properly set !.');exit(1)
def A0(cpm):B=cpm.get_key_data();A.print('[bold][red]======[/red][ ACCESS KEY DETAILS ][red]======[/red][bold]\n');A.print(f">>> [bold green]Access Key [bold white]: {B.get('access_key')}");A.print(f">>> [bold green]Telegram ID[bold white]: {B.get('telegram_id')}");A.print(f">>> [bold green]Balance    [bold white]: {B.get('coins')if not B.get('is_unlimited')else'Unlimited'}",end=f)
def R(content,tag,password=Q):
	while g:
		A=G.ask(content,password=password)
		if not A or A.isspace():T(f"{tag} cannot be empty or just spaces. Please try again.")
		else:return A
def A1(start_color,end_color,fraction):A=e(Z(start_color[A:A+2],16)for A in(1,3,5));B=e(Z(end_color[A:A+2],16)for A in(1,3,5));C=e(Z(A+fraction*(B-A))for(A,B)in zip(A,B));return'{:02x}{:02x}{:02x}'.format(*C)
def A2(customer_name):
	C='{:06x}';A=customer_name;B='';D=P(A);E=C.format(l.randint(0,16777215));F=C.format(l.randint(0,16777215))
	for(G,H)in d(A):I=G/c(D-1,1);J=A1(E,F,I);B+=f"[{J}]{H}"
	return B
if __name__==q:
	A=u();m.signal(m.SIGINT,y)
	while g:
		o(A);A3=R(h,i,password=Q);A4=R(j,k,password=Q);A5=R('[bold][?] Access Key[bold]','Access Key',password=Q);A.print('[bold cyan][%] Trying to Login[bold cyan]: ',end=J);H=v(A5);X=H.login(A3,A4)
		if X!=0:
			if X==100:A.print('[bold red]ACCOUNT NOT FOUND[bold red].');E(2);continue
			elif X==101:A.print('[bold red]WRONG PASSWORD[bold red].');E(2);continue
			elif X==103:A.print('[bold red]INVALID ACCESS KEY[bold red].');E(2);continue
			else:A.print('[bold red]TRY AGAIN[bold red].');A.print('[bold yellow]! Note[bold yellow]: make sure you filled out the fields !.');E(2);continue
		else:A.print('[bold green]SUCCESSFUL[bold green].');E(2)
		while g:
			o(A);z(H);A0(H);A6=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22'];A.print('[bold red]=============[bold white][ MENU ][bold red]=============[bold white]');A.print('[bold green][01][bold white] Change money [bold yellow]1K[bold white]');A.print('[bold green][02][bold white] Change coins [bold yellow]3.5K[bold white]');A.print('[bold green][03][bold white] King rank max achievement [bold yellow]4k[bold white]');A.print('[bold green][04][bold white] Custom ID [bold yellow]3.5K[bold white]');A.print('[bold green][05][bold white] Change name [bold yellow]100[bold white]');A.print('[bold green][06][bold white] Change rainbow name [bold yellow]100[bold white]');A.print('[bold green][07][bold white] Number plates [bold yellow]2K[bold white]');A.print('[bold green][08][bold white] Delete account [bold yellow]FREE[bold white]');A.print('[bold green][09][bold white] Register account [bold yellow]FREE[bold white]');A.print('[bold green][10][bold white] Delete friends list [bold yellow]500[bold white]');A.print('[bold green][11][bold white] Unlock premium cars [bold yellow]4K[bold white]');A.print('[bold green][12][bold white] Unlock all cars [bold yellow]3K[bold white]');A.print('[bold green][13][bold white] Unlock siren all cars [bold yellow]2K[bold white]');A.print('[bold green][14][bold white] Unlock engine W16 [bold yellow]3K[bold white]');A.print('[bold green][15][bold white] Unlock horns [bold yellow]3K[bold white]');A.print('[bold green][16][bold white] Disable engine damage [bold yellow]2K[bold white]');A.print('[bold green][17][bold white] Unlock unlimited fuel [bold yellow]2K[bold white]');A.print('[bold green][18][bold white] Unlock house [bold yellow]3.5K[bold white]');A.print('[bold green][19][bold white] Unlock smoke [bold yellow]2K[bold white]');A.print('[bold green][20][bold white] Change race win [bold yellow]2K[bold white]');A.print('[bold green][21][bold white] Change race lose [bold yellow]2K[bold white]');A.print('[bold green][22][bold white] Clone account to other account [bold yellow]5K[bold white]');A.print('[bold green][00][bold white] Exit tools[bold white]',end='');A.print('\n[bold red]===================================[bold white]');I=V.ask(f"\n[bold][?] Input menu [01-22]",choices=A6,show_choices=Q)
			if I==0:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
			elif I==1:
				A.print('[bold cyan][!] Input money[bold cyan]');O=V.ask(a);A.print(W,end=J)
				if O>0 and O<=50000000:
					if H.set_player_money(O):
						A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
						if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
						else:continue
					else:A.print(F);A.print(M);E(2);continue
				else:A.print(F);A.print(U);E(2);continue
			elif I==2:
				A.print('[bold cyan][!] Insert input coins.[bold cyan]');O=V.ask(a);A.print(W,end=J)
				if O>0 and O<=90000:
					if H.set_player_coins(O):
						A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
						if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
						else:continue
					else:A.print(F);A.print(M);E(2);continue
				else:A.print(F);A.print(U);E(2);continue
			elif I==3:
				A.print('[bold cyan][%] Instan king rank.[bold cyan]: ',end=J)
				if H.set_player_rank():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==4:
				A.print('[bold cyan][!] Enter your new ID.[bold cyan]');A.print('[bold cyan][!] Min ID 9 Character Max 14[bold cyan]');Y=G.ask('[bold][?] ID[bold]');A.print(W,end=J)
				if P(Y)>=9 and P(Y)<=14 and(' 'in Y)==Q:
					if H.set_player_localid(Y.upper()):
						A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
						if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
						else:continue
					else:A.print(F);A.print(M);E(2);continue
				else:A.print(F);A.print('[bold yellow][!] Please use valid ID.[bold yellow]');E(2);continue
			elif I==5:
				A.print('[bold cyan][!] Enter your new Name.[bold cyan]');S=G.ask(r);A.print(W,end=J)
				if P(S)>=0 and P(S)<=30:
					if H.set_player_name(S):
						A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
						if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
						else:continue
					else:A.print(F);A.print(M);E(2);continue
				else:A.print(F);A.print(U);E(2);continue
			elif I==6:
				A.print('[bold cyan][!] Enter your new Rainbow Name.[bold cyan]');S=G.ask(r);A.print(W,end=J)
				if P(S)>=0 and P(S)<=30:
					if H.set_player_name(A2(S)):
						A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
						if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
						else:continue
					else:A.print(F);A.print(M);E(2);continue
				else:A.print(F);A.print(U);E(2);continue
			elif I==7:
				A.print('[bold cyan][%] Giving you a Number Plates[bold cyan]: ',end=J)
				if H.set_player_plates():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==8:
				A.print('[bold cyan][!] After deleting your account there is no going back !!.[bold cyan]');D=G.ask('[bold cyan][?] Do You want to Delete this Account ?![bold cyan]',choices=[B,C],default=C)
				if D==B:H.delete();A.print('[bold cyan][%] Deleting Your Account[bold cyan]: [bold green]SUCCESSFUL.[bold green].');A.print(K);A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
				else:continue
			elif I==9:
				A.print('[bold cyan][!] Registring new Account.[bold cyan]');A7=R(h,i,password=Q);A8=R(j,k,password=Q);A.print('[bold cyan][%] Creating new Account[bold cyan]: ',end=J);p=H.register(A7,A8)
				if p==0:A.print(L);A.print(K);A.print(f"[bold red]! INFO[bold red]: In order to tweak this account with CyberCPM");A.print('you most sign-in to the game using this account.');E(2);continue
				elif p==105:A.print(F);A.print('[bold yellow][!] This email is already exists !.[bold yellow]');E(2);continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==10:
				A.print('[bold cyan][%] Deleting your Friends[bold cyan]: ',end=J)
				if H.delete_player_friends():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==11:
				A.print('[bold cyan][%] Unlocking All Paid Cars[bold cyan]: ',end=J)
				if H.unlock_paid_cars():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==12:
				A.print('[bold cyan][%] Unlocking All Cars[bold cyan]: ',end=J)
				if H.unlock_all_cars():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==13:
				A.print('[bold cyan][%] Unlocking All Cars Siren[bold cyan]: ',end=J)
				if H.unlock_all_cars_siren():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==14:
				A.print('[bold cyan][%] Unlocking w16 Engine[bold cyan]: ',end=J)
				if H.unlock_w16():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==15:
				A.print('[bold cyan][%] Unlocking All Horns[bold cyan]: ',end=J)
				if H.unlock_horns():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==16:
				A.print('[bold cyan][%] Unlocking Disable Damage[bold cyan]: ',end=J)
				if H.disable_engine_damage():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==17:
				A.print('[bold cyan][%] Unlocking Unlimited Fuel[bold cyan]: ',end=J)
				if H.unlimited_fuel():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==18:
				A.print('[bold cyan][%] Unlocking House 3[bold cyan]: ',end=J)
				if H.unlock_houses():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==19:
				A.print('[bold cyan][%] Unlocking Smoke[bold cyan]: ',end=J)
				if H.unlock_smoke():
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			elif I==20:
				A.print('[bold cyan][!] Input race win.[bold cyan]');A.print(s);O=V.ask(a);A.print(t,end=J)
				if O>0 and O<=1000:
					if H.set_player_wins(O):
						A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
						if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
						else:continue
					else:A.print(F);A.print(M);E(2);continue
				else:A.print(F);A.print(U);E(2);continue
			elif I==21:
				A.print('[bold cyan][!] Input race lose.[bold cyan]');A.print(s);O=V.ask(a);A.print(t,end=J)
				if O>0 and O<=1000:
					if H.set_player_loses(O):
						A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
						if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
						else:continue
					else:A.print(F);A.print(M);E(2);continue
				else:A.print(F);A.print(U);E(2);continue
			elif I==22:
				A.print('[bold cyan]Please Enter Account Detalis[bold cyan]:');A9=R(h,i,password=Q);AA=R(j,k,password=Q);A.print('[bold cyan][%] Cloning your account[bold cyan]: ',end=J)
				if H.account_clone(A9,AA):
					A.print(L);A.print(K);D=G.ask(N,choices=[B,C],default=C)
					if D==B:A.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[bold blue].")
					else:continue
				else:A.print(F);A.print(M);E(2);continue
			else:continue
			break
		break