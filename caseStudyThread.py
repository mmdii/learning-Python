from threading import *

class flyReservation:
    def __init__(self,ticket_left):
        self.ticket_left = ticket_left

    def buy(self,ticketReq):
        if (self.ticket_left>=ticketReq):
            print("Your ticket is confirmid")
            print("plz make a payment and take you ticket")
            self.ticket_left -= ticketReq
            
        else:
            print("there is not enough tickets remaining")
    
obj = flyReservation(9)
t1 = Thread(target=obj.buy,args=[3])
t2 = Thread(target=obj.buy,args=[4])
t3 = Thread(target=obj.buy,args=[3])
t1.start()
t2.start()
t3.start() 