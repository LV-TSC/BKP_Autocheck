import os
import glob
import pyodbc
import time
from datetime import date
from datetime import timedelta
import subprocess
from pathlib import Path
from sys import exit

ID15_SVMYSQL_BBDD = (r"\\172.16.88.10\bk_ftp\sql\mysql")

#files = list(filter(os.path.isfile, os.listdir(ID15_SVMYSQL_BBDD)))

import os

# List all files and directories in the "download" directory
files_and_directories = os.listdir("C:\TSC\Data\Escaner")

# Filter out the directories and keep only the files
files = [f for f in files_and_directories if os.path.isfile(f)]

# Print the list of files
print(files)