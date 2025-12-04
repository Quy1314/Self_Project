import datetime
import time
hosts_path = "hosts.txt"
redirect = "127.0.0.1"
website = ["dantri.com.vn"]

def WriteSite(hosts_path, redirect, website):
    with open(hosts_path,"r+",encoding="utf-8") as file:
        content = file.read()
        for site in website:
            if site in content:
                print("Đã chặn")
            else: 
                file.write(f"{redirect} {site}\n")
    
def RemoveSite(hosts_path, redirect, website):
    with open(hosts_path,"r+",encoding="utf-8") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any (site in line for site in website):
                file.write(line)
        file.truncate()



while True:
    now = datetime.datetime.now()
    curr_h = int(now.strftime("%H"))
    if 8<=curr_h<16:
        WriteSite(hosts_path, redirect, website)
    else:
        RemoveSite(hosts_path, redirect, website)
    time.sleep(10)