import threading
from queue import Queue
import time
import socket
from plyer import notification
# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
print_lock = threading.Lock()



target = input("Enter target: ")
ip = socket.gethostbyname(target)

notification.notify(
            title = "Port scanning:",
            message=ip ,
            timeout=60)


#error handling bois
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('Port',port,": Open")
        con.close()
    except:
        pass



def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()



        


q = Queue()
for x in range(30):
     t = threading.Thread(target=threader)
     t.daemon = True
     t.start()


start = time.time()

# Ports 1-1000
for worker in range(1,1000):
    q.put(worker)

q.join()
