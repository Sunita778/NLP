import streamlit as st
from text_translator import translation

#Title
st.title("English to Hindi text Translator")

# text input
user_input = st.text_area("Enter the english text to translate in hindi:")

if st.button("Translate Text"):
    if user_input:
        # result_text = translation(user_input)
        # result = result_text.text
        my_translator = translation(user_input)
        result = my_translator.translate_word()

        # Display the translated text
        st.write("Translated Text:")
        st.write(result)

        # Save the text result to a text file
        text_file_name = "input_text.txt"
        with open(text_file_name, "w", encoding="utf-8") as text_file:
            text_file.write(user_input)

        # Save the text result to a text file
        text_file_name = "translated_text.txt"
        with open(text_file_name, "w", encoding="utf-8") as text_file:
            text_file.write(result)



st.write("Instructions:")
st.write("1. Enter the text you want to translate in the text area above.")
st.write("2. Click the 'Translate Text' button for translation.")


