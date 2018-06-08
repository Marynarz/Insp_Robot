cliName = "CLI"
def help():
    print("---WELCOME IN INSPECTION ROBOT---")
    print("HELP")
    print("Commands:")
    print("---------")
    print("\"help\", \"h\" - this help")
    print("\"exit\", \"q\" - exit")

def commandLineClient(traceEntry,connHndl):
    traceEntry.traceAdd(cliName, "Command Line Client Welcome!")
    while True:
        command = input("#:").split()
        if command[0].lower() in ["help","h"]:
            help()
        elif command[0].lower() in ["exit","quit","q","x"]:
            traceEntry.traceAdd(cliName, "EXIT: " + str(command))
            print("Bye...")
            break
        elif command[0].lower() in ["send", "s"]:
            connHndl.sendData(command[1])
            print(connHndl.recvData())
        else:
            traceEntry.traceAdd(cliName, "Wronc command! typed: "+str(command))
            print("Wrong command. For help use command: help")