import os
import glob
import time
from datetime import date
from datetime import timedelta
import subprocess
from pathlib import Path
from sys import exit

CREATE_NO_WINDOW = 0x08000000
subprocess.call("""net use S: /del /y""", creationflags=CREATE_NO_WINDOW)
subprocess.call("""net use S: "\\172.16.87.23\bk_ftp" /user:tscsa\admin Kambio.891 /p:yes""", creationflags=CREATE_NO_WINDOW)

TODAY = str(date.today())
YESTERDAY = str(date.today() - timedelta(days = 1))

ID6_SERVICIOS_TSCCH = (r"\\172.16.87.23\bk_v\BK_SERVICIOS_TSCCH_2\*")
ID30_SERVICIOS_LIMA = (r"\\172.16.87.23\bk_v\SERVICIOS_LIMA\*")

def sqlvalidation(server,idsql,yesterday,today):
    file_list=[]
    for filename in glob.glob(server):
        if ".vbm" not in filename:
            file_list.append(filename)
        else:
            pass

    if len(file_list) != 0:
        latest_file = max(file_list, key=os.path.getctime)
        lastdate = str(time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(latest_file))))
        hour = int(time.strftime("%H",time.localtime(os.path.getmtime(latest_file))))

        print(lastdate)
        print(hour)

        if lastdate == TODAY:
            if hour < 4 and idsql == "6":
                print("EUREKA")
            elif hour < 4 and server == "30":
                print("EUREKA")
        else:
            print("OTRO")

if __name__ == "__main__":
    try:
        sqlvalidation(ID6_SERVICIOS_TSCCH,"6",YESTERDAY, TODAY)
        sqlvalidation(ID30_SERVICIOS_LIMA,"30",YESTERDAY, TODAY)

    except Exception as e:
        print(e)

