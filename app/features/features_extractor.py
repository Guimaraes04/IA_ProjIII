import spacy

class SystemFeatureExtractor:
    def __init__(self, key_features):
        self.nlp = spacy.load("en_core_web_sm")
        self.key_features = set(key_features)

    def extract_features(self, text):
        doc = self.nlp(text)
        system_features = []

        for sent in doc.sents:
            tokens = [token.text.lower() for token in sent]
            
            # Extrair se a frase contiver uma feature relevante
            if any(word in tokens for word in self.key_features):
                system_features.append(sent.text.strip())

        return system_features