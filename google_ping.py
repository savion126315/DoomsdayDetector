import subprocess
import platform

def ping(ip):
    param = "-n"  if platform.system().lower() == "windows" else "-c"

    result = subprocess.run(
        ["ping", param, "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print(result.returncode)

    if result.returncode == 0:
        return True
    else:
        return False


def google_ping() -> bool:
    if ping("8.8.8.8") == True:
        print("Host is up")
        return True
    else:
        print("Host is down")
        return False