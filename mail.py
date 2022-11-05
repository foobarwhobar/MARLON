import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import schedule
import time
load_dotenv()

'''Creating an array of emails'''
emails = ['']

'''Environment variables'''
sender = os.environ['FROM']
password = os.environ['PW']

'''Puts your email in the emails array'''
emails[0] = sender

'''Function to send an email with to-email, subject, and message passed in'''
def email(to, subject, message):
    msg = MIMEText(message) #Set up MIME object - Simple text, pass in message - use MIMEMultiPart for attachments
    msg['From'] = sender #Assign sender part of object
    msg['To'] = to #Assign to address 
    msg['Subject'] = subject #Assign subject
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465) #Set up connection
    s.login(sender, password) #Login
    s.sendmail(sender, to, msg.as_string()) #Send the mail
    s.quit() #Terminate session
    print('Should have succesfully sent an email') #Print to console
    
'''Checks every day to see if it is monday at 9:00am, if so, sends a motivational message!'''
def check():
    #Gets the current moment
    now = dt.datetime.now() 
    #Gets date of this current moment as 3 part object day, week, month
    date = now.isocalendar()
    if date.weekday == 1:
        #Open txt file with quotes and select a random one
        with open('quotes.txt') as quotes:
            quotes = quotes.readlines()
            quote = random.choice(quotes)
            subject = 'Monday Motivation!'
    #Trigger email function
    email(sender, subject, quote)
    
'''Schedule for the check function'''
schedule.every().day.at("09:00").do(check)

'''Sets program to indefinitely run - this isn't completely ideal but it works'''
while True:
    schedule.run_pending()
    time.sleep(1)
    
    


    
    