from flask import Flask, request, render_template
from googletrans import Translator
import os
from PyPDF2 import PdfReader

app = Flask(__name__)
translator = Translator()

LANGUAGES = {
    'english': 'en',
    'kannada': 'kn',
    'hindi': 'hi'
}

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        src_lang = LANGUAGES.get(request.form.get('source', 'english').lower(), 'en')
        tgt_lang = LANGUAGES.get(request.form.get('target', 'english').lower(), 'en')

        
        file = request.files.get('file')
        if file:
            filename = file.filename.lower()
            if filename.endswith('.txt'):
                original_text = file.read().decode('utf-8')
            elif filename.endswith('.pdf'):
                # Extract text from PDF
                reader = PdfReader(file)
                original_text = ""
                for page in reader.pages:
                    original_text += page.extract_text() or ""
            else:
                original_text = ""
        else:
            
            original_text = request.form.get('text', '')

        if original_text.strip():
            try:
                translated = translator.translate(original_text, src=src_lang, dest=tgt_lang)
                if translated and translated.text:
                    translated_text = translated.text
                else:
                    translated_text = "Translation failed: No response from translator."
            except Exception as e:
                translated_text = f"Translation error: {str(e)}"
        else:
            translated_text = "No text provided for translation."

        return render_template('index.html', translated_text=translated_text, 
                               source=request.form.get('source', 'english'), 
                               target=request.form.get('target', 'english'),
                               original_text=original_text)

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
