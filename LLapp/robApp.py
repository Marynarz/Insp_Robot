from connHndl import *
from traceHndl import *

traceEntry = traceHndl()
connHandler = connHndl(traceEntry)

traceName = "ROBT_MAIN"


def main():
    traceEntry.traceAdd(traceName, "Poczatek pliku")
    connHandler.servRcv()
    commandLineClient(traceEntry,connHandler)

if __name__ == "__main__":
    main()