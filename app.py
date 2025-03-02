from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        # Get JSON input
        data = request.get_json()
        text = data.get("text", "")
        target_language = data.get("target_language", "en")  # Default: English

        # Check if input text is empty
        if not text:
            return jsonify({"error": "Text is required"}), 400

        # Translate text
        translated = translator.translate(text, dest=target_language)

        return jsonify({
            "original_text": text,
            "translated_text": translated.text,
            "language": target_language
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
