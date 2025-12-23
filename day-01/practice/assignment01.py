#Takes threshold values (CPU, disk, memory) from user input
#Also fetches system metrics using a Python library (example: psutil)
#Compares metrics against thresholds
#Prints the result to the terminal

import psutil
cpu_threshold = int(input("enter the cpu threshold limit:"))
disk_threshold = int(input("enter the disk threshold limit:"))
memory_threshold = int(input("enter the memory threshold limit:"))

def check_cpu_threshold ():
     current_cpu = psutil.cpu_percent(interval=1)
     if current_cpu > cpu_threshold:
          print("threshold limit excedded email sent ")
     else:
         print ("threshold limit excedded")

def check_disk_threshold ():
     current_disk = psutil.disk_usage('/').percent
     if current_disk > disk_threshold:
          print("threshold limit excedded email sent ")
     else:
         print ("threshold limit excedded")

def check_memory_threshold ():
     current_memory = psutil.virtual_memory().percent
     if current_memory > memory_threshold:
          print("threshold limit excedded email sent ")
     else:
         print ("threshold limit excedded")

check_cpu_threshold()
check_disk_threshold()
check_memory_threshold()
