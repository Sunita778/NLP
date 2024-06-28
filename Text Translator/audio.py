import pyttsx3

# Initialize  engine
engine = None

def initialize_engine():
    global engine
    if engine is None:
        engine = pyttsx3.init()

def speak(text):
    initialize_engine()  # Initialize the engine if not already initialized
    engine.say(text)
    engine.runAndWait()