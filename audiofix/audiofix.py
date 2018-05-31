import os
import time
import sys
import subprocess


calls = ['net stop audiosrv', 'net start audiosrv']


os.system("net stop audiosrv")
time.sleep(3)
os.system("net start audiosrv")
time.sleep(3)
sys.exit(0)

