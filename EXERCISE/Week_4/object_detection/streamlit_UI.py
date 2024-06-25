import streamlit as st
import numpy
import PIL.Image as Image
from process import *

st.title("Object Detection")
file = st.file_uploader("Choose an image", type=['jpg', 'png', 'jpeg'])
if file is not None:
    st.image(file, caption='Upload image')
    image = Image.open(file)
    image_array = numpy.array(image)
    detection = process_image(image_array)
    processed_image = draw_boxes(image_array, detection)
    st.image(processed_image, caption='Processed image')