import time
from datetime import datetime as dt

#host_temp ="hosts"
hosts_path ="C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    print('worktime')
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17):
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    
    else:
        print('funtime')
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0) #replace the cursor back to the start of the txt file 
            for line in content:
                if not any(website in line for website in website_list ):
                    file.write(line)
            
            file.truncate() #remove everything after what is written



    time.sleep(5)

#to execute through the background, need to access the pythonw.exe on installed python in pc
#change file extension to pyw to allow it to run in background
#go to task scheduler and run with highest priv 
#run on startup
#actions create action to start program and point at script
#now will start on start up
