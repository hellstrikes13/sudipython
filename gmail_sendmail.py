#!/usr/bin/python
import datetime
import smtplib
import sys
import getpass
dt = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
def mailbhai():     
         gmail_user = raw_input('enter your gmail ID')
         gmail_password = getpass.getpass()
         sent_from = gmail_user
         if len(sys.argv) <  2:
             print 'sorry u dint  enter mail receipient'
             sys.exit(2)
         to = [sys.argv[1]]

         subject = 'Relax , NOT A spam MAIL %s'%dt
         body = '''
         this is not a SPAM but just mail send via CLI so chillofy.. !!
         
         '''
         message = 'To: {}\nSubject: {}\n\n{}'.format(to[0],subject, body)
         try:
             server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
             server.ehlo()
             server.login(gmail_user, gmail_password)
             server.sendmail(sent_from, to, message)
             server.close()
             print ('Email sent...!')
         except() as e:
             print ('An Error has occured',e)
mailbhai()
