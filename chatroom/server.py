import socket
from threading import Thread

clients = {}
addresses = {}

host = "127.0.0.1"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

def accept_client_connections():
    while True:
        client_con,client_address = s.accept()
        print(client_address, "Has Connected")
        client_con.send("Welcome to the chatroom! Please Type your name to continue".encode("utf8"))
        addresses[client_con] = client_address
        Thread(target=handle_client, args=(client_con, client_address)).start()

def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix,"utf8")+msg)

def handle_client(conn, addr):
    name = conn.recv(1024).decode("utf8")
    welcome = "Welcome "+ name + " You can type #quit if you want to leave the chatroom"
    conn.send(bytes(welcome, "utf8"))
    msg = name + " has recently joined the chatroom"
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name
    while True:
        msg = conn.recv(1024)

        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name+":")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name+" Has left chatroom !", "utf8"))

if __name__ == "__main__":

    s.listen(5)
    
    print("The Server has been started and is Now Listening to client requests")
    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()