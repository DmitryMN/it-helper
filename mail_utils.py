import os
import subprocess
import psutil
import win32com.client as win32

#create mail
def create_mail(login, to):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = f'Сброс 2 фактора от {login}'
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

def send_mail(login, to):
    path_64bit = r'C:\Program Files\Microsoft Office\Office16\OUTLOOK.EXE'
    path_32bit = r'C:\Program Files (x86)\Microsoft Office\Office16\OUTLOOK.EXE'
    print(f'Send mail {login}')
    if search_process_outlook():
        create_mail(login, to)
    else:
        if search_outlook(path_64bit):
            create_mail(login, to)
            open_outlook(path_64bit)
        elif search_outlook(path_32bit):
            create_mail(login, to)
            open_outlook(path_32bit)
        else:
            print('Outlook is absent, install outlook')
