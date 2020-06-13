import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host='smtp.gmail.com'
port=587

message = "hey this is how i learn python"

userName='test.mmdii@gmail.com'
password='0019786409'

_from = userName
_to = userName

try:
    connection = smtplib.SMTP(host,port)
    print("connection successful")
    connection.ehlo()
    connection.starttls()
    connection.login(userName,password)
    

    tmessage = MIMEMultipart("alternative")
    tmessage['Subject'] = "HTML message"
    tmessage['From'] = _from
    tmessage['To'] = _to

    html_message = """<html><body><h1>this should be header</h1><p>this is a paragraph and i hope it works</p></body></html>"""
    msg = MIMEText(html_message,'html')
    tmessage.attach(msg)

    connection.sendmail(_from,_to,tmessage.as_string())
    connection.quit()
except:
    print("connection error")
