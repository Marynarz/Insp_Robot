from socket import *
import netifaces as ni

network = '192.168.0.'
addreses = set()
def ownIP():
    #ni.ifaddresses('eth0')
    return ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

def isOk(addr,port):
    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(0.001)
    if not s.connect_ex((addr,port)):
        #print("Addres: "+addr+" port: "+str(port))
        addreses.add(addr)
        s.close()
        return 1
    else:
        s.close()

def searchRun():
    for ip in range(1,256):
        for port in range(1,150):
            addr = network +str(ip)
            #print(addr+':')
            if isOk(addr,port):
                print("Adres: "+addr+" port: "+str(port)+" nazwa: "+getfqdn(addr))
    addreses.remove(ownIP())
    print("END")

searchRun()
print(addreses)