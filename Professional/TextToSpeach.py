import pyttsx3
import PyPDF2
import pytesseract
from pdf2image import convert_from_path

def pdf_to_text(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)

        # Convert PDF pages to images
        images = convert_from_path(file_path)

    # Extract text from images using OCR
    extracted_text = ''
    for image in images:
        text = pytesseract.image_to_string(image, lang='eng')
        extracted_text += text + '\n'

    return extracted_text

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

# Provide the path to the PDF file
pdf_path = '/Users/henripeters/Documents/TAPIN_Emeline_Memoire_102021.pdf'

# Convert PDF to text
extracted_text = pdf_to_text(pdf_path)

# Convert text to speech
text_to_speech(extracted_text)
