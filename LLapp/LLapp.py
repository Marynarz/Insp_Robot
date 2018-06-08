from connHndl import *
from traceHndl import *
from funcs import *

#global vars
traceEntry = traceHndl()
connHandler = connHndl(traceEntry)

traceName = "MAIN"


def main():
    traceEntry.traceAdd(traceName, "Poczatek pliku")
    print('Loading...\n Wait a moment...')
    connHandler.scanRun()
    print("Welcome!")
    connHandler.connect()
    commandLineClient(traceEntry,connHandler)

if __name__ == "__main__":
    main()