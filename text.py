

# Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os
from googletrans import Translator
import tkinter as tk
from tkinter import ttk

# Function to convert text to speech
def text_to_speech():
    # Get the article
    article = Article(url_entry.get())

    # Download and parse the article
    article.download()
    article.parse()

    # Download the 'punkt' package if not previously downloaded
    nltk.download('punkt')

    # Apply Natural Language Processing (NLP)
    article.nlp()

    # Get the articles text
    mytext = article.text

    # Translate the text to the selected language
    translator = Translator()
    translation = translator.translate(mytext, dest=language_var.get())
    translated_text = translation.text

    # Pass the text and language to the engine, speed = high
    myobj = gTTS(text=translated_text, lang=language_var.get(), slow=False)

    # Save the speech audio into a file
    myobj.save("read_article.mp3")

    # Play the converted audio file
    os.system("afplay read_article.mp3")

# Create a window
window = tk.Tk()

# Create an entry field for the URL
url_label = tk.Label(window, text="Article URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create a dropdown menu for language selection
language_var = tk.StringVar(window)
language_var.set('en') # default value
language_label = tk.Label(window, text="Language:")
language_label.pack()
language_dropdown = ttk.Combobox(window, textvariable=language_var)
language_dropdown['values'] = ('en', 'fr', 'es', 'de') 
language_dropdown.pack()

# Create a button to start the text to speech conversion
convert_button = tk.Button(window, text="Convert", command=text_to_speech)
convert_button.pack()

# Run the GUI
window.mainloop()


