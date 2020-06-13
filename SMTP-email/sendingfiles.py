import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

host='smtp.gmail.com'
port=587

email_from = 'emali from'
email_password = 'password'
email_to = 'email to'
email_subject = "Some random names"

message = MIMEMultipart()
message['From'] = email_from
message['To'] = email_to
message['Subject'] = email_subject

plain_text = "This files just have some random names on it"
message.attach(MIMEText(plain_text,'plain'))

filename = 'names.txt'
openfile = open(filename,'rb')

mimref = MIMEBase('application','octect_stream')
mimref.set_payload((openfile.read()))
encoders.encode_base64(mimref)
mimref.add_header('Content-Dispostion','openfile;filename='+filename)

message.attach(mimref)

connection = smtplib.SMTP(host,port)
connection.starttls()
connection.login(email_from,email_password)
connection.sendmail(email_from,email_to,message.as_string())
connection.quit()

