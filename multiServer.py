import socket
import threading


#  create a socket 
sock = socket.socket()
port = 9000
host = '127.0.0.1'
List = []
Ports = []
connection = []
address = []
try:
    sock.bind((host, port))
except socket.error as e:
    print(str(e))

def handle_client (conn,addr) : 
    print ("new connection on",addr)
    connected = True 
    while connected:
        msg = (conn.recv(9000).decode())
        SplitedMsg = msg.split(' ')
        if int(SplitedMsg[0]) is 4 :
            idx = address.index(addr)
            List.pop(idx)
            connection.pop(idx)
            address.pop(idx)
            print("client on address ", addr," was disconnected")
            conn.close()
            break
        elif int(SplitedMsg[0]) is 1 :
            conn.send(str(List+address).encode())
        elif int(SplitedMsg[0]) is 2 :
            client = List.index(SplitedMsg[1])
            connection[client].sendto("["+"client"+str(address.index(addr))+","+SplitedMsg[2]+"]".encode(),address[client])
            print('message sent')
        elif int(SplitedMsg[0]) is 3 :
            print("nothing set up yet!")

    conn.close()
def start ():
    sock.listen(5)
    print("The server is bonded to 127.0.0.1")
    while True:
        conn, addr = sock.accept()
        connection.append(conn)
        address.append(addr)
        thread = threading.Thread(name = "thread"+str(threading.active_count()-1), target = handle_client, args=(conn, addr))
        List.append("client"+str(threading.active_count()-1))
        thread.start()
        print("active connections ",threading.activeCount()-1)

start()