from connHndl import *
from traceHndl import *

#global vars
traceEntry = traceHndl()
connHandler = connHndl(traceEntry)

traceName = "MAIN"

def main():
    traceEntry.traceAdd(traceName, "Poczatek pliku")

if __name__ == "__main__":
    main()