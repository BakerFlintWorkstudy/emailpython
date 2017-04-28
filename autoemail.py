#needed imports
import smtplib
import datetime

#create the smtp server object. If not gmail, llok up your respective email's smtp server and port
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

#begin comminication with a hello command and starting to use tls encryption
smtpObj.ehlo()
smtpObj.starttls()

#login, send, and leave.
smtpObj.login("email addr","pass")
smtpObj.sendmail('sender', 'recipient', 'subject line / msg')
smtpObj.quit()
