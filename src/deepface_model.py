import streamlit as st
import cv2
from deepface import DeepFace


def deep(image):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Detecting the faces
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for(x, y, w, h) in faces:

        #Drawing rectangle over the face area
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255, 0), 2)
        face = image[y:y + h, x:x + w]

        #predicting the emotion with deepface
        result = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, result['dominant_emotion'], (x,y), font, 1, (0,0,225), 2, cv2.LINE_4)
    
    #Displaying image with it's corresponding emotion
    st.image(image)
  