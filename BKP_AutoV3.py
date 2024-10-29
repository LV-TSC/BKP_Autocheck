#####LIBRERIAS NECESARIAS#####
import os
import glob
import pyodbc
import time
from datetime import date
from datetime import timedelta
import subprocess
from pathlib import Path
from sys import exit
from termcolor import colored

#####QUITAR VENTANA CMD#####
CREATE_NO_WINDOW = 0x08000000
subprocess.call("""net use n: /del /i""", creationflags=CREATE_NO_WINDOW)
subprocess.call("""net use n: "\\172.16.47.15\bk_v" /user:admin Kambio.891 /p:yes""", creationflags=CREATE_NO_WINDOW)

CREATE_NO_WINDOW = 0x08000000
subprocess.call("""net use m: /del /i""", creationflags=CREATE_NO_WINDOW)
subprocess.call("""net use m: "\\172.16.87.16\bktsc11" /user:user11 Xtr3m4.@22 /p:yes""", creationflags=CREATE_NO_WINDOW)

#####RUTA PARA ELIMINAR .FILE#####
home_dir = Path.home()
deletefiles = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\TI-Soporte e Infraestructura - Controles\\Backup')
extensions = ('.pdf','.PDF','.docx','.DOCX','.png','.jpg')

#####OBTENER FECHAS#####
TODAY = str(date.today())
YESTERDAY = str(date.today() - timedelta(days = 1))

#####SERVIDORES#####
#ID1_SRV001 #ID2_MICRO22 #ID3_MICRO23 #ID4_OCSINVENTORY #ID5_PCRVILCA #ID8_SRV002 #ID9_PCFACT13 #ID10_SVPLANILLA
#ID11_SVPLANILLA_BBDD #ID12_SVFACT11 #ID13_SVFACT12 #ID14_SVMYSQL #ID15_SVMYSQL_BBDD #ID17_TSCDCP002 #ID18_SRVAFL
#ID20_SRVSIGE11 #ID22_SRVSIGE12 #ID23_SORARITZY #ID28_SRV_SISCONT #ID31_DHCP


ID6_SERVICIOS_TSCCH = (r"\\172.16.87.16\bkfil11\CH\*") ##SYNOLOGY##
ID7_SRVWEB11 = (r"\\172.16.87.16\bkfil11\SRVWEB11\*") ##SYNOLOGY##
ID16_TSCDCP001 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_TSCDCP001\*") ##SYNOLOGY##
ID19_SOFYA = (r"\\172.16.87.16\bktsc11\sofya\*") ##SYNOLOGY##
ID21_SIGE11 = (r"\\172.16.87.16\bktsc11\sige\*") ##SYNOLOGY##
ID24_FISICO_ARC = (r"\\172.16.87.16\bktsc11\ora_fis\*") ##SYNOLOGY##
ID25_FISICO_FULL = (r"\\172.16.87.16\bktsc11\ora_fis\*") ##SYNOLOGY##
ID26_LOGICO_USYSTEX = (r"\\172.16.87.16\bktsc11\ora_log\*") ##SYNOLOGY##
ID27_LOGICO_SYSTEXTILRPT = (r"\\172.16.87.16\bktsc11\ora_log\*") ##SYNOLOGY##
ID29_SISCONT = (r"\\172.16.87.16\bktsc11\siscont\*") ##SYNOLOGY##
ID30_SERVICIOS_LIMA = (r"\\172.16.87.16\bkfil11\LI\*") ##SYNOLOGY##
ID38_BDORACLE11 = (r"\\172.16.87.16\bktsc11\bd_ora\*") ##SYNOLOGY##

#### NUBE SYNOLOGY
ID47_NUBE_BDORACLE = (r"\\172.16.87.16\bknube\bd_ora\*") ##SYNOLOGY##
ID48_NUBE_SIGE11 = (r"\\172.16.87.16\bknube\sige\*") ##SYNOLOGY##
ID49_NUBE_SOFYA = (r"\\172.16.87.16\bknube\sofya\*") ##SYNOLOGY##
ID50_NUBE_SISCONT = (r"\\172.16.87.16\bknube\siscont\*") ##SYNOLOGY##
ID51_NUBE_ORAFIS = (r"\\172.16.87.16\bknube\ora_fis\*") ##SYNOLOGY##
ID52_NUBE_ORALOG = (r"\\172.16.87.16\bknube\ora_log\*") ##SYNOLOGY##

