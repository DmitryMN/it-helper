import os.path
import pathlib
import datetime
import shutil
from typing import List
from const import PATH_PC, PATH_SERVER

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

#create file on server
def create_file_on_server(file_name):
    if find_directory(get_path(PATH_SERVER)):
        if not find_directory(get_path(PATH_SERVER, file_name)):
            create_empty_file(get_path(PATH_SERVER, file_name))

#create file local
def create_file_local(file_name):
    if not find_directory(get_path(PATH_PC)):
        create_folder(get_path(PATH_PC))
        create_empty_file(get_path(PATH_PC, file_name))
    else:
        if not find_directory(get_path(PATH_PC, file_name)):
            create_empty_file(get_path(PATH_PC, file_name))

#create file
def create_empty_file(path):
    try:
        pathlib.Path(path).touch(exist_ok=True)
    except IOError as e:
        print(e)

#write log
def logging(path_file, command, login, hostname, ip):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    log = f'{current_date};{command};{login};{hostname};{ip} \n'
    with open(path_file, 'a', encoding='utf-8', buffering=1) as file:
        file.write(log)

# write log
def write_log(path, command, login, hostname, ip):
    logging(get_path(PATH_PC, path), command, login, hostname, ip)
    if find_directory(get_path(PATH_SERVER, path)):
        logging(get_path(PATH_SERVER, path), command, login, hostname, ip)

#get directory of user
def get_env_path(env_path: str, *args):
    return os.path.join(os.environ[env_path], *args)

#clear directory and files and not remove exclude
def clear_directory(env_path: str, exclude: List[str], *args):
    try:
        profile_path = get_env_path(env_path, *args)
        if find_directory(profile_path):
            for item in os.listdir(profile_path):
                path_item = os.path.join(profile_path, item)
                if item not in exclude:
                    if os.path.isfile(path_item) or os.path.islink(path_item):
                        os.unlink(path_item)
                    elif os.path.isdir(path_item):
                        (shutil.rmtree(path_item))

    except Exception as err:
        print(err)