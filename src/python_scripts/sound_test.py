import subprocess
import time
import os

subprocess.Popen("paplay --process-time-msec=1000 Kodo_long.wav", shell=True)
time.sleep(0.92)
os.system("pkill paplay")
