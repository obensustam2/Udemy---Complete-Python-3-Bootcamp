import smtplib
import getpass

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()

# email = getpass.getpass('Email: ')
# password = getpass.getpass('Password: ')
email_sender = input('Email Sender: ')
app_password = input('App Password: ')
check0 = smtp_obj.login(email_sender, app_password)
print(check0)

sender = email_sender
receiever = input('E-mail Receiver: ')
subject = input('E-mail Subject: ')
message = input('E-mail Message: ')
msg = 'Subject: '+subject+'\n'+message

check1 = smtp_obj.sendmail(sender, receiever, msg)
print(check1)
check2 = smtp_obj.quit()
print(check2)