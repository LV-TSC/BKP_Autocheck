import glob
import os
import fnmatch
import logging

path = """\\\\172.16.88.10\\bk_v\\BK_MICRO22\\*"""
path2 = """\\\\172.16.88.10\\bk_v\\BK_MICRO22\\"""
extensions = ('.vib','.vbk')



backup_storage_available = os.path.isdir("\\172.16.88.10\bk_ftp")


if backup_storage_available:
    print("Ok")
else:
    print("vamo a conectar")

    mount_command = "net use /user:" + "tscsa\admin" + " " + "\\172.16.88.10\bk_ftp" + " " + "Kambio.891"
    os.system(mount_command)
    backup_storage_available = os.path.isdir("\\172.16.88.10\bk_ftp")

    if backup_storage_available:
        print("Ok ya estas")
    else:
        raise Exception("Failed to find storage directory.")