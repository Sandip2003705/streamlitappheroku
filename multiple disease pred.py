# -*- coding: utf-8 -*-
"""
Created on Sun May 11 23:43:05 2025

@author: Sandip Verma
"""
import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

# Load the saved models (make sure these are .pkl files, not .py)
diabetes_model = pickle.load(open(
    'diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(
    'heart_desease_model.sav', 'rb'))

parkinsons_model  = pickle.load(open(
    'parkinsons_model.sav', 'rb'))

# Sidebar navigation
with st.sidebar:
   selected = option_menu('Multiple Disease Prediction System',

                       ['Diabetes Prediction',
                        'Heart Disease Prediction',
                        'Parkinson Prediction'],

                       icons=['activity', 'heart', 'person'],

                       default_index=0)
   
   
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction using ML")

    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        BloodPressure = st.text_input('Blood Pressure Level')
        Insulin = st.text_input('Insulin Level')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')

    with col2:
        Glucose = st.text_input('Glucose Level')
        SkinThickness = st.text_input('Skin Thickness')
        BMI = st.text_input('BMI')
        Age = st.text_input('Age')

    diab_dignosis = ''

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[
            float(Pregnancies), float(Glucose), float(BloodPressure),
            float(SkinThickness), float(Insulin), float(BMI),
            float(DiabetesPedigreeFunction), float(Age)
        ]])

        if diab_prediction[0] == 1:
            diab_dignosis = 'The person is diabetic'
        else:
            diab_dignosis = 'The person is not diabetic'

        st.success(diab_dignosis)
        
# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction using ML") 
  # Input fields
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Age of the person', min_value=1, max_value=120, step=1)
        sex = st.selectbox('Sex (0 = female, 1 = male)', [0, 1])
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3)
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200)
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=100, max_value=600)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', [0, 1])
        restecg = st.number_input('Resting ECG results (0-2)', min_value=0, max_value=2)

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220)
        exang = st.selectbox('Exercise Induced Angina (1 = yes; 0 = no)', [0, 1])
        oldpeak = st.number_input('Oldpeak (ST depression)', min_value=0.0, max_value=6.0, format="%.1f")
        slope = st.number_input('Slope of peak exercise ST segment (0-2)', min_value=0, max_value=2)
        ca = st.number_input('Number of major vessels (0-4)', min_value=0, max_value=4)
        thal = st.number_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', min_value=0, max_value=2)

    # Prediction
    if st.button('Predict Heart Disease'):
        
            heart_prediction = heart_disease_model.predict([[
                age, sex, cp, trestbps, chol, fbs, restecg,
                thalach, exang, oldpeak, slope, ca, thal
            ]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person **has** heart disease.'
            else:
                heart_diagnosis = 'The person **does not have** heart disease.'

            st.success(heart_diagnosis)
    

elif selected == "Parkinson Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    # Input fields
    col1, col2 = st.columns(2)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0)
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0)
        jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0)
        jitter_abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)
        rap = st.number_input('MDVP:RAP', min_value=0.0)
        ppq = st.number_input('MDVP:PPQ', min_value=0.0)
        ddp = st.number_input('Jitter:DDP', min_value=0.0)
        shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)
        shimmer_db = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)
        apq3 = st.number_input('Shimmer:APQ3', min_value=0.0)

    with col2:
        apq5 = st.number_input('Shimmer:APQ5', min_value=0.0)
        apq = st.number_input('MDVP:APQ', min_value=0.0)
        dda = st.number_input('Shimmer:DDA', min_value=0.0)
        nhr = st.number_input('NHR', min_value=0.0)
        hnr = st.number_input('HNR', min_value=0.0)
        rpde = st.number_input('RPDE', min_value=0.0)
        dfa = st.number_input('DFA', min_value=0.0)
        spread1 = st.number_input('spread1', min_value=-10.0, max_value=0.0)
        spread2 = st.number_input('spread2', min_value=-10.0, max_value=1.0)
        d2 = st.number_input('D2', min_value=0.0)
        ppe = st.number_input('PPE', min_value=0.0)

    # Prediction
    if st.button("Predict Parkinson's Disease"):
   
            parkinsons_prediction = parkinsons_model.predict([[
                fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
                shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
                rpde, dfa, spread1, spread2, d2, ppe
            ]])

            if parkinsons_prediction[0] == 1:
                diagnosis = "The person **has Parkinson's Disease**."
            else:
                diagnosis = "The person **does not have Parkinson's Disease**."

            st.success(diagnosis)
     

        
        
        
        
        