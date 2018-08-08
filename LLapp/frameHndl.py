class frameHndl:
    frameHeader = 7<<1
    movePart = 0
    endFrame =15>>1

    # FRAME STRUCTURE
    # 1110 | xxxx | 0111
    # header | move | end

    #trace part
    traceName = "FRAME_HNDL"
    eventLog = 0

    def __init__(self,tracePoint):
        self.eventLog = tracePoint
        self.eventLog.traceAdd(self.traceName,"Frame handler welcome!")

    def setMovement(self,front,right,left,rear):
        self.movePart=0<<3;

        if(front and not rear):
            self.movePart = self.movePart | 1<<3
        elif((not front) and rear):
            self.movePart = self.movePart | 1
        elif((not front)and (not rear)):
            self.movePart = 0
            return 1
        else:
            self.eventLog.traceAdd(self.traceName,"ERROR: front == rear: f: "+str(front)+" r: "+str(rear))
            return -1

        if(left and not right):
            self.movePart = self.movePart | 1<<1
        elif(right and not left):
            self.movePart = self.movePart | 1<<2
        else:
            self.eventLog.traceAdd(self.traceName, "ERROR: left == right: l: " + str(left) + " r: " + str(right))
            return -1

        return 0

    def getFrame(self):
        self.frameHeader = self.frameHeader << 8
        self.movePart = self.movePart << 4
        frame = self.frameHeader|self.movePart|self.endFrame
        self.eventLog.traceAdd(self.traceName, "frame: " + str(frame))
        return frame
