from threading import Thread
import threading

# def even_odd ():
#     evenNum()
#     oddNum()
#     print(threading.current_thread().getName())

# def evenNum ():
#     print("Even numbers are :")
#     for x in range(20):
#         if x%2 == 0:
#             print(x)

# def oddNum ():
#     print("Odd numbers are :")
#     for x in range(20):
#         if x%2 != 0:
#             print(x)



# t = Thread(target=even_odd,name="even_Odd Thread")
# t.start()

# #########################################################################################################
# class myT (Thread):
#     def run(self):
#         print(threading.current_thread().getName())
#         for x in range(1,10):
#             for j in range(1,x+1):
#                 print("*",end=" ")
#             print("\r")
# cla = myT()
# cla.start()

##########################################################################################################

def n():
    print (threading.current_thread().getName(),"has started")
    for x in range(1,10):
        print(x)
    print (threading.current_thread().getName(),"has ended")


t1 = Thread(target=n)
t2 = Thread(target=n)
t1.start()
t2.start()