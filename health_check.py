#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
import emails

# define varaibles of throhold
cpu_min_available_perc = 20
disk_min_available_perc = 20
memory_min_available_mb = 500
localhost_ip = "127.0.0.1"

# define the checking functions for above requests throholds
def check_cpu_available():
    """Check CPU available capacity"""
    cpu_available = 100 - psutil.cpu_percent(1)
    return cpu_available > cpu_min_available_perc

def check_disk_available(disk)
    """Check the appointed disk's available capacity"""
    disk_free = shutil.disk_usage(disk).free
    disk_total = shutil.disk_usage(disk).total
    disk_available = disk_free / disk_total * 100
    return disk_available > disk_min_available_perc

def check_memory_available():
    """Check available memory"""
    memory_available = psutil.virtual_memory().available/(1024*1024)
    return memory_available > memory_min_available_mb

def check_localhost():
    """Check localhost is configured on 127.0.0.1"""
    localhost = socket.gethostbyname("localhost")
    return localhost == locathost_ip

# setup error message for each functions
if not check_cpu_available():
    error_msg = "CPU usage is over 80%"

elif not check_disk_available():
    error_msg = "Available dis space is less than 20%"

elif not check_memory_available():
    error_msg = "Availbale memory is less than 500MB"
    
elif not check_localhost():
    error_msg = "localhost is not 127.0.0.1"

else:
    pass

# if error happened, then send an reported email
if __name__ == "__main__":
    try:
        sender = "automation@example.com"
        receiver = "<studentuser>@example.com"
        subject = "Error - {}".format(error_msg)
        body = "Please check your system and resolve the issue as soon as possible"
        alert = generate_report(sender, receiver, subject, body, attachment = None)
        send_email(alert)
    except NameError:
        pass