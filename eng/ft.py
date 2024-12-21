import spacy
from googletrans import Translator
import time

# Carregar o modelo de língua inglesa
nlp = spacy.load("en_core_web_sm")

print("Insira o texto a ser analisado (cole o texto e pressione na tecla Enter duas vezes para analisar): ")

linhas = []

while True:
    linha = input()
    if linha == "":
        break
    linhas.append(linha)
texto = "\n".join(linhas)

def extract_functional_requirements(text):
    doc = nlp(text) # Processar o texto

    requirements = []
    
    for sent in doc.sents:  # Iterar por sentenças
        entities = [ent.text for ent in sent.ents]  # Extrair entidades dessa sentença
        for entity in entities:
            requirement = (
                f"The requirement related to '{entity}' is: {sent.text.strip()}"
            )
            requirements.append(requirement)

    return requirements

def translate_to_portuguese(requirements):
    
    translator = Translator()
    
    translated_requirements = [translator.translate(req, src='en', dest='pt').text for req in requirements]
    return translated_requirements

# Extrair requisitos funcionais
functional_requirements = extract_functional_requirements(texto)

# Exibir os requisitos funcionais extraídos
if functional_requirements:
    
    print("\nExtracted Functional Requirements:")
    for req in functional_requirements:
        time.sleep(1)
        print(f"- {req}")
    
    print("\n")
    print("-"*50)
    
    # Perguntar ao utilizador se deseja traduzir para português
    traduzir = input("\nDeseja traduzir os requisitos para português? (sim/não): ").strip().lower()
    
    if traduzir == "sim":
        translated_requirements = translate_to_portuguese(functional_requirements)
        
        print("\nRequisitos Funcionais (Traduzidos para Português):")
        
        for req in translated_requirements:
            time.sleep(1)
            print(f"- {req}")
    print("\n")        
else:
    print("\nNo functional requirements could be extracted from the text!\n")
