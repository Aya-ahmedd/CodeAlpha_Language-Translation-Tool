from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route("/translate", methods=["POST"])
def translate_text():
    """
    API Endpoint to translate text into a specified language.
    """
    try:
        data = request.json
        text = data.get("text", "").strip()
        target_language = data.get("target_language", "").lower()

        # Validate input
        if not text:
            return jsonify({"error": "No text provided"}), 400
        if target_language not in LANGUAGES:
            return jsonify({"error": "Invalid target language code"}), 400

        # Perform translation
        translated_text = translator.translate(text, dest=target_language).text
        return jsonify({"original_text": text, "translated_text": translated_text, "language": target_language})

    except Exception as e:
        return jsonify({"error": "Translation failed", "details": str(e)}), 500

@app.route("/languages", methods=["GET"])
def get_supported_languages():
    """
    API Endpoint to retrieve supported languages.
    """
    return jsonify(LANGUAGES)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)

