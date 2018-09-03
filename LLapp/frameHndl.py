class frameHndl:
    frameHeader = 7<<1
    movePart = 0
    endFrame =15>>1

    # FRAME STRUCTURE
    # 1110 | xxxx | 0111
    # header | move | end
    #   X        X       X       X
    #front    right     left    rear
    # empty frame = 3591

    #trace part
    traceName = "FRAME_HNDL"
    eventLog = 0

    #constructor
    def __init__(self,tracePoint):
        self.eventLog = tracePoint
        self.eventLog.traceAdd(self.traceName,"Frame handler welcome!")

    def setMovement(self,front,right,left,rear):
        self.movePart=0<<3;

        #front/rear/stop part
        if(front and not rear):     #front movement -> first bit
            self.movePart = self.movePart | 1<<3
        elif((not front) and rear): #rear movement ->last bit
            self.movePart = self.movePart | 1
        elif((not front)and (not rear)):    #stop -> left/right part not needed
            self.movePart = 0
            return 1
        else:       #ups! something goes wrong,
            self.eventLog.traceAdd(self.traceName,"ERROR: front == rear: f: "+str(front)+" r: "+str(rear))  #error in logs
            self.endFrame = self.endFrame >> 1  #demage frame , for make sure frame will be not used
            return -1

        #left/right part
        if(left and not right):     #left
            self.movePart = self.movePart | 1<<1
        elif(right and not left):   #right
            self.movePart = self.movePart | 1<<2
        else:   #something goes wrng
            self.eventLog.traceAdd(self.traceName, "ERROR: left == right: l: " + str(left) + " r: " + str(right)) #error in logs
            self.endFrame = self.endFrame >>1 #damage of frame
            return -1

        return 0

    #building frame
    def getFrame(self):
        self.frameHeader = self.frameHeader << 8    #header
        self.movePart = self.movePart << 4          #movement part
        frame = self.frameHeader|self.movePart|self.endFrame    #all frame
        self.eventLog.traceAdd(self.traceName, "frame: " + "{0:b}".format(frame))   #write frame in logs
        return frame

    # frame decoder
    def decodeFrame(self, frame):
        frame_tmp = frame;  # to do not destroy frame
        if frameValidation(frame_tmp): #validate if frame is not destroyed
            self.eventLog.traceAdd(self.traceName, "Frame validation OK: " + "{0:b}".format(frame))
        else:
            self.eventLog.traceAdd(self.traceName, "Frame validation NOK: " + "{0:b}".format(frame))
            return -1   #brake due to wrong frame

    # frame valiadation
    def frameValidation(self, frame):
        frametmp = 7 << 9 | 0 << 8 | 15 >> 1;   #clean frame (without any data)
        frame = frametmp & frame;               #if header and end of frame are k, should return empty frame
        return frame == 3591;                   #check if empty frame
