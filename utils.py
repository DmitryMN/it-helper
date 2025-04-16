import pathlib
import datetime

#return home user directory
def get_path_home(path):
    return pathlib.Path.home().joinpath(path)
#return true or false else don't find file or directory
def find_directory(path):
    return pathlib.Path(path).exists()
#get path
def get_path(path, file_name=''):
    if file_name:
        return pathlib.Path(path, file_name)
    return pathlib.Path(path)
#create folder
def create_folder(path):
    try:
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    except IOError as e:
        return 0
#create file
def create_empty_file(path):
    try:
        pathlib.Path(path).touch(exist_ok=True)
    except IOError as e:
        return 0
#write log
def logging(path_file, command, login, hostname, ip):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    log = f'{current_date};{command};{login};{hostname};{ip} \n'
    with open(path_file, 'a', encoding='utf-8', buffering=1) as file:
        file.write(log)