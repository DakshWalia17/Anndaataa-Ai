import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="AnnDaata AI", page_icon="🌾")

translations = {
    "English":{
        "title": "AnnDaata Ai", "subtitle" : "Understading The Soil,Empowering The Farmers",
        "input_section": "Enter Field Details" , "predict_button": "Predict crop",
        "result_text": "Proffitable Crop for your filed is :", "N":"Nitrogen","p": "phosphorus","K": "Potassium",
        "temperature":"Temperature","humidy":"humidity","ph":"ph","rainfall":"rainfall"
    },
    "Hindi":{
        "title": "अन्नदाता एआई", "subtitle" : "मिट्टी की समझ, किसान की तरक्की ",
        "input_section": "क्षेत्र विवरण दर्ज करें" , "predict_button": "फसल का पूर्वानुमान लगाएं",
        "result_text": "आपके क्षेत्र के लिए लाभदायक फसल है :", "N":"नाइट्रोजन","p": "फॉस्फोरस","K": "पोटैशियम",
        "temperature":"तापमान","humidy":"आर्द्रता","ph":"पीएच","rainfall":"वर्षा"
    },
    "punjabi":{
        "title": "ਅੰਨਦਾਤਾ ਐਆਈ", "subtitle" : "ਮਿੱਟੀ ਦੀ ਸਮਝ, ਕਿਸਾਨ ਦੀ ਤਰੱਕੀ ",
        "input_section": "ਖੇਤ ਵ੿ਸ਼ੇਸ਼ ਦਰਜ ਕਰੋ" , "predict_button": "ਫਸਲ ਦੀ ਪ੍ਰਯੋਜਨ ਲੱਗਾਓ",
        "result_text": "ਆਪਣੇ ਖੇਤ ਲਈ ਡਬਬਰ ਡਰਮ ਫਸਲ:", "N":"ਐਸਪੀ","p": "ਪੋਸਪਰਸ","K": "ਪੋਸਪਰਸ",
        "temperature":"ਆਪਮ","humidy":"ਆਰਜਮ","ph":"ਪੀਐਚ","rainfall":"ਬਰਸ"
    }
}

language_choice = st.sidebar.selectbox("Select Language / भाषा चुनें / ਭਾਸ਼ਾ ਚੁਣੋ", options=["English", "Hindi", "punjabi"])
t = translations[language_choice]

st.title(t['title'])
st.header(t['subtitle'])

st.subheader(t['input_section'])
col1 , col2 = st.columns(2)

with col1:
    N = st.slider(t['N'], 0, 140 ,50)
    P = st.slider(t['p'], 5,145,50)
    K = st.slider(t['K'], 5 , 205 , 50)
    ph = st.slider(t['ph'], 3.5,9.5,6.5)
with col2:
    temperature = st.slider(t['temperature'], 8.0 , 43.0 ,25.0)
    humidity = st.slider(t['humidity'], 14.0 , 100.0 ,50.0)
    rainfall = st.slider(t['rainfall'], 20.0 , 300.0 , 100.0)

if st.button(t['predict_button']):
    try:
        crop_data = pd.read_csv("crop_recommendation.csv")
        X = crop_data.drop('label', axis =1)
        Y = crop_data['label']
        clf = RandomForestClassifier()

        clf.fit(X, Y)
        input_df = pd.DataFrame({'N': [N], 'P': [P], 'K': [K], 'temperature': [temperature], 'humidity': [humidity], 'ph': [ph], 'rainfall': [rainfall]})
        prediction = clf.predict(input_df)

        st.success(f"{t['result_text']} {prediction[0].upper()}")

    except FileNotFoundError:
        st.error("Crop_recommendation.csv file not found. Please ensure the file is in the correct directrory.")