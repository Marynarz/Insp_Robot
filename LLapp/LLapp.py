# PC APP
#client (pc) -> server (robot)

#own classes
from connHndl import *
from traceHndl import *
from funcs import *
from frameHndl import *

#python libs
import sys

#global vars
traceEntry = traceHndl()                    #trace point
connHandler = connHndl(traceEntry,True)     #connection handler
frameHandler = frameHndl(traceEntry)         #frame handler
ipAddr =0
port =0

traceName = "MAIN"                          #trace name


def main():
    if len(sys.argv) ==3:                    #if args in program call, add server ip and port
        #LLapp.py <ipaddress> <port>
        ipAddr = sys.argv[1]
        port = sys.argv[2]
        traceEntry.traceAdd(traceName,"Args used: ipAddress: "+str(ipAddr)+", port: "+str(port))

    traceEntry.traceAdd(traceName, "Main client welcome")
    connHandler.connect()
    commandLineClient(traceEntry,connHandler)

if __name__ == "__main__":
    main()                      #main call