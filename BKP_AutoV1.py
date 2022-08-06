import os
import glob
import pyodbc
import time
from datetime import date
from datetime import timedelta
import subprocess


CREATE_NO_WINDOW = 0x08000000
subprocess.call("""net use S: /del /y""", creationflags=CREATE_NO_WINDOW)
subprocess.call("""net use S: "\\172.16.88.10\bk_ftp" /user:tscsa\admin Kambio.891 /p:yes""", creationflags=CREATE_NO_WINDOW)


TODAY = str(date.today())
YESTERDAY = str(date.today() - timedelta(days = 1))


#ID1_SRV001 #ID3_MICRO23 #ID4_OCSINVENTORY #ID5_PCRVILCA #ID8_SRV002 #ID9_PCFACT13
#ID13_SVFACT12 #ID17_TSCDCP002 #ID20_SRVSIGE11 #ID22_SRVSIGE12 #ID23_SORARITZY
ID2_MICRO22 = (r"\\172.16.88.10\bk_v\BK_MICRO22\*")
ID6_SERVICIOS_TSCCH = (r"\\172.16.88.10\bk_v\BK_SERVICIOS_TSCCH\*")
ID7_SRVWEB11 = (r"\\172.16.88.10\bk_v\BK_SRVWEB11\*")
ID10_SVPLANILLA = (r"\\172.16.88.10\bk_v\BK_PLANILLA\*")
ID11_SVPLANILLA_BBDD = (r"\\172.16.88.10\bk_ftp\sql\planilla\*")
ID12_SVFACT11 = (r"\\172.16.88.10\bk_v\BK_SVFACT11\*")
ID14_SVMYSQL = (r"\\172.16.88.10\bk_v\BK_SVMYSQL\*")
ID15_SVMYSQL_BBDD = (r"\\172.16.88.10\bk_ftp\sql\mysql\*")
ID16_TSCDCP001 = (r"\\172.16.88.10\bk_v\BK_TSCDCP001\*")
ID18_SRVAFL = (r"\\172.16.88.10\bk_v\BK_SRVAFL\172.16.87.9\*")
ID19_SOFYA = (r"\\172.16.88.10\bk_ftp\sql\sofya\*")
ID21_SEGURIDAD = (r"\\172.16.88.10\bk_ftp\sql\sige\*")
ID24_FISICO_ARC = (r"\\172.16.88.10\bk_ftp\ora\fis\*")
ID25_FISICO_FULL = (r"\\172.16.88.10\bk_ftp\ora\fis\*")
ID26_LOGICO_USYSTEX = (r"\\172.16.88.10\bk_ftp\ora\log\*")
ID27_LOGICO_SYSTEXTILRPT = (r"\\172.16.88.10\bk_ftp\ora\log\*")
ID28_SRV_SISCONT = (r"\\172.16.88.10\bk_v\BK_SRVSISCONT\172.16.87.5\*")
ID29_SISCONT = (r"\\172.16.88.10\bk_ftp\sql\siscont\*")
ID30_SERVICIOS_LIMA = (r"\\172.16.88.10\bk_v\BK_SERVICIOS_LIMA\192.168.0.5\*")
ID31_DHCP = (r"\\172.16.88.10\bk_ftp\dhcp\*")

def crearconexion():
    global conexion
    direccion_servidor = 'DESKTTSC248\SQLEXPRESS'
    nombre_bd = 'SRV_BACKUP'
    nombre_usuario = 'lvivanco'
    password = '123qweASD!"#'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)

def sqlvalidation(server,idsql,yesterday,today):
    list_of_files = glob.iglob(server)
    latest_file = max(list_of_files, key=os.path.getctime)
    lastdate = str(time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(latest_file))))
    if lastdate == TODAY:
        crearconexion()
        try:
            with conexion.cursor() as cursor:
                consulta = "use SRV_BACKUP update TBL_RECORDS set idstatus = '3', reg_user = 'RPA', reg_date = ? where idserver = ? and bkp_date = ?"
                cursor.execute(consulta, today, idsql, today)
                conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    elif lastdate == YESTERDAY:
        crearconexion()
        try:
            with conexion.cursor() as cursor:
                consulta = "use SRV_BACKUP update TBL_RECORDS set idstatus = '3', reg_user = 'RPA', reg_date = ? where idserver = ? and bkp_date = ?"
                cursor.execute(consulta, today, idsql, yesterday)
                conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    else:
        crearconexion()
        try:
            with conexion.cursor() as cursor:
                consulta = "use SRV_BACKUP update TBL_RECORDS set idstatus = '1', reg_user = 'RPA', reg_date = ? where idserver = ? and bkp_date = ?"
                cursor.execute(consulta, today, idsql, yesterday)
                conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()

if __name__ == "__main__":
    try:
        sqlvalidation(ID2_MICRO22,"2",YESTERDAY, TODAY)
        sqlvalidation(ID6_SERVICIOS_TSCCH,"6",YESTERDAY, TODAY)
        sqlvalidation(ID7_SRVWEB11,"7",YESTERDAY, TODAY)
        sqlvalidation(ID10_SVPLANILLA,"10",YESTERDAY, TODAY)
        sqlvalidation(ID11_SVPLANILLA_BBDD,"11",YESTERDAY, TODAY)
        sqlvalidation(ID12_SVFACT11,"12",YESTERDAY, TODAY)
        sqlvalidation(ID14_SVMYSQL,"14",YESTERDAY, TODAY)
        sqlvalidation(ID15_SVMYSQL_BBDD,"15",YESTERDAY, TODAY)
        sqlvalidation(ID16_TSCDCP001,"16",YESTERDAY, TODAY)
        sqlvalidation(ID18_SRVAFL,"18",YESTERDAY, TODAY)
        sqlvalidation(ID19_SOFYA,"19",YESTERDAY, TODAY)
        sqlvalidation(ID21_SEGURIDAD,"21",YESTERDAY, TODAY)
        sqlvalidation(ID24_FISICO_ARC,"24",YESTERDAY, TODAY)
        sqlvalidation(ID25_FISICO_FULL,"25",YESTERDAY, TODAY)
        sqlvalidation(ID26_LOGICO_USYSTEX,"26",YESTERDAY, TODAY)
        sqlvalidation(ID27_LOGICO_SYSTEXTILRPT,"27",YESTERDAY, TODAY)
        sqlvalidation(ID28_SRV_SISCONT,"28",YESTERDAY, TODAY)
        sqlvalidation(ID29_SISCONT,"29",YESTERDAY, TODAY)
        sqlvalidation(ID30_SERVICIOS_LIMA,"30",YESTERDAY, TODAY)
        sqlvalidation(ID31_DHCP,"31",YESTERDAY, TODAY)

    except Exception as e:
        print(e)