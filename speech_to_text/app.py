import streamlit as st
from speech_to_text import speech2Text
from components.utils import decodeSound

st.title("Audio to Text Converter")

# Upload an audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

if audio_file is not None:
    st.audio(audio_file, format="audio/wav")

    if st.button("Convert to Text", key="convert_button"):
        # Save the uploaded audio file to a temporary file
        with open("temp_audio.wav", "wb") as temp_audio:
            temp_audio.write(audio_file.read())

        # Call the speech2Text function to convert the audio to text
        text_result = speech2Text("temp_audio.wav")

        # Save the text result to a text file
        text_file_name = "text_result.txt"
        with open(text_file_name, "w") as text_file:
            text_file.write(text_result)

        #display a link to download the text file
        st.markdown(f"Download the text result: [Text Result File]({text_file_name})")

        #text result
        st.subheader("Text Result:")
        st.write(text_result)

        # Optionally, to delete the temporary audio file
        st.button("Delete Temp File", key="delete_button")
        if st.button("Delete Temp File"):
            import os
            os.remove("temp_audio.wav")
