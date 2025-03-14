from runCommand import run_command

def add_new_printer(host_name):
    match host_name:
        case "W00-68":
            run_command(r'Start-Process "\\S00-6800-PX01\"')
        case "W00-54":
            run_command(r'Start-Process "\\S00-5400-PX01\"')
        case "W00-05":
            run_command(r'Start-Process "\\S00-0500-PX01\"')
        case "W00-46":
            run_command(r'Start-Process "\\S00-4600-PX01\"')
        case "W00-74":
            run_command(r'Start-Process "\\S00-7400-PX01\"')
        case "W00-47":
            run_command(r'Start-Process "\\S00-4700-PX01\"')
        case "W00-52":
            run_command(r'Start-Process "\\S00-5200-PX01\"')
        case "W00-14":
            run_command(r'Start-Process "\\S00-1400-PX1\"')
        case "W00-77":
            run_command(r'Start-Process "\\S00-7700-PX01\"')
        case "W00-01":
            run_command(r'Start-Process "\\S00-0100-PX01\"')
        case "W00-50":
            run_command(r'Start-Process "\\S00-5000-PX1\"')
        case "W00-13":
            run_command(r'Start-Process "\\S00-1300-PS02\"')
        case "W00-00":
            run_command(r'Start-Process "\\S00-0000-PS01\"')
        case "W00-49":
            run_command(r'Start-Process "\\S00-4900-PX01\"')
        case "W00-36":
            run_command(r'Start-Process "\\S00-3600-PX01\"')
        case "W00-10":
            run_command(r'Start-Process "\\S00-1000-PX01\"')
        case "W00-12":
            run_command(r'Start-Process "\\S00-1200-PX01\"')
        case "W00-59":
            run_command(r'Start-Process "\\S00-5900-PX01\"')
        case "W00-82":
            run_command(r'Start-Process "\\S00-8200-PX01\"')
        case "W00-62":
            run_command(r'Start-Process "\\S00-6200-PX01\"')
        case "W00-45":
            run_command(r'Start-Process "\\S00-4500-PX01\"')
        case "W00-75":
            run_command(r'Start-Process "\\S00-7500-PX01\"')
        case "W00-81":
            run_command(r'Start-Process "\\S00-8100-PX01\"')
        case "W00-04":
            run_command(r'Start-Process "\\S00-0400-PX01\"')
        case "W00-37":
            run_command(r'Start-Process "\\S00-3700-PX01\"')
        case "W00-79":
            run_command(r'Start-Process "\\S00-7900-PX01\"')
        case "W00-64":
            run_command(r'Start-Process "\\S00-6400-PX01\"')
        case "W00-48":
            run_command(r'Start-Process "\\S00-4800-PX01\"')
        case "W00-87":
            run_command(r'Start-Process "\\S00-8700-PX01\"')
        case "W00-92":
            run_command(r'Start-Process "\\S00-9200-PX01\"')
        case "W00-91":
            run_command(r'Start-Process "\\S00-9100-PX01\"')
        case "W00-55":
            run_command(r'Start-Process "\\S00-5500-PX01\"')
        case "W00-26":
            run_command(r'Start-Process "\\S00-2600-PX01\"')
        case "W00-44":
            run_command(r'Start-Process "\\S00-4400-PX01\"')
        case "W00-16":
            run_command(r'Start-Process "\\S00-1600-PX01\"')
        case "W00-39":
            run_command(r'Start-Process "\\S00-3900-PX01\"')
        case "W00-65":
            run_command(r'Start-Process "\\S00-6500-PX01\"')
        case "W00-38":
            run_command(r'Start-Process "\\S00-3800-PX01"')
        case "W00-25":
            run_command(r'Start-Process "\\S00-2500-PX01\"')
        case "W00-29":
            run_command(r'Start-Process "\\S00-2900-PX01\"')
        case "W00-69":
            run_command(r'Start-Process "\\S00-6900-PX01\"')
        case "W00-03":
            run_command(r'Start-Process "\\S00-0300-PX01\"')
        case "W00-61":
            run_command(r'Start-Process "\\S00-6100-PX01\"')
        case "W00-86":
            run_command(r'Start-Process "\\S00-8600-PX1\"')
        case "W00-22":
            run_command(r'Start-Process "\\S00-2200-PX1\"')
        case "W00-66":
            run_command(r'Start-Process "\\S00-6600-PX1\"')
        case "W00-84":
            run_command(r'Start-Process "\\S00-8400-PX01\"')
        case "W00-23":
            run_command(r'Start-Process "\\S00-2300-PX01\"')
        case "W00-60":
            run_command(r'Start-Process "\\S00-6000-PX01\"')
        case "W00-21":
            run_command(r'Start-Process "\\S00-2100-PX01\"')
        case "W00-06":
            run_command(r'Start-Process "\\S00-0600-TS01\"')
        case "W00-07":
            run_command(r'Start-Process "\\S00-0700-PX01\"')
        case "W00-80":
            run_command(r'Start-Process "\\S00-8000-PX1\"')
        case "W00-02":
            run_command(r'Start-Process "\\S00-0200-PX01\"')
        case "W00-19":
            run_command(r'Start-Process "\\S00-1900-PX01\"')
        case "W00-34":
            run_command(r'Start-Process "\\S00-3400-PX01\"')
        case "W00-31":
            run_command(r'Start-Process "\\S00-3100-PX01\"')
        case "W00-85":
            run_command(r'Start-Process "\\S00-8500-PX01\"')
        case "W00-63":
            run_command(r'Start-Process "\\S00-6300-PX01\"')
        case "W00-08":
            run_command(r'Start-Process "\\S00-0800-PX01\"')
        case "W00-24":
            run_command(r'Start-Process "\\S00-2400-PX01\"')
        case "W00-15":
            run_command(r'Start-Process "\\S00-1500-PX01\"')
        case "W00-58":
            run_command(r'Start-Process "\\S00-5800-PX01\"')
        case "W00-27":
            run_command(r'Start-Process "\\S00-2700-AP01\"')
        case "W00-42":
            run_command(r'Start-Process "\\S00-4200-PX01\"')
        case "W00-41":
            run_command(r'Start-Process "\\S00-4100-PX01\"')
        case "W00-71":
            run_command(r'Start-Process "\\S00-7100-PX01\"')
        case "W00-35":
            run_command(r'Start-Process "\\S00-3500-PX01\"')
        case "W00-40":
            run_command(r'Start-Process "\\S00-4000-PX01\"')
        case "W00-57":
            run_command(r'Start-Process "\\S00-5700-PX01\"')
        case "W00-56":
            run_command(r'Start-Process "\\S00-5600-PX01\"')
        case "W00-73":
            run_command(r'Start-Process "\\S00-7300-PX01\"')
        case "W00-72":
            run_command(r'Start-Process "\\S00-7200-PX01\"')
        case "W00-28":
            run_command(r'Start-Process "\\S00-2800-PX01\"')
        case "W00-43":
            run_command(r'Start-Process "\\S00-4300-PX01\"')
        case "W00-70":
            run_command(r'Start-Process "\\S00-7000-PX01\"')
        case "W00-51":
            run_command(r'Start-Process "\\S00-5100-PX01\"')
        case _:
            print("Неопознаный компьютер")

