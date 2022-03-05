import imaplib
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

email_add = input('Email : ')
app_password = input('App Password: ')
check = M.login(email_add, app_password)
check2 = M.select("inbox")


typ, data = M.search(None, 'SUBJECT "Python Receiving Trial"') # Search the subject
email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)