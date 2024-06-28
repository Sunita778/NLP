import streamlit as st
from text_translator import translation
# from audio import speak


# Title
st.title("Text Translator")

# list of languages with language codes
languages = {
    "English": "en",
    "Hindi": "hi",
    "Odia": "or",  
    "Telugu": "te",  
    "Bengali": "bn", 
    "Marathi": "mr",
    "Tamil": "ta",
    "Urdu": "ur",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Assamese": "as",
    "Sanskrit": "sa",
    "Spanish": "es",
    "French": "fr",
    "Nepali": "ne", 
    "German": "de",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Russian": "ru",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
}


# Text input
user_input = st.text_area("Enter the text to translate:")

source_language = st.selectbox("Select Source Language", list(languages.keys()))
target_language = st.selectbox("Select Target Language", list(languages.keys()))


# result = ''
if st.button("Translate Text"):
    if user_input and source_language and target_language:
        # Map the selected language names to language codes
        source_lang_code = languages[source_language]
        target_lang_code = languages[target_language]

        # Create a translation object and call the translate_text method
        translator = translation(user_input, source_lang_code, target_lang_code)
        result = translator.translate_text()

        # Display the translated text
        st.write("Translated Text:")
        st.write(result)


        # # Save the text result to a text file
        # text_file_name = "input_text.txt"
        # with open(text_file_name, "w", encoding="utf-8") as text_file:
        #     text_file.write(user_input)

        # # Save the text result to a text file
        # text_file_name = "translated_text.txt"
        # with open(text_file_name, "w", encoding="utf-8") as text_file:
        #     text_file.write(result)

# # Listen to the input text
# if st.button("Listen to Input Text"):
#     speak(user_input) 
# # Listen to the translated text
# if st.button("Listen to Translated Text"):
#     speak(result) 


st.write("Instructions:")
st.write("1. Enter the text you want to translate in the text area above.")
st.write("2. Click the 'Translate Text' button for translation.")


