import webbrowser
import time
import os
import subprocess
from datetime import datetime
from win10toast import ToastNotifier

def sendNotificationOnWindows(msg="", delay=5):
    t = 0
    notify = ToastNotifier()
    while t < delay:
        notify.show_toast("Notification", msg)
        time.sleep(1)
        t+=1

def continueDay():
    cont = input("Press to continue")

sendNotificationOnWindows("Practice some math bitch")
webbrowser.open("https://projecteuler.net/archives")
continueDay()

