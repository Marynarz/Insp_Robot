class traceHndl:
    #variables
    traceLog = 0

    #constructor
    def __init__(self):
        try:
            self.traceLog = open("log.txt","w") #creating file log.txt
            self.traceLog.close()
        except:
            print("ERROR: unable to open log file")

    def traceAdd(self,traceName,traceBuff):     #adding trace to log.txt
        self.traceLog = open("log.txt","a")
        self.traceLog.write(str(traceName)+": "+str(traceBuff)+"\n")
        self.traceLog.close()
