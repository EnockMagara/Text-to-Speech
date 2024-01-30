# Text-to-Speech
This Python application uses a simple GUI to convert online articles into speech. It allows the user to input a URL of an article and select a language for the speech. The application then downloads the article, translates it into the selected language, converts the text into speech, and plays the audio.
Dependencies

The application uses the following Python libraries:

- newspaper3k for downloading and parsing articles.
- nltk for natural language processing.
- gtts (Google Text-to-Speech) for converting text into speech.
- googletrans for translating text.
- tkinter for the GUI.
- os for playing the audio file.

You can install these dependencies using pip:
  pip install newspaper3k nltk gTTS googletrans tkinter

How to Use

1. Run the script.
2. In the GUI, enter the URL of the article you want to convert into the "Article URL" field.
3. Select the language you want for the speech from the "Language" dropdown menu. The default language is English ('en'), but French ('fr'), Spanish ('es'), and German ('de') are also available.
4. Click the "Convert" button. The application will download and parse the article, translate the text, convert the text into speech, and play the audio.
Code Overview

The text_to_speech function is the core of the application. It gets the article from the URL entered by the user, downloads and parses the article, applies natural language processing to the text, translates the text into the selected language, converts the translated text into speech, saves the speech as an audio file, and plays the audio file.

The GUI is created using tkinter. It includes an entry field for the URL, a dropdown menu for language selection, and a button to start the text-to-speech conversion.
Note

This application uses the 'afplay' command to play the audio file, which is specific to macOS. If you're using a different operating system, you'll need to replace 'afplay' with a command that's appropriate for your system.
