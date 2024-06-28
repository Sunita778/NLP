# Text Translator

Text Translator is a Python application that allows users to translate text from one language to another. This application is built using Streamlit for the user interface and the `translate` library for translation functionality. Users can input text, select the source and target languages, and receive the translated text. Additionally, the application includes text-to-speech functionality to listen to both the input and translated text.


## Features

- Translate text from one language to another.
- Supports a variety of source and target languages.
- Listen to the input and translated text using audio.py.
- Provides an interactive user interface via Streamlit.

## Prerequisites

Before using the Text Translator, make sure you have the following prerequisites installed:

- Python 3.6 or higher
- Streamlit
- The `translate` library
- (if want to listen the text) The `pyttsx3` library for audio


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sunita778/text-translator.git
   ```

2. Change to the project directory:

   ```bash
   cd text-translator
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the Text Translator app using the instructions in the "Installation" section.

2. Enter the text you want to translate in the provided text area.

3. Select the source and target languages from the dropdown menus.

4. Click the "Translate Text" button to receive the translated text.

5. Use the "Listen to Input Text" and "Listen to Translated Text" buttons to hear the input and translated text.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/my-feature
   ```

3. Make your changes, test them, and ensure they follow the project's coding style.

4. Commit your changes:

   ```bash
   git commit -m "Add new feature"
   ```

5. Push your changes to your forked repository:

   ```bash
   git push origin feature/my-feature
   ```

6. Create a pull request to the main project repository.

7. I will be reviewed your pull request and merged into the project.