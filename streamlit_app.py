import streamlit as st
import cv2
import numpy as np

st.subheader("แปลงภาพ Color ไปเป็นภาพ Grayscale")
img_file = st.file_uploader("เปิดไฟล์ภาพ")

if img_file is not None:    
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    #------------------------------------------------
    img_out = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    #------------------------------------------------
    col1, col2 = st.columns(2)
    col1.image(img, caption='ภาพ Color',channels="BGR")
    col2.image(img_out, caption='ภาพ Grayscale')
