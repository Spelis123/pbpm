from subprocess import check_output

cmd = str(check_output("pacman -Sup",shell=True))[2:]
cmd = cmd.split("\\n")[:-1]
cmd = len(cmd)
s = "" if cmd == 1 else "s"
if cmd == 0:
    print("All up to date!")
else:
    print(f"{cmd} old package{s}")
