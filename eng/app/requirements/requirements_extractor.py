import spacy


class RequirementsExtractor:
    def __init__(self):
        self.npl = spacy.load("en_core_web_sm")

    def extract_functional_requirements(self, text):
        doc = self.npl(text)  # Processar o texto

        requirements = []

        for sent in doc.sents:  # Iterar por frases
            entities = [ent.text for ent in sent.ents]  # Extrair entidades dessa frase

            for entity in entities:
                requirement = (
                    f"The requirement related to '{entity}' is: {sent.text.strip()}"
                )
                requirements.append(requirement)

        return requirements
