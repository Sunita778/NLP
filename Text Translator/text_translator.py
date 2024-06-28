from translate import Translator


class translation:

    def __init__(self, text, source_language, target_language):
        self.text = text
        self.source_language = source_language
        self.target_language = target_language

    def translate_text(self):
        translator = Translator(from_lang=self.source_language, to_lang=self.target_language)
        translation = translator.translate(self.text)
        return translation