from socket import *
import netifaces as ni

class connHndl:
    #variables
    network = 0
    addreses = set()
    eventLog = 0
    traceName = "CONN_HNDL"
    clientSock = 0

    #constructor
    def __init__(self,traceLog):
        self.eventLog = traceLog
        self.eventLog.traceAdd(self.traceName,"Connection handler, welcome!")
        tempIp = self.ownIP()
        self.network = tempIp[0:len(tempIp)-3]
        self.eventLog.traceAdd(self.traceName,"Own ip: "+tempIp+" network: "+self.network)
        print("Loading... It can take a moment")
        self.scanRun()
        print("Loading succesfull, WELCOME!")
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
        for ip in range(1, 256):
            for port in range(1, 150):
                addr = self.network + str(ip)
                # print(addr+':')
                if self.isOk(addr, port):
                    self.eventLog.traceAdd(self.traceName,"Adres: " + addr + " port: " + str(port) + " nazwa: " + getfqdn(addr))
        #self.addreses.remove(self.ownIP())
        self.eventLog.traceAdd(self.traceName,"End of scanning!")

    def connect(self):
        self.clientSock = socket(AF_INET,SOCK_STREAM)
        try:
            for ipAddr in self.addreses:
                if self.clientSock.connect(ipAddr):
                    break
                self.eventLog.traceAdd(self.traceName,"Conn not estabished for: "+str(ipAddr))
        except:
            self.eventLog.traceAdd(self.traceName,"ERROR")