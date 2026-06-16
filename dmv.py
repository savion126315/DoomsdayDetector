from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.dmv.ca.gov/portal/field-office/sacramento/"

def dmv_wait_times() -> bool:
    page = urlopen(url)
    html = page.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")

    wait_section = soup.find("ul", class_="current-wait-times")
    times = wait_section.find_all("span", class_="p medium")

    apt_wait_time = times[0].text.strip()
    no_apt_wait_time = times[1].text.strip()

    # print("Appointment wait:", apt_wait_time, "minutes")
    # print("No appointment wait:", no_apt_wait_time, "minutes")

    if apt_wait_time and no_apt_wait_time == "0":
        return False
    else:
        return True
    
print(dmv_wait_times())