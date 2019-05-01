#import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fil = "sampletext.txt"
fp = open(fil, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
print type(msg)
print 'printing msg\n-------------------------------------------------------\n',msg
fp.close()

# me == the sender's email address
# you == the recipient's email address
me = "paav@pavk.com"
you = "blah@blaj.com"
msg['Subject'] = 'The contents of %s' %fil
print msg['From'] = me
print msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
"""
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
"""