#### SERVIDORES FISICOS Y VIRTUALES
ID02_MICRO22 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_MICRO22\*") ##SYNOLOGY##
ID04_OCSINVENTORY = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_OCSINVENTORY\*") ##SYNOLOGY##
ID05_PCRVILCA = (r"\\172.16.87.16\servers_fisicos\ActiveBackupData\PC-VIRTU0001JC-user11-Default\*") ##SYNOLOGY##
ID12_SVFACT11 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SVFACT11\*") ##SYNOLOGY##
ID13_SVFACT12 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SVFACT12\*") ##SYNOLOGY##
ID17_TSCDCP002 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_TSCDCP002\*") ##SYNOLOGY##
ID18_SRVAFL = (r"\\172.16.87.16\servers_fisicos\ActiveBackupData\Server-SRVAFL-user11-BKP_SRV\*") ##SYNOLOGY##
ID20_SRVSIGE11 = (r"\\172.16.87.16\servers_fisicos\ActiveBackupData\Server-SRVSIGE11-user11-BKP_SRV\*") ##SYNOLOGY##
ID22_SRVSIGE12 = (r"\\172.16.87.16\servers_fisicos\ActiveBackupData\Server-SRVSIGE12-user11-BKP_SRV\*") ##SYNOLOGY##
ID28_SRV_SISCONT = (r"\\172.16.87.16\servers_fisicos\ActiveBackupData\Server-SRVSISCONT-user11-BKP_SRV\*") ##SYNOLOGY##
ID33_SRV_SERVICIOS_TSCCH = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SERVICIOS_TSCCH\*") ##SYNOLOGY##
ID35_SRV_WEB11 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SRVWEB11\*") ##SYNOLOGY##
ID36_SRV_SERVICIOS_LIMA = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SERVICIOS_LIMA\*") ##SYNOLOGY##
ID39_SRVNAGIOS11 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SRVNAGIOS11\*") ##SYNOLOGY##
ID40_SRVCACTI11 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SRVCACTI11\*") ##SYNOLOGY##
ID41_SRVBDORA11 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SRVBDORA11\*") ##SYNOLOGY##
ID42_SRVUNIFI11 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SRVUNIFI11\*") ##SYNOLOGY##
ID43_SRVSIGE13 = (r"\\172.16.87.16\servers_fisicos\ActiveBackupData\Server-SRVSIGE13-user11-BKP_SRV\*") ##SYNOLOGY##
ID44_SRVWSUS11 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SRVWSUS11\*") ##SYNOLOGY##
ID45_SRVPRINTER11 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SRVPRINTER11\*") ##SYNOLOGY##
ID46_SRVPRINTER12 = (r"\\172.16.87.16\bkvir11\ActiveBackupData\VM-BK_SRVPRINTER12\*") ##SYNOLOGY##

#####FUNCIONES#####
def crearconexion():
    global conexion
    direccion_servidor = 'SRVAFL'
    nombre_bd = 'SRV_BACKUP'
    nombre_usuario = 'SRV_BKP'
    password = '123qweASD!"#'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)

def calc_size_folder(directorio): return sum([sum([os.path.getsize(rutas+"\\"+archivo) for archivo in archivos]) for rutas, _, archivos in os.walk(directorio)])

def sqlvalidation(server,idsql,yesterday,today):
    file_list=[]
    for filename in glob.glob(server):
        if ".json" not in filename and "target.db" not in filename and "fs-config" not in filename:
            file_list.append(filename)

    #Valida si existe el Backup y obtiene el ultimo archivo
    if len(file_list) != 0:
        latest_file = max(file_list, key=os.path.getctime)

        #Obtiene el tamaño del ultimo archivo
        sizefile = os.stat(latest_file).st_size
        size_folder = calc_size_folder(latest_file)

        lastsize = 0
        if sizefile > size_folder:
            lastsize = sizefile
        else :
            lastsize = size_folder

        #Obtine la fecha del ultimo archivo
        lastdate = str(time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(latest_file))))
        hour = int(time.strftime("%H",time.localtime(os.path.getmtime(latest_file))))

        if lastdate == TODAY and lastsize > 100: 
            crearconexion()
            S = "HOY"
            try:
                with conexion.cursor() as cursor:
                    consulta = "use SRV_BACKUP update TBL_RECORDS set idstatus = '3', reg_user = 'RPA', reg_date = convert(date,?) where idserver = ? and bkp_date = convert(date,?)"
                    cursor.execute(consulta, today, idsql, today)
                    conexion.commit()
            except Exception as e:
                print(e)
            finally:
                conexion.close()

        else:
            S = "NOP"
            crearconexion()
            try:
                with conexion.cursor() as cursor:
                    consulta = "use SRV_BACKUP update TBL_RECORDS set idstatus = '1', reg_user = 'RPA', reg_date = convert(date,?) where idserver = ? and idstatus = '2' and bkp_date = convert(date,?)"
                    cursor.execute(consulta, today, idsql, yesterday)
                    conexion.commit()
            except Exception as e:
                print(e)
            finally:
                conexion.close()

        # if S == "HOY":
        #    print(colored(f'Server: {server}  -  Size : {lastsize}', 'green'))
        #    print(colored(f'Last : {latest_file}', 'green'))
        #    print(colored(f'-{S}- Fecha: {lastdate}, Hora: {hour}, Server: {server}','green'))
        # else:
        #    print(colored(f'Server: {server}  -  Size : {lastsize}', 'red'))
        #    print(colored(f'Last : {latest_file}', 'red'))
        #    print(colored(f'-{S}- Fecha: {lastdate}, Hora: {hour}, Server: {server}','red'))
        # print('---------------------------------------------------------------')

