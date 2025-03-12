import pathlib
import datetime

PATH_DIRECTORY = r"C:\it-help\log"
#find directory or file
def find_directory(path):
    return pathlib.Path(path).exists()
#get path for logging
def get_path(file_name=''):
    if file_name:
        return pathlib.Path(PATH_DIRECTORY, file_name)
    return pathlib.Path(PATH_DIRECTORY)
#create folder
def create_folder(path):
    try:
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    except IOError as e:
        print(f'{e}')
#create file
def create_empty_file(path):
    try:
        pathlib.Path(path).touch(exist_ok=True)
    except IOError as e:
        print(f'{e}')
#write log
def logging(path_file, command, login, hostname, ip):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    log = f'{current_date};{command};{login};{hostname};{ip} \n'
    with open(path_file, 'a', encoding='utf-8' ,buffering=1) as file:
        file.write(log)