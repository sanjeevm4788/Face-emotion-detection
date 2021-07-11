# Introduction

Global E-learning is estimated to witness an 8X over the next 5 years to reach USD 2B in 2021. India is expected to grow with a CAGR of 44% crossing the 10M users mark in 2021. Although the market is growing on a rapid scale, there are major challenges associated with digital learning when compared with brick and mortar classrooms. One of many challenges is how to ensure quality learning for students. Digital platforms might overpower physical classrooms in terms of content quality but when it comes to understanding whether students are able to grasp the content in a live class scenario is yet an open-end challenge. In a physical classroom during a lecturing teacher can see the faces and assess the emotion of the class and tune their lecture accordingly, whether he is going fast or slow. He can identify students who need special attention. Digital classrooms are conducted via video telephony software program (exZoom) where it’s not possible for medium scale class (25-50) to see all students and access the mood. Because of this drawback, students are not focusing on content due to lack of surveillance. While digital platforms have limitations in terms of physical surveillance but it comes with the power of data and machines which can work for you. It provides data in the form of video, audio, and texts which can be analysed using deep learning algorithms. Deep learning backed system not only solves the surveillance issue, but it also removes the human bias from the system, and all information is no longer in the teacher’s brain rather translated in numbers that can be analysed and tracked

## Problem Statements

We will solve the above-mentioned challenge by applying deep learning algorithms to live video data. The solution to this problem is by recognizing facial emotions. Face Emotion Recognition This is a few shot learning live face emotion detection system. The model should be able to real-time identify the emotions of students in a live class.

## Scope Of Project

A. Model should be able to identify students’ emotions using minimum reference images.

B. Model should work on the real-time webcam video feed.

C. It should be deployed as webapp.

## Steps to be followed to run this project -

STEP 1:
**$ pip install -r requirements.txt**

STEP 2:
**$ streamlit run app.py**

STEP 3:
**You can now view your Streamlit app in your browser. Local URL: http://localhost:8501**

## DEPLOYMENT

The web app is deployed on heroku and can be accessed by this link
**https://face-emotion-dectection.herokuapp.com/**

P.S - It takes over 20 minutes to launch the camera as the slug size is too large, but the face emotion detection for image is working fine.
