import os
import shutil
from utils import get_env_path
from const import PATH_LOCAL, PATH_ROAMING

#get profiles firefox
def get_firefox_profiles(env_path: str):
    profile_path = get_env_path(env_path, 'Mozilla', 'Firefox', 'Profiles')
    return [profile for profile in os.listdir(profile_path) if not profile.endswith('.default')]

def clear_firefox_local():
    try:
        # get profiles name
        profiles = get_firefox_profiles(PATH_LOCAL)
        if profiles:
            for profile in profiles:
                profile_dir = get_env_path(PATH_LOCAL, 'Mozilla', 'Firefox', 'Profiles', profile)
                for dir_name in ['thumbnails', 'cache2']:
                    cash_path = os.path.join(profile_dir, dir_name)
                    if os.path.exists(cash_path):
                        shutil.rmtree(cash_path)

    except Exception as err:
        pass

def clear_firefox_cookies():
    try:
        profiles = get_firefox_profiles(PATH_ROAMING)
        for profile in profiles:
            profile_dir = get_env_path(PATH_ROAMING, 'Mozilla', 'Firefox', 'Profiles', profile)
            cookies_file = os.path.join(profile_dir, 'cookies.sqlite')
            if os.path.exists(cookies_file):
                os.remove(cookies_file)

    except Exception as err:
        pass

