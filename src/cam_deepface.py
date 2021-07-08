import cv2
from streamlit_webrtc import VideoTransformerBase
from deepface import DeepFace

class VideoTransformer(VideoTransformerBase):
        def transform(self, frame):
          frame = frame.to_ndarray(format="bgr24")
          faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
          gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

          #Detecting the faces
          faces = faceCascade.detectMultiScale(gray,1.1,4)
          for(x, y, w, h) in faces:

            #Drawing rectangle over the face area
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            face = frame[y:y + h, x:x + w]

            #predicting the emotion with deepface
            result = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
            cv2.putText(frame, result['dominant_emotion'], (x,y), font, 2, (0,0,0), 2, cv2.LINE_4)

          #returning a frame of the live cam with it's corresponding emotion
          return frame