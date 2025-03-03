def add_new_printer(host_name):
    match host_name:
        case "W00-68":
            print("add printer m")
        case "W00-54":
            print("add printer s")
        case _:
            print("default")



t = "w00-6800-4545".upper()
s = t[:6]
print(s)
add_new_printer(s)