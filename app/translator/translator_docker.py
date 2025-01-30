import googletrans
from googletrans import Translator

class RequirementsTranslator:
    def __init__(self):
        self.translator = Translator()

    async def translate_to_portuguese(self, requirements):
        translated = [
            (await self.translator.translate(req, src="en", dest="pt")).text for req in requirements
        ]
        return translated