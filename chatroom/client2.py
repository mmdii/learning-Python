from tkinter import *
import tkinter
import socket
from threading import Thread


def recevie():
    while True:
        try:
            msg = s.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except:
            print ("There is an error while receving message")
            break

def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf8"))

    if msg == "#quit":
        s.close()
        window.quit()

def on_closing():
    my_msg.set("#quit")
    send()

window = Tk()
window.title("Chat Room")
window.configure(bg="black")



messages_frame = Frame(window, height=300, width=300, bg="gray")
my_msg = StringVar()
my_msg.set("")
scroll_bar = Scrollbar(messages_frame)
msg_list = Listbox(messages_frame, height=15, width=150, bg="white", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

button_lable = Label(window, text="Enter Your Message", fg="skyblue", font="Aerial", bg="black")
button_lable.pack()

enter_field = Entry(window, textvariable=my_msg, fg="gray", width=50)
enter_field.pack()

send_button = Button(window, text="Send", bg="green", font="Aerail", fg="white", command= send)
send_button.pack()

quit_button = Button(window, text="Quit", bg="green", font="Aerail", fg="white", command= on_closing)
quit_button.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)

Host = "127.0.0.1"
Port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

recevie_thread = Thread(target=recevie)
recevie_thread.start()


mainloop()