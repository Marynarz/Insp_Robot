class traceHndl:
    #variables
    traceLog = 0

    def __init__(self):
        try:
            self.traceLog = open("log.txt","w")
            self.traceLog.close()
        except:
            print("ERROR: unable to open log file")

    def traceAdd(self,traceName,traceBuff):
        self.traceLog = open("log.txt","a")
        self.traceLog.write(str(traceName)+": "+str(traceBuff)+"\n")
        self.traceLog.close()
