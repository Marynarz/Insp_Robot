from frameHndl import *
from scratch import *
from traceHndl import *

#test init

traceEntry = traceHndl()

# frame decoder
def decodeFrame(frame):
    frame_tmp = frame;  # to do not destroy frame
    if frameValidation(frame_tmp):  # validate if frame is not destroyed
        traceEntry.traceAdd("FRAME_TEST","Frame validation OK: " + "{0:b}".format(frame))
        print("Frame validation OK: " + "{0:b}".format(frame))
        return True
    else:
        traceEntry.traceAdd("FRAME_TEST", "Frame validation OK: " + "{0:b}".format(frame))
        print("Frame validation NOK: " + "{0:b}".format(frame))
        return False  # brake due to wrong frame


# frame valiadation
def frameValidation(frame):
    frametmp = 7 << 9 | 0 << 8 | 15 >> 1;  # clean frame (without any data)
    frame = frametmp & frame;  # if header and end of frame are k, should return empty frame
    return frame == 3591;  # check if empty frame

frame = frameHndl(traceEntry)

#
# TEST CASE 1 : frame NOK
#
traceEntry.traceAdd("TEST_1","Test case 1 : frame NOK")
frame.setMovement(True,True,True,False)
traceEntry.traceAdd("TEST_1","Test frame: " + "{0:b}".format(frame.getFrame()))
if not decodeFrame(frame.getFrame()):
    print("Test 1 : ok")
    traceEntry.traceAdd("TEST_1", "Test 1 OK")
else:
    print("Test 1 : nok")
    traceEntry.traceAdd("TEST_1", "Test 1 NOK")

#
# TEST CASE 2 : frame OK
#
traceEntry.traceAdd("TEST_2","Test case 2 : frame OK")
frame.setMovement(True,True,False,False)
traceEntry.traceAdd("TEST_2","Test frame: " + "{0:b}".format(frame.getFrame()))
if decodeFrame(frame.getFrame()):
    print("Test 2 : ok")
    traceEntry.traceAdd("TEST_2", "Test 2 OK")
else:
    print("Test 2 : nok")
    traceEntry.traceAdd("TEST_2", "Test 2 NOK")
