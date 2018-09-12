#notatnik

import sys


#frame decoder
def decodeFrame(frame):
    frame_tmp = frame; #coby nie zespuc
    if frameValidation(frame_tmp):
        print("Is ok")
    else:
        print("Is nok")

#frame valiadtion
def frameValidation(frame):
    print("Origin frame: "+"{0:b}".format(frame))
    frametmp = 7<<9 | 0<<8 | 15>>1;
    print("frame clean: "+"{0:b}".format(frametmp))
    frame = frametmp & frame;
    return frame == 3591;

print(len(sys.argv))