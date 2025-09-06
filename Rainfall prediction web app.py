# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 19:17:46 2024

@author: HONNAPPA M S
"""

import pickle
import streamlit as st
import numpy as np

# load the saved model

load_model=pickle.load(open('C:/Users/HONNAPPA M S/Desktop/Rainfall Prediction/rainfall.sav','rb'))

# create function for prediction
def prediction_function(input):
    input_asarray=np.asarray(input)
    input_reshape=input_asarray.reshape(1,-1)
    prediction=load_model.predict(input_reshape)
    print(prediction)
    if prediction[0]==1:
        return'Rainfall'
    else:
        return 'No Rainfall'

def main():
    
    # creating title
    st.title('RainFall Prediction Using ML')
    
    
    #getting the input from user
    
    col1,col2=st.columns(2)
    with col1:
        pressure=st.text_input('Pressure(mb)')
    with col2:
        
        dewpoint=st.text_input('Dewpoint (°C)')
    with col1:
        humidity=st.text_input('Humidity (%)')
    with col2:
        cloud=st.text_input('Cloud (%)')
    with col1:
        sunshine=st.text_input('Sunshine (hours)')
    with col2:
        winddirection=st.text_input('Wind Direction (°)')
    with col1:
        windspeed=st.text_input('Wind Speed (km/h)')
    
    # code for prediction
    diagnosis=''
    
    # create the button for prediction
    if st.button('RainFall Test Result'):
        diagnosis=prediction_function([pressure,dewpoint,humidity ,cloud,sunshine,winddirection,windspeed])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
        
        
