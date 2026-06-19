import smtplib
import json

def get_config():
    with open('email_config.json') as file:
        config = json.load(file)
    return config


config = get_config()
EMAIL = config.get('email')
PASSWORD = config.get('app_pass')  # App_password


def send_email(recipient_list: list[str], message: str) -> None:
    auth = (EMAIL, PASSWORD)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    for email in recipient_list:
            server.sendmail(auth[0], email, message)
