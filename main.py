from app.verb.verb_extractor import VerbFinder
from app.entities.analyse_entities import AnalyseEntities
from app.requirements.requirements_extractor import RequirementsExtractor
from app.translator.translator import RequirementsTranslator
from app.features.features_extractor import SystemFeatureExtractor
import time

# Criar uma instância da classe VerbFinder
verb_finder = VerbFinder()

def main():
    key_list = [
        "managers", "scanners", "company", "database", "stakeholders", "server", "maintenances", 
        "automation", "manager", "branch", "sensors", "team", "subsidiary", "dashboard", "consultant", 
        "productions", "tool", "trace", "specialist", "tailor", "planner", "worker", "analyst", 
        "enterprise", "person", "driver", "shipping", "employees", "compliance", "accountant", "receive"
    ]

    print("Insira o texto a ser analisado (cole o texto e pressione Enter duas vezes para analisar): ")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)

    texto = "\n".join(linhas)

    # Analisar as entidades do texto usando o BoW
    analyse_entities = AnalyseEntities([texto], key_list)
    functional_entities = analyse_entities.extract()

    if not functional_entities:
        return print("\nNo entities could be extracted from the text!\n")

    print("\n🔹 Functional Requirements Extracted:")
    requirements_extractor = RequirementsExtractor(key_list)
    functional_requirements = requirements_extractor.extract_functional_requirements(texto)

    if functional_requirements:
        for idx, req in enumerate(functional_requirements, 1):
            # Encontrar a palavra-chave correspondente no requisito
            found_keyword = next((word for word in key_list if word in req.lower()), "N/A")

            # Encontrar a frase completa a partir do verbo após a palavra-chave
            full_sentence = verb_finder.find_verb_and_rest_of_sentence(req, found_keyword) if found_keyword != "N/A" else "N/A"

            print(f"{idx}. {req}")
            print(f"   🔹 (Palavra-chave encontrada: **{found_keyword}**)")
            print(f"   📝 The **{found_keyword}** {full_sentence}")
            print("-" * 60)
            time.sleep(1)
    else:
        print("\nNo functional requirements could be extracted from the text!")

if __name__ == "__main__":
    main()
