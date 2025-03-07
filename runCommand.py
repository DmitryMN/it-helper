import subprocess
from PySide6.QtCore import QTimer

def run_command(command):
    with subprocess.Popen(["powershell", command], creationflags=0x08000000) as proc:
        try:
            proc.wait(3)
        except Exception as e:
            proc.terminate()
            proc.wait()
            print(f"script fail {e}")

def run_lazy_command(command, time=2000):
    QTimer.singleShot(time, lambda: run_command(command))