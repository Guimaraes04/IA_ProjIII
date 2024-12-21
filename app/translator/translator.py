from googletrans import Translator


class RequirementsTranslator:
    def __init__(self):
        pass

    def translate_to_portuguese(self, requirements):
        translator = Translator()

        translated_requirements = [
            translator.translate(req, src="en", dest="pt").text for req in requirements
        ]

        return translated_requirements
