import spacy


class RequirementsExtractor:
    def __init__(self, key_list):
        self.nlp = spacy.load("en_core_web_sm")
        self.key_list = set(key_list)

    def extract_functional_requirements(self, text):
        doc = self.nlp(text)  # Processar o texto
        requirements = []

        for sent in doc.sents:
            tokens = [token.text.lower() for token in sent]
            
            # Se a frase contém pelo menos uma palavra-chave, adicionamos como requisito funcional
            if any(word in tokens for word in self.key_list):
                requirements.append(sent.text.strip())

        return requirements