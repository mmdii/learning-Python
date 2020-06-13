import socket

host = "localhost"
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print("server is listening for client requst on port",port)
con, adress = s.accept()
print("connection has been estabilashed from ", str(adress))
try :
    fileName = con.recv((1024))
    file = open(fileName,"rb")
    readFile = file.read()
    con.send(readFile)
    file.close() 
    # if you want to send message uncomment this part
    # con.send("hello my name is server !!!".encode())
    con.close()
except:
    con.send("File Not Found on the Server".encode())