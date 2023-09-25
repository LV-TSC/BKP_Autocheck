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

ID2_MICRO22 = (r"\\172.16.87.23\bk_v\BK_MICRO22\*")
ID6_SERVICIOS_TSCCH = (r"\\172.16.87.23\bk_v\BK_SERVICIOS_TSCCH_2\*")
ID7_SRVWEB11 = (r"\\172.16.87.23\bk_v\SRVWEB11\*")
ID11_SVPLANILLA_BBDD = (r"\\172.16.87.16\bktsc11\planilla\*") ##SYNOLOGY##
ID12_SVFACT11 = (r"\\172.16.87.23\bk_v\BK_SVFACT11\*")
ID14_SVMYSQL = (r"\\172.16.87.23\bk_v\BK_SVMYSQL\*")
ID15_SVMYSQL_BBDD = (r"\\172.16.87.16\bktsc11\mysql\*") ##SYNOLOGY##
ID16_TSCDCP001 = (r"\\172.16.87.23\bk_v\BK_TSCDCP001\*")
ID18_SRVAFL = (r"\\172.16.87.23\bk_v\BK_SRVAFL\172.16.87.9\*")
ID19_SOFYA = (r"\\172.16.87.16\bktsc11\sofya\*") ##SYNOLOGY##
ID20_SRVSIGE11 = (r"\\172.16.87.23\bk_v\BK_SRVSIGE11\172.16.87.12\*")
ID21_SEGURIDAD = (r"\\172.16.87.16\bktsc11\sige\*") ##SYNOLOGY##
ID24_FISICO_ARC = (r"\\172.16.87.16\bktsc11\ora_fis\*") ##SYNOLOGY##
ID25_FISICO_FULL = (r"\\172.16.87.16\bktsc11\ora_fis\*") ##SYNOLOGY##
ID26_LOGICO_USYSTEX = (r"\\172.16.87.16\bktsc11\ora_log\*") ##SYNOLOGY##
ID27_LOGICO_SYSTEXTILRPT = (r"\\172.16.87.16\bktsc11\ora_log\*") ##SYNOLOGY##
ID28_SRV_SISCONT = (r"\\172.16.87.23\bk_v\BK_SRVSISCONT\172.16.87.5\*")
ID29_SISCONT = (r"\\172.16.87.16\bktsc11\siscont\*") ##SYNOLOGY##
ID30_SERVICIOS_LIMA = (r"\\172.16.87.23\bk_v\SERVICIOS_LIMA\*")


def calcular_directorio(directorio): return sum([sum([os.path.getsize(rutas+"\\"+archivo) for archivo in archivos]) for rutas, _, archivos in os.walk(directorio)])

def sqlvalidation(server,idsql,yesterday,today):
    file_list=[]
    for filename in glob.glob(server):
        if ".vbm" not in filename:
            file_list.append(filename)
        else:
            pass

    if len(file_list) != 0:
        latest_file = max(file_list, key=os.path.getctime)
        sizefile = os.stat(latest_file).st_size
        size_folder = calcular_directorio(latest_file)
        print(f'Folder : {size_folder}')
        print(f'File : {sizefile}')
        print(f'Last : {latest_file}')
        print('------------------------')
        lastdate = str(time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(latest_file))))
        hour = int(time.strftime("%H",time.localtime(os.path.getmtime(latest_file))))

if __name__ == "__main__":
    try:
        sqlvalidation(ID6_SERVICIOS_TSCCH,"6",YESTERDAY, TODAY)
        sqlvalidation(ID11_SVPLANILLA_BBDD,"11",YESTERDAY, TODAY)
        sqlvalidation(ID15_SVMYSQL_BBDD,"15",YESTERDAY, TODAY)
        sqlvalidation(ID20_SRVSIGE11,"20",YESTERDAY, TODAY)
        sqlvalidation(ID24_FISICO_ARC,"24",YESTERDAY, TODAY)
        sqlvalidation(ID25_FISICO_FULL,"25",YESTERDAY, TODAY)
        sqlvalidation(ID26_LOGICO_USYSTEX,"26",YESTERDAY, TODAY)
        sqlvalidation(ID27_LOGICO_SYSTEXTILRPT,"27",YESTERDAY, TODAY)
        

    except Exception as e:
        print(e)

