import streamlit as st
import cv2
from tensorflow.keras.models import load_model
import numpy as np

#loading the pre-trained model file
model = load_model('final_model.h5')

def dl_model(image):

    #Labels for the emotions
    class_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Detecting the faces
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for(x, y, w, h) in faces:

        #Drawing rectangle over the face area
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255, 0), 2)
        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face,(48,48))
        face = np.expand_dims(face,axis=0)
        face = face/255.0
        face = face.reshape(face.shape[0],48,48,1)

        #Predicting the emotion with the pre-trained model
        preds = model.predict(face)[0]
        label = class_labels[preds.argmax()]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, label, (x,y), font, 1, (0,0,225), 2, cv2.LINE_4)

    #Displaying image with it's corresponding emotion
    st.image(image)
