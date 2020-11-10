import cv2
import os


USERNAME = 'admin'
PASSWORD = '147258Jr'
IP = '192.168.15.19'
PORT = '554'

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"


URL = 'rtsp://{}:{}@{}:{}/onvif1'.format(USERNAME, PASSWORD, IP, PORT)
print('Connecting to: ' + URL)

vcap = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)

while(1):
    ret, frame = vcap.read()
    if ret == False:
        print("Frame is empty")
        break
    else:
        cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)


# cam = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)