import streamlit as st
from text_to_speech import text2Speech  

st.title("Text to Speech Converter")

user_input = st.text_area("Enter the text you want to convert to speech:")

if st.button("Convert to Speech"):
    if user_input:
        audio_data = text2Speech(user_input)
        st.audio(audio_data, format="audio/mp3")

st.write("Instructions:")
st.write("1. Enter the text you want to convert to speech in the text area above.")
st.write("2. Click the 'Convert to Speech' button to generate the audio.")