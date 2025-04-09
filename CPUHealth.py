import psutil
import time

CPU_THRESHOLD=80 #Set thethreshold value for CPU usage 

def monitor_CPU_Usage():
    try:
        cpu_usage=psutil.cpu_percent(interval=1)
        if(cpu_usage>CPU_THRESHOLD):
            print("Alert, CPU usage is more than 80%")
        else:
            print("CPU Usage is normal",cpu_usage)

        time.sleep(1) #Added delay to run after every two seconds
        monitor_CPU_Usage() # added this method call here to call in Recursive way  
   
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.") #added exception to stop the code runnign by pressing ctrl+c

monitor_CPU_Usage()


