import smtplib 

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
    connection.sendmail(_from,_to,message)
    connection.quit()
except:
    print("connection error")
