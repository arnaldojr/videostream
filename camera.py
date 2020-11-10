#!/usr/bin/env python

#
# rtsp links: http://wiki.multimedia.cx/index.php?title=RTSP
#

import cv2
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

stream = 'rtsp://admin:147258Jr@192.168.15.19/onvif1'
#stream = 0

cap = cv2.VideoCapture(stream)

# check if opened 
if not cap.isOpened():
    print("Can't open stream/file")
else:    
    while True:
        # read one frame (and "return" status)
        ret, frame = cap.read()

        # exit if error (check it because it doesn't rise error when it has problem to read)
        if not ret:
            break

        # (open window and) display one frame
        cv2.imshow('frame', frame)

        # exit if pressed any key
        # (it doesn't wait for key so you can read next frame)
        # (you need opened window to catch pressed key)
        if cv2.waitKey(1) != -1:
            break

# close stream
cap.release()

# close window
cv2.destroyAllWindows()