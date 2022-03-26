import smtplib
import datetime as dt
import random 

now = dt.datetime.now()
#Tapping into Todays Data
day_of_week = now.weekday()
# Weekday = 0 for Sunday and so on....
#print(day_of_week)

if day_of_week == 1:
  with open ("quotes.txt") as file:
    all_quote = file.readlines()
    quote = random.choice(all_quote)
    print(quote)

my_email = "javedmomin99999@gmail.com"
password = "testing@123!"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,
to_addrs="javedmomin99@gmail.com",
msg=f"Subject : Monday Motivational Quote! \n\n {quote}")
connection.close()
