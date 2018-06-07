from connHndl import *
from traceHndl import *
from funcs import *

#global vars
traceEntry = traceHndl()
connHandler = connHndl(traceEntry)

traceName = "MAIN"


def main():
    traceEntry.traceAdd(traceName, "Poczatek pliku")
    connHandler.connect()
    commandLineClient(traceEntry)

if __name__ == "__main__":
    main()