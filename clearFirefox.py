import os
import shutil

def clear_firefox_local():
    try:
        profile_path_local = os.path.join(os.environ['LOCALAPPDATA'], 'Mozilla', 'Firefox', 'Profiles')
        # Find the default profile directory
        profiles = [d for d in os.listdir(profile_path_local) if d.endswith('.default-release')]
        if not profiles:
            raise FileNotFoundError("No default Firefox profile found")
        profile_dir = os.path.join(profile_path_local, profiles[0])
        # Delete thumbnails directory
        cache_dir = os.path.join(profile_dir, 'thumbnails')
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
            print("cleared thumbnails")
        # Delete cache2 directory
        cache_dir = os.path.join(profile_dir, 'cache2')
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
            print("cleared cache2")

    except Exception as e:
        print(f"message: {e}")

def clear_firefox_cookies():
    try:
        # Get profile path
        profile_path_roaming = os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles')
        # Find the default profile directory
        profiles = [d for d in os.listdir(profile_path_roaming) if d.endswith('.default-release')]
        if not profiles:
            raise FileNotFoundError("No default Firefox profile found")
        profile_dir = os.path.join(profile_path_roaming, profiles[0])
        # Delete cookies (cookies.sqlite)
        cookies_file = os.path.join(profile_dir, 'cookies.sqlite')
        if os.path.exists(cookies_file):
            os.remove(cookies_file)
            print("Cleared Cookies")
    except Exception as e:
        print(f"message: {e}")
