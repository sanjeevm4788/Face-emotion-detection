import streamlit as st

#Contents displayed on the Homepage
def mainpage():
    st.write("This is an face emotion detection app that detects facial emotions.")
    st.write("It can detect 7 emotions.")
    st.write('Angry :angry:, Disgust :persevere:, Fear 😨, Happy :smile:, Sad :worried:, Suprise :astonished:, Neutral :expressionless:.')
    st.subheader('Deep learning with Webcam and Deep learning with picture-')
    st.text('They both use deep learning model to predict the face emotion in picture and in live webcam.')
    st.text('You can use the deep learning with webcam to detect the facial emotion on real time through your webcam.')
    st.text('You can use the deep learning with picture to detect facial emotion on the uploaded picture.')
