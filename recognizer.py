import cv2
import numpy as np
import pywhatkit as kitkat
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('model/trained.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
id = 0

# add the list of names of your person here
names = ['None','ananya','subhash'] 
msg_cnt=0
aws_cn=0

cam = cv2.VideoCapture(0)

while True:
    ret, img =cam.read()
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        
        if (confidence >65):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        if(id==subhash):
            if(msg_cnt==0):
                email_message()
                whatsapp()
                count=count+1
            
        if(id==ananya):
            if(aws_cnt==0):
                aws()
                aws_cnt=aws_cnt+1
    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

cam.release()

cv2.destroyAllWindows()
