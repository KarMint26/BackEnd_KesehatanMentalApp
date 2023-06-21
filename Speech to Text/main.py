import os
from flask import Flask, render_template, request
import speech_recognition as sr
from pydub import AudioSegment

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    audio_file = request.files['audio']
    
    # Initialize the SpeechRecognition recognizer
    recognizer = sr.Recognizer()

    # Save the audio file temporarily
    audio_file_path = "E:/PKM KES MENTAL/Speech to Text/audio/"
    audio_file.save(audio_file_path)

    # Convert the audio to text
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    # Remove the temporary audio file
    os.remove(audio_file_path)

    # Pass the text to the HTML template for display
    return render_template('result.html', text=text)


if __name__ == '__main__':
    app.run()