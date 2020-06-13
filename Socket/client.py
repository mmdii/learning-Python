import socket

s = socket.socket()
host = "localhost"
port = 8080

s.connect((host,port))
fileName = "test.txt"
s.send(fileName.encode())
readFile = s.recv(1024)
print(readFile.decode())


# if you wanna reseve massage uncomment this part 
# message = s.recv(1024)

# while message:
#     print("Message", message.decode())
#     message = s.recv(1024)

s.close()