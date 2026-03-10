from deep_translator import GoogleTranslator

def translate_text(text, language):

    lang_codes = {
    "English":"en",
    "Hindi":"hi",
    "Telugu":"te",
    "Tamil":"ta",
    "Marathi":"mr",
    "Kannada":"kn"
    }

    target = lang_codes.get(language,"en")

    translated = GoogleTranslator(source='auto', target=target).translate(text)

    return translated