if __name__ == "__main__":
    try:
        sqlvalidation(ID6_SERVICIOS_TSCCH,"6",YESTERDAY, TODAY)
        sqlvalidation(ID7_SRVWEB11,"7",YESTERDAY, TODAY)
        sqlvalidation(ID16_TSCDCP001,"16",YESTERDAY, TODAY)
        sqlvalidation(ID19_SOFYA,"19",YESTERDAY, TODAY)
        sqlvalidation(ID21_SIGE11,"21",YESTERDAY, TODAY)
        sqlvalidation(ID24_FISICO_ARC,"24",YESTERDAY, TODAY)
        sqlvalidation(ID25_FISICO_FULL,"25",YESTERDAY, TODAY)
        sqlvalidation(ID26_LOGICO_USYSTEX,"26",YESTERDAY, TODAY)
        sqlvalidation(ID27_LOGICO_SYSTEXTILRPT,"27",YESTERDAY, TODAY)
        sqlvalidation(ID29_SISCONT,"29",YESTERDAY, TODAY)
        sqlvalidation(ID30_SERVICIOS_LIMA,"30",YESTERDAY, TODAY)
        sqlvalidation(ID38_BDORACLE11,"38",YESTERDAY, TODAY)
        sqlvalidation(ID47_NUBE_BDORACLE,"47",YESTERDAY, TODAY)
        sqlvalidation(ID48_NUBE_SIGE11,"48",YESTERDAY, TODAY)
        sqlvalidation(ID49_NUBE_SOFYA,"49",YESTERDAY, TODAY)
        sqlvalidation(ID50_NUBE_SISCONT,"50",YESTERDAY, TODAY)
        sqlvalidation(ID51_NUBE_ORAFIS,"51",YESTERDAY, TODAY)
        sqlvalidation(ID52_NUBE_ORALOG,"52",YESTERDAY, TODAY)

        ###SERVERS
        sqlvalidation(ID02_MICRO22,"02",YESTERDAY, TODAY)
        sqlvalidation(ID04_OCSINVENTORY,"04",YESTERDAY, TODAY)
        sqlvalidation(ID05_PCRVILCA,"05",YESTERDAY, TODAY)
        sqlvalidation(ID12_SVFACT11,"12",YESTERDAY, TODAY)
        sqlvalidation(ID13_SVFACT12,"13",YESTERDAY, TODAY)
        sqlvalidation(ID17_TSCDCP002,"17",YESTERDAY, TODAY)
        sqlvalidation(ID18_SRVAFL,"18",YESTERDAY, TODAY)
        sqlvalidation(ID20_SRVSIGE11,"20",YESTERDAY, TODAY)
        sqlvalidation(ID22_SRVSIGE12,"22",YESTERDAY, TODAY)
        sqlvalidation(ID28_SRV_SISCONT,"28",YESTERDAY, TODAY)
        sqlvalidation(ID33_SRV_SERVICIOS_TSCCH,"33",YESTERDAY, TODAY)
        sqlvalidation(ID35_SRV_WEB11,"35",YESTERDAY, TODAY)
        sqlvalidation(ID36_SRV_SERVICIOS_LIMA,"36",YESTERDAY, TODAY)
        sqlvalidation(ID39_SRVNAGIOS11,"39",YESTERDAY, TODAY)
        sqlvalidation(ID40_SRVCACTI11,"40",YESTERDAY, TODAY)
        sqlvalidation(ID41_SRVBDORA11,"41",YESTERDAY, TODAY)
        sqlvalidation(ID42_SRVUNIFI11,"42",YESTERDAY, TODAY)
        sqlvalidation(ID43_SRVSIGE13,"43",YESTERDAY, TODAY)
        sqlvalidation(ID44_SRVWSUS11,"44",YESTERDAY, TODAY)
        sqlvalidation(ID45_SRVPRINTER11,"45",YESTERDAY, TODAY)
        sqlvalidation(ID46_SRVPRINTER12,"46",YESTERDAY, TODAY)


        for file in os.listdir(deletefiles):
            if os.path.isfile(str(deletefiles) + "\\" + str(file)):
                if not(file.endswith(extensions)):
                    os.remove(str(deletefiles) + "\\" + str(file))

        crearconexion()
        with conexion.cursor() as cursor:
            consulta = "use SRV_BACKUP update TBL_RECORDS set idstatus = 1, reg_user = 'RPA', reg_date = convert(date,?) where bkp_date != convert(date,?) and idstatus = 2"
            cursor.execute(consulta,TODAY,TODAY)
            conexion.commit()

    except Exception as e:
        print(e)

    finally:
        conexion.close()
        exit()
        