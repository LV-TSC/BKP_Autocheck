import subprocess
subprocess.call(r'net use S: /del', shell=True)
subprocess.call(r'net use S: "\\172.16.88.10\bk_ftp" /user:tscsa\admin Kambio.891 /p:yes', shell=True)