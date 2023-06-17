import datetime as dt
import smtplib
from random import choice
import pandas

my_email = "your email id"
passw = "email passowrd"

with open("./letter_templates/letter_1.txt") as letter:
    letter_1 = letter.read()
with open("./letter_templates/letter_2.txt") as letter:
    letter_2 = letter.read()
with open("./letter_templates/letter_3.txt") as letter:
    letter_3 = letter.read()
letters = [letter_1, letter_2, letter_3]

birthdays = pandas.read_csv("birthdays.csv")

today = dt.datetime.now()
month = today.month
day = today.day

for index, row in birthdays.iterrows():
    if row.month == month and row.day == day:
        letter = choice(letters).replace("[NAME]", row['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=passw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row.email,
                msg=f"Subject: Happy Birthday\n\n{letter}"
            )
