#!/usr/bin/env python

# exemplo simples de como rodar stream de uma camera IP 

import cv2
import os

#parametros de acesso da camera
USERNAME = 'admin'
PASSWORD = '147258Jr'
IP = '192.168.0.184'
PORT = '554'

#so roda se for ffmpeg
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

#url da camera stream varia conforme o modelo da camera
URL = 'rtsp://{}:{}@{}:{}/onvif1'.format(USERNAME, PASSWORD, IP, PORT)
print('Conectando com: ' + URL)

cap = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)

while True:
    ret, frame = cap.read()
    if ret == False:
        print("Sem frame")
        break
    else:


        cv2.imshow('VIDEO', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
