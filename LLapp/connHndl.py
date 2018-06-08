from socket import *
import netifaces as ni
import sys

class connHndl:
    #variables
    network = 0
    addreses = set()
    eventLog = 0
    traceName = "CONN_HNDL"
    clientSock = socket(AF_INET,SOCK_STREAM)

    #constructor
    def __init__(self,traceLog):
        self.eventLog = traceLog
        self.eventLog.traceAdd(self.traceName,"Connection handler, welcome!")
        tempIp = self.ownIP()
        self.network = tempIp[0:len(tempIp)-3]
        self.eventLog.traceAdd(self.traceName,"Own ip: "+tempIp+" network: "+self.network)

    def __del__(self):
        self.clientSock.close()

    #determine own ip
    def ownIP(self):
        return ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    #check if ip address and port is open
    def isOk(self,addr, port):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.001)
        if not s.connect_ex((addr, port)):
            # print("Addres: "+addr+" port: "+str(port))
            self.addreses.add((addr,port))
            s.close()
            return 1
        else:
            s.close()

    #scanning
    def scanRun(self):
        for ip in range(2, 256):
            for port in range(1, 150):
                addr = self.network + str(ip)
                # print(addr+':')
                if addr == self.ownIP():
                    pass
                elif self.isOk(addr, port):
                    self.eventLog.traceAdd(self.traceName,"Adres: " + addr + " port: " + str(port) + " nazwa: " + getfqdn(addr))
        self.eventLog.traceAdd(self.traceName,"IP ADRESSES found: "+str(self.addreses))
        self.eventLog.traceAdd(self.traceName,"End of scanning!")

    def connect(self):
        self.clientSock.settimeout(0.1)
        try:
            for ipAddr in self.addreses:
                if ipAddr[0] == self.ownIP():
                    pass
                elif self.clientSock.connect(ipAddr):
                    self.eventLog.traceAdd(self.traceName,"Conn established for: "+str(ipAddr))
                    break
                self.eventLog.traceAdd(self.traceName,"Conn not estabished for: "+str(ipAddr))
            #self.clientSock.close()
        except:
            self.eventLog.traceAdd(self.traceName,sys.exc_info()[0])
    def servRcv(self):
        self.clientSock.bind(('localhost',50000))
        self.clientSock.listen(1)
        conn , addr = self.clientSock.accept()
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    def sendData(self,data):
        try:
            self.clientSock.sendall(str(data))
        except:
            self.eventLog.traceAdd(self.traceName, sys.exc_info()[0])
    def recvData(self):
        return self.clientSock.recv(1024)