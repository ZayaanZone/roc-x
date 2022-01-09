version="2.3.6"
#IMPORT
import getpass,time,os,sys
import signal
import time,os,sys
import sys, random
import threading,time
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
line=yellow+"======================================================================================================================"+end
space=" "
logo=red+str("""
     8888888b.   .d88888b.   .d8888b.       Y88b   d88P
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P
     888    888 888     888 888    888        Y88o88P
     888   d88P 888     888 888        888888  Y888P
     8888888P"  888     888 888        888888  d888b
     888 T88b   888     888 888    888        d88888b
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b""")+end

notice=""
def header():
	print(logo+cyan+"\n\n\n\t\tDeveloped By : Sanaur Asif\n\n"+green+"\t\t     Version : "+str(version)+" \n\n"+end+line+"\n"+end)
def clear():
        os.system("clear || cls")
count=1
erase = '\x1b[1A\x1b[2K'
count=1
about=12

os.system("clear")
header()
print(cyan+"\n\t\t[•] Checking For Updates")
time.sleep(0.7)


try:
	import requests
except:
	os.system("pip install requests")
import requests
r=requests.get('https://pastebin.com/raw/0e7CzUNG')
upchck=r.text
if upchck==version:
	pass
elif upchck!=version:
	os.system("clear")
	header()
	print(cyan+"\n  [°] Installing The Updated Tools. Allow Up to 10 minutes ")
	time.sleep(2)
	os.system("clear")
	notice=cyan+"\t\t[°] Installing Updated Tools.. \n"
	header()
	notice=""
	print("\n")
	clear()
	notice=cyan+"\t\t[•] Backing up the ROC-X...."
	header()
	os.system("mkdir $HOME/roc-x_updater")
	os.system("cp -rf $HOME/roc-x $HOME/roc-x_updater")
	try:
		clear()
		notice=cyan+"\t\t[•] Updating the Tools...."
		header()
		os.system("cd $HOME")
		os.system("cd $HOME && rm -rf roc-x")
		print(green)
		os.system("cd $HOME && git clone https://github.com/RootOfCyber/roc-x")
		
		clear()
		notice=green+"\t\t[√] Update Successful!"
		header()
		#os.kill(os.getppid(), signal.SIGHUP)
		os.system("rm -rf $HOME/roc-x_updater")
		for i in range(99999999999):
			r2=requests.get("https://pastebin.com/raw/6sBnXFV7")
			r=requests.get('https://pastebin.com/raw/0e7CzUNG')
			upchck=r.text

			os.system("clear")
			print(green+"\n"*4+"\t  [✓]  Successfully Updated to ROC-X "+yellow+str(upchck)+green+" !\n\n\n\n"+cyan+"  [•] What's New in Version "+str(upchck)+" ?\n\n")
			rng=r2.text
			exec(rng)
			print(yellow+"\n\n\n [•••] TerMux Restart is Required for The Update. Please Restart Termux For The ROC-X Updated Version")
			a=input()

	except:
		clear()
		notice=red+"\t\t[×] Update Failed!"
		header()
		sjsjstshsb=input(cyan+"\n\n\t     Press Enter to Restore ROC-X")
		os.system("cd $HOME")
		os.system("cd $HOME && mkdir roc-x")
		os.system("cd $HOME && cp -rf $HOME/roc-x_updater/roc-x $HOME")
		os.system("rm -rf $HOME/roc-x_updater")
		os.system("python3 $HOME/roc-x/main.py")
		for i in range(99999999999):
			os.system("clear")
			a=input(cyan+"\n"*10+" [>] Please Exit Termux from Notification Bar. Then Again Open ROC-X Tools By :\n\n "+yellow+"\t [1] Exit Termux\n\t [2] Open Termux"+"\n\t [3] cd $HOME/roc-x"+yellow+"\n\t [4] "+yellow+"python3 main.py\n\n")
		
#Main Page

while count<2:
	clear()
	header()
	notice=""
	print(cyan+"\n==> Select the number of the option that you want to start from below : ")
	print(yellow+"\n  [1] Install ROC-X Package\n\n  [2] TeleGram Kit\n\n  [3] Encrypt/Obfuscate Script\n\n  [4] BD SMS Bomber\n\n  [5] ROC-X Phishing\n\n  [6] Location Hacking \n\n  [7] Kali NetHunter\n\n  [8] MetaSploit FrameWork\n\n  [9] E-Mail Bomber\n\n  [10] DDoS Attacker\n\n  [11] Manage ROC-X Auto Opening\n\n  ["+str(about)+"] Contact Us"+end)
	main_opt=str(input(blue+"\n[>] Select Your Option : "+yellow))
	if main_opt=="1":
		os.system("sh pkgs")
		sys.exit()
	
	elif main_opt=="2":
		os.system("python3 tgkit.py")
	
	elif main_opt=="3":
		os.system("python3 enc.py")

	elif main_opt=="4":
		os.system("python3 bdsms.py")

	elif main_opt=="5":
		os.system("python3 t.py")
	
	elif main_opt=="6":
		os.system("python3 grabloc.py")
	
	elif main_opt=="7":
		os.system("python3 kali.py")

	elif main_opt=="8":
		os.system("python3 ms_opt.py")
	
	elif main_opt=="9":
		os.system("python3 emailtool.py")
		
	elif main_opt=="10":
		os.system("python3 ddos_opt.py")

	elif main_opt=="11":
		os.system("python3 tmxchck.py")
		
	elif main_opt==str(about):
		notice=""
		print(cyan+"\n\n\tYoutube:"+yellow+"\n\n\thttps://www.youtube.com/c/RootOfCyber"+cyan+"\n\n\tFacebook:"+yellow+"\n\n\thttps://www.facebook.com/RootOfCyber"+cyan+"\n\n\tWhat\'s app:"+yellow+"\n\n\tCurrently Unavailable!"+cyan+"\n\n\tTelegram:"+yellow+"\n\n\thttps://t.me/joinchat/G2TQaUpEEKBlOGQ1"+cyan+"\n\n\n\n\tContact Us:"+yellow+"\n\n\trootofcyber@gmail.com"+cyan+"\n\n\n\tDeveloped By "+yellow+"Sanaur Asif"+cyan+"\n\n\tFB:"+yellow+" https://facebook.com/sanaur.asif.72")
		a=input(cyan+"\n\n\t\t[>] Press "+yellow+"Enter"+cyan+" to Continue")
		count=1
	else:
		clear()
		notice=red+"\t\t[×] Wrong Option Entered!"
		count=1
