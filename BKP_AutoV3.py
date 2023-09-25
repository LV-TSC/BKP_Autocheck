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

#####QUITAR VENTANA CMD#####
CREATE_NO_WINDOW = 0x08000000
subprocess.call("""net use n: /del /i""", creationflags=CREATE_NO_WINDOW)
subprocess.call("""net use n: "\\172.16.87.23\bk_v" /user:admin Kambio.891 /p:yes""", creationflags=CREATE_NO_WINDOW)

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
#ID1_SRV001 #ID3_MICRO23 #ID4_OCSINVENTORY #ID5_PCRVILCA #ID8_SRV002 #ID9_PCFACT13 #ID10_SVPLANILLA
#ID13_SVFACT12 #ID17_TSCDCP002 #ID22_SRVSIGE12 #ID23_SORARITZY #ID31_DHCP
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

#####FUNCIONES#####
def crearconexion():
    global conexion
    direccion_servidor = 'SRVAFL'
    nombre_bd = 'SRV_BACKUP'
    nombre_usuario = 'RPA'
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
        if ".vbm" not in filename:
            file_list.append(filename)

    if len(file_list) != 0:
        latest_file = max(file_list, key=os.path.getctime)

        sizefile = os.stat(latest_file).st_size
        size_folder = calc_size_folder(latest_file)

        lastsize = 0
        if sizefile > size_folder:
            lastsize = sizefile
        else :
            lastsize = size_folder

        lastdate = str(time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(latest_file))))
        hour = int(time.strftime("%H",time.localtime(os.path.getmtime(latest_file))))

        if lastdate == TODAY and lastsize > 100:
            crearconexion()
            if hour <= 2 and idsql == "30" or hour <= 4 and idsql == "6" or hour <= 1:
                S = "AYER"
                try:
                    with conexion.cursor() as cursor:
                        consulta = "use SRV_BACKUP update TBL_RECORDS set idstatus = '3', reg_user = 'RPA', reg_date = convert(date,?) where idserver = ? and bkp_date = convert(date,?)"
                        cursor.execute(consulta, today, idsql, yesterday)
                        conexion.commit()
                except Exception as e:
                    print(e)
                finally:
                    conexion.close()

            else:
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

        elif lastdate == YESTERDAY and lastsize > 100:
            S = "AYER"
            crearconexion()
            try:
                with conexion.cursor() as cursor:
                    consulta = "use SRV_BACKUP update TBL_RECORDS set idstatus = '3', reg_user = 'RPA', reg_date = convert(date,?) where idserver = ? and bkp_date = convert(date,?)"
                    cursor.execute(consulta, today, idsql, yesterday)
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

        #print(f'Size : {lastsize}')
        #print(f'Last : {latest_file}')
        #print(f"-{S}- Fecha: {lastdate}, Hora: {hour}, Server: {server}")
        #print('---------------------------------------------------------------')

if __name__ == "__main__":
    try:
        sqlvalidation(ID2_MICRO22,"2",YESTERDAY, TODAY)
        sqlvalidation(ID6_SERVICIOS_TSCCH,"6",YESTERDAY, TODAY)
        sqlvalidation(ID7_SRVWEB11,"7",YESTERDAY, TODAY)
        sqlvalidation(ID11_SVPLANILLA_BBDD,"11",YESTERDAY, TODAY)
        sqlvalidation(ID12_SVFACT11,"12",YESTERDAY, TODAY)
        sqlvalidation(ID14_SVMYSQL,"14",YESTERDAY, TODAY)
        sqlvalidation(ID15_SVMYSQL_BBDD,"15",YESTERDAY, TODAY)
        sqlvalidation(ID16_TSCDCP001,"16",YESTERDAY, TODAY)
        sqlvalidation(ID18_SRVAFL,"18",YESTERDAY, TODAY)
        sqlvalidation(ID19_SOFYA,"19",YESTERDAY, TODAY)
        sqlvalidation(ID20_SRVSIGE11,"20",YESTERDAY, TODAY)
        sqlvalidation(ID21_SEGURIDAD,"21",YESTERDAY, TODAY)
        sqlvalidation(ID24_FISICO_ARC,"24",YESTERDAY, TODAY)
        sqlvalidation(ID25_FISICO_FULL,"25",YESTERDAY, TODAY)
        sqlvalidation(ID26_LOGICO_USYSTEX,"26",YESTERDAY, TODAY)
        sqlvalidation(ID27_LOGICO_SYSTEXTILRPT,"27",YESTERDAY, TODAY)
        sqlvalidation(ID28_SRV_SISCONT,"28",YESTERDAY, TODAY)
        sqlvalidation(ID29_SISCONT,"29",YESTERDAY, TODAY)
        sqlvalidation(ID30_SERVICIOS_LIMA,"30",YESTERDAY, TODAY)

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
        