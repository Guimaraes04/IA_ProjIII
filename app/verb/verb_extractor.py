import spacy

class VerbFinder:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def find_verb_and_rest_of_sentence(self, text, keyword):
        """ Encontra o primeiro verbo que aparece depois da palavra-chave e retorna o resto da frase """
        doc = self.nlp(text)
        found_keyword = False

        for i, token in enumerate(doc):
            if found_keyword and token.pos_ == "VERB":
                # Pegamos o verbo e o restante da frase até o final do ponto
                rest_of_sentence = " ".join([t.text for t in doc[i:]])
                return rest_of_sentence

            if token.text.lower() == keyword.lower():
                found_keyword = True

        return "N/A"
