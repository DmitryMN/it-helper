import subprocess

def run_command(command):
    with subprocess.Popen(["powershell", command]) as proc:
        try:
            proc.wait(3)
        except Exception as e:
            proc.terminate()
            proc.wait()
            print(f"script fail {e}")