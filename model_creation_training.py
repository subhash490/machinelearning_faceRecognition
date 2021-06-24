
import cv2
import csv
import os
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time
#face_detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
Name=input()
ID=input()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    Num = 0
    while (True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # incrementing number
            Num = Num + 1
            # saving the captured face in the dataset folder
            cv2.imwrite("data1/ " + Name + "." + ID + '.' + str(Num) + ".jpg",
                                gray[y:y + h, x:x + w])
            cv2.imshow('Frame', img)
                # wait for data creation
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                # break if the sample number is morethan 150
        elif Num > 150:
            break
    cap.release()
    cv2.destroyAllWindows()
    
    
    
    def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faceSamples = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image

        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces = detector.detectMultiScale(imageNp)
        # If a face is there then append that in the list as well as Id of it
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids
  
  
  
  
  def trainig():
    recognizer = cv2.face.LBPHFaceRecognizer_create() #cv2.face_LBPHFaceRecognizer.create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces,Id
        faces, Id = getImagesAndLabels("data1")
    except Exception as e:
        s='please make "dataset" folder & put Images'
        print(s)

    recognizer.train(faces, np.array(Id)) 
    try:
        recognizer.save("model/trained.yml")
    except Exception as e:
        s='Please make "model" folder'
        print(s)

    
    
