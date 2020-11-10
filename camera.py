import cv2
import time
import datetime
import imutils
import os

IMG_PATH = "/home/engecorp/videostream/captured_img/"
time_grava = 3.0 # grava um frame a cada x segundos

def camera_config():
    #parametros de acesso da camera
    USERNAME = 'admin'
    PASSWORD = '147258Jr'
    IP = '192.168.15.19'
    PORT = '554'

    #so roda se for ffmpeg
    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

    #url da camera stream varia conforme o modelo da camera
    URL = 'rtsp://{}:{}@{}:{}/onvif1'.format(USERNAME, PASSWORD, IP, PORT)
    print('Conectando com: ' + URL)
    return URL



#salva um frame de referencia e compara com o atual
def motion_detection(URL):
    video_capture = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)
    #video_capture = cv2.VideoCapture(0) 
    

    first_frame = None
    startTime = time.time()

    while True:

        ret,frame = video_capture.read()
        
        if ret: exit
        
        text = 'Normal'

        greyscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        gaussian_frame = cv2.GaussianBlur(greyscale_frame, (21,21),0)
        blur_frame = cv2.blur(gaussian_frame, (5,5))
        greyscale_image = blur_frame
     
        if first_frame is None:
            first_frame = greyscale_image
        else:
            pass

        frame_delta = cv2.absdiff(first_frame, greyscale_image)
        thresh = cv2.threshold(frame_delta, 100, 255, cv2.THRESH_BINARY)[1]
        dilate_image = cv2.dilate(thresh, None, iterations=2)
        _,cnt,hierarchy = cv2.findContours(dilate_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

        for c in cnt:
            if c is None: print(c, 'nothing!!!')
            if cv2.contourArea(c) > 800:
                (x, y, w, h) = cv2.boundingRect(c)

                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

                text = 'Movimento detectado'
                
            else:
                pass


        
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, '{+} Status: %s' % (text),
            (10,frame.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 255), 2)
        
        cv2.putText(frame, datetime.datetime.now().strftime('%A %d %B %Y %I:%M:%S%p'),
            (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX , 0.35, (0, 0, 255),1)
       
        cv2.imshow('Security Feed', frame)
        #cv2.imshow('Threshold(foreground mask)', dilate_image)
        #cv2.imshow('Frame_delta', frame_delta)


        if (text == 'Movimento detectado') and ((time.time()- startTime) > time_grava ):
            ()
            res = cv2.imwrite(os.path.join(IMG_PATH, str(time.time()) + ".jpg"), frame)
            first_frame = None
            startTime = time.time()



        key = cv2.waitKey(1) & 0xFF 
        if key == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__=='__main__':
    print('will start now')
    cam = camera_config()
    motion_detection(cam)
