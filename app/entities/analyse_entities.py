from sklearn.feature_extraction.text import CountVectorizer

class AnalyseEntities:
    def __init__(self, requirements, key_list):
        self.requirements = requirements
        self.key_list = key_list
        self.bow = CountVectorizer(stop_words='english')

    def extract(self):
        # Criar a matriz de termos do documento apenas para teoria
        X = self.bow.fit_transform(self.requirements)
        feature_names = self.bow.get_feature_names_out()
        
        # Filtrar as palavras-chave que estão presentes nos requisitos
        filtered_features = [feature for feature in feature_names if feature in self.key_list]
        return filtered_features
