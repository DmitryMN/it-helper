import subprocess


def run_command(self, command):
    with subprocess.Popen(["powershell", command]) as proc:
        try:
            proc.wait(3)
            print("run script")
        except:
            proc.terminate()
            proc.wait()

def add_new_printer(host_name):
    match host_name:
        case "W00-68":
            pass
        case "W00-54":
            pass
        case "W00-05":
            pass
        case "W00-46":
            pass
        case "W00-74":
            pass
        case "W00-47":
            pass
        case "W00-52":
            pass
        case "W00-14":
            pass
        case "W00-77":
            pass
        case "W00-01":
            pass
        case "W00-50":
            pass
        case "W00-13":
            pass
        case "W00-00":
            pass
        case "W00-49":
            pass
        case "W00-36":
            pass
        case "W00-10":
            pass
        case "W00-12":
            pass
        case "W00-59":
            pass
        case "W00-82":
            pass
        case "W00-62":
            pass
        case "W00-45":
            pass
        case "W00-75":
            pass
        case "W00-81":
            pass
        case "W00-04":
            pass
        case "W00-37":
            pass
        case "W00-79":
            pass
        case "W00-64":
            pass
        case "W00-48":
            pass
        case "W00-87":
            pass
        case "W00-92":
            pass
        case "W00-91":
            pass
        case "W00-55":
            pass
        case "W00-26":
            pass
        case "W00-44":
            pass
        case "W00-16":
            pass
        case "W00-39":
            pass
        case "W00-65":
            pass
        case "W00-38":
            pass
        case "W00-25":
            pass
        case "W00-29":
            pass
        case "W00-69":
            pass
        case "W00-03":
            pass
        case "W00-61":
            pass
        case "W00-86":
            pass
        case "W00-22":
            pass
        case "W00-66":
            pass
        case "W00-84":
            pass
        case "W00-23":
            pass
        case "W00-60":
            pass
        case "W00-21":
            pass
        case "W00-06":
            pass
        case "W00-07":
            pass
        case "W00-80":
            pass
        case "W00-02":
            pass
        case "W00-19":
            pass
        case "W00-34":
            pass
        case "W00-31":
            pass
        case "W00-85":
            pass
        case "W00-63":
            pass
        case "W00-08":
            pass
        case "W00-24":
            pass
        case "W00-15":
            pass
        case "W00-58":
            pass
        case "W00-27":
            pass
        case "W00-42":
            pass
        case "W00-41":
            pass
        case "W00-71":
            pass
        case "W00-35":
            pass
        case "W00-40":
            pass
        case "W00-57":
            pass
        case "W00-56":
            pass
        case "W00-73":
            pass
        case "W00-72":
            pass
        case "W00-28":
            pass
        case "W00-43":
            pass
        case "W00-70":
            pass
        case "W00-51":
            pass
