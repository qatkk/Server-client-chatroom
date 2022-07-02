from os import error
import socket
import threading
import select
# Create a socket object
s = socket.socket()
received = ''
port = 9000
s.connect(('127.0.0.1', port))
s.setblocking(False)
print ('enter a command from below:\nList = 1 , Send = 2 name message , Recieve = 3 from whom , Exit =4')
def start ():
    while True:
        command = input("whats the command?\n")
        SplitedComm = command.split(" ")
        # if int(SplitedComm[0]) != int :
        #     command = input("wrong format?\n")
        s.send(command.encode())
        ready = select.select([s], [], [], 0.05)
        if ready[0]:
            data = s.recv(port).decode()
            global received 
            received =  data + received
        if(int(SplitedComm[0]) == 4) : 
            break
        elif(int(SplitedComm[0]) == 1) : 
            data = data.replace("'","")
            data = data.replace("[","")
            data = data.replace("]","")
            data = data.replace(")","")
            data = data.replace("(","")
            data = data.replace(" ","")
            data = data.split(',')  
            global client_addr
            global clients
            clients = data[0:int(len(data)/3) ]
            client_addr = data[int(len(data)/3):len(data)]
            print ('clients' , clients)
            print ('adrresses' ,client_addr)
        elif (int(SplitedComm[0]) == 2) :
            cli = 2*clients.index(SplitedComm[1])
            to = client_addr[cli],int(client_addr[cli+1])
            s.sendto(command.encode(),to)
            print (SplitedComm[2],"sent to ",SplitedComm[1])
        elif (int(SplitedComm[0]) == 3) :
            print (received)
            try :
                idx = -1
                msg = received.split(',')
                print (msg)
                for p in msg:
                    if p == '['+SplitedComm[1] :
                        idx = msg.index(p)
                        if idx != -1:
                            print(msg[idx+1])
                            msg.pop(idx)
                            msg.pop(idx+1)
                        else :
                            print('does not exist')
                # received.replace(msg[idx],"")
            except error as e :
                print (e)
                print ('sth wrong with massages')

    s.close()

start()
