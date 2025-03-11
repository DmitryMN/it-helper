import os
import subprocess
import psutil
import win32com.client as win32
import datetime

#create mail
def create_mail(login, to, subject):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = f'{subject} от {login}'
    mail.Display()
#open outlook app
def open_outlook(path):
    try:
        subprocess.run([path])
    except Exception as err:
        print(err)
#search process
def search_process_outlook():
    result = False

    for item in psutil.pids():
        p = psutil.Process(item)
        if p.name() == 'OUTLOOK.EXE':
            result = True

    return  result
#search outlook
def search_outlook(path):
    return os.path.isfile(path)
#send mail
def send_mail(login, to, subject):
    path_64bit = r'C:\Program Files\Microsoft Office\Office16\OUTLOOK.EXE'
    path_32bit = r'C:\Program Files (x86)\Microsoft Office\Office16\OUTLOOK.EXE'
    if search_process_outlook():
        create_mail(login, to, subject)
    else:
        if search_outlook(path_64bit):
            create_mail(login, to, subject)
            open_outlook(path_64bit)
        elif search_outlook(path_32bit):
            create_mail(login, to, subject)
            open_outlook(path_32bit)
        else:
            print('Outlook is absent, install outlook')

def reboot_information():
    last_reboot = psutil.boot_time()
    days = f'{datetime.date.fromtimestamp(last_reboot)}'
    return days