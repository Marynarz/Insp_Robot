from connHndl import *
from traceHndl import *
from funcs import *

#global vars
traceEntry = traceHndl()
connHandler = connHndl(traceEntry,True)

traceName = "MAIN"


def main():
    traceEntry.traceAdd(traceName, "Poczatek pliku")
    connHandler.connect()
    commandLineClient(traceEntry,connHandler)

if __name__ == "__main__":
    main()