
import datetime
import random
import pandas as pd
import smtplib

email_addr = ""
passwd = ""

x = datetime.datetime.now()
today_month = x.month
today_day = x.day

today = (today_month,today_day)

df_bd = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in df_bd.iterrows()}

if today in birthday_dict:
    bday_person = birthday_dict[today]
    path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(path) as f:
        contents = f.read()
        contents = contents.replace("[NAME]",bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email_addr, passwd)
        connection.sendmail(
            from_addr=email_addr,
            to_addrs=bday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )



