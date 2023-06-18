import sys
from socket import *
from keyboard import *
import time
ip='192.168.0.110'
port=80
bufsize=1024


def IsPrime(n):
        d=2
        while n % d !=0:
                d+=1
        return d == n

def udp():
        server=socket(AF_INET, SOCK_DGRAM)
        server.bind((ip,port))
        while True:
                if is_pressed("Esc"):
                        exit(0)
                print('Waiting...')
                data, address = server.recvfrom(bufsize)
                loc_data=data.decode('utf8')
                loc_data=int(loc_data)
                print ('recieved from: ', address, ' data: ', loc_data)
                print('Primality: ',IsPrime(loc_data))
                answer = 'answer to ' + str(address) + ', echo: ' + str(IsPrime(loc_data))
                server.sendto(answer.encode('utf8'), address)
                        
                
        
def syn():
        server=socket(AF_INET, SOCK_STREAM)
        server.bind((ip,port))
        server.listen(1)
        while True:
                print('Waiting...')
                c,addr=server.accept()
                data=c.recv(1024).decode('utf8')
                print("syn received")
                data2="syn recevied"
                c.send(data2.encode('utf8'))
                c.close()
        server.close()
        print('Server is closed')
        
def start_server():
        if choice==1:
                udp()
        elif choice==2:
                syn()
        else:
                print("Incorrect key")
                exit(0)
                

        
print("What kind of connection you want to start?")
print("1-UDP")
print("2-TCP\n")
choice=int(input())

start_server()



