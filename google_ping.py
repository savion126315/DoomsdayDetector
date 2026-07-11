import subprocess
import platform
import test_metrics

def ping(ip):
    param = "-n"  if platform.system().lower() == "windows" else "-c"

    result = subprocess.run(
        ["ping", param, "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        return True
    else:
        return False


def google_ping() -> bool:
    if ping("8.8.8.8") == True:  # Host is up
        test_metrics.record("Google_Ping", "google", True)
        return True
    
    else:
        test_metrics.record("Google_Ping", "google", False)
        return False  # Host is down