import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "ahmadtahirmalik04@gmail.com"
MY_PASSWORD = "dslescmgeuqhjiry"

MY_LAT = 43.589046
MY_LNG = -79.644119
formatted = 0


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data1 = response.json()
    iss_longitude = float(data1["iss_position"]["longitude"])
    iss_latitude = float(data1["iss_position"]["latitude"])

    if MY_LNG-5 <= iss_longitude <= MY_LNG+5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        return True


def is_night():

    parameters = {
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json?lat=43.589046&-79.644119", params=parameters)
    response.raise_for_status()
    data2 = response.json()
    sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up 👆!\n\n"
                                                                       "The ISS is above you in the sky 🌓")


