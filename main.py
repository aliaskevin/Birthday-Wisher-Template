import datetime as dt
import smtplib
from random import choice
import pandas
# fill your email credentials
my_email = "your email id"
passw = "email passowrd"
# Choosing a random letter template
with open("./letter_1.txt") as letter:
    letter_1 = letter.read()
with open("./letter_2.txt") as letter:
    letter_2 = letter.read()
with open("./letter_3.txt") as letter:
    letter_3 = letter.read()
letters = [letter_1, letter_2, letter_3]
# Reading birthdays database
birthdays = pandas.read_csv("birthdays.csv")
# Find the date
today = dt.datetime.now()
month = today.month
day = today.day
# Check if date and month matches for anyone in the list
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
