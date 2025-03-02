from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == "__main__":
    print("🌍 Language Translation Tool")
    text = input("Enter text to translate: ")
    target_language = input("Enter target language (e.g., 'fr' for French, 'es' for Spanish): ")
    
    translated_text = translate_text(text, target_language)
    print(f"📝 Translated Text: {translated_text}")
