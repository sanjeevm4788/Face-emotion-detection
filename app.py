from src.cam_dl import VideoTransformer
from src.dl_model import dl_model
from src.mainpage import mainpage
import streamlit as st
from PIL import Image
import numpy as np
from streamlit_webrtc import webrtc_streamer


def main():

    #Title of the web app
    st.title("Face Emotion detection")
    
    #Available function in the web app
    activities = ["Homepage", "Deep learning with webcam", "Deep learning with picture"]
    choice = st.sidebar.selectbox("Select the required activty to navigate.", activities)

    #Navigating to Homepage
    if choice == "Homepage":
      
      mainpage()

    #Navigating to face emotion detction with pre=trained deep learning model on live web-cam            
    if choice == "Deep learning with webcam":

      st.text('Select the respective devices for webcam and microphone(Allow access to camera and microphone if asked).')
      st.text('Press START to start face emotion detection and STOP for stopping the detection.')
      st.text('If the webcam is not opening then, Try pressing START and STOP and relaunching the tab sometimes as it may take some time to open the webcam in some cases. ')
      webrtc_streamer(key="exam", video_transformer_factory=VideoTransformer)

    #Navigating to face emotion detction with pre=trained deep learning model on picture            
    if choice == "Deep learning with picture":

      #Uploading the image
      image_file = st.file_uploader("Upload the image", type=['jpeg', 'png', 'jpg'])

      if image_file is not None:
          image1 = Image.open(image_file)
          image = np.asarray(image1)

          #Displaying the uploaded image
          st.image(image1)
          st.text('Press Process to display the face emotion detected image.')

          #Processing the uploaded image
          if st.button("Process"):
            dl_model(image)


if __name__ == "__main__":
    main()