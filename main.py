from app.entities.analyse_entities import AnalyseEntities
from app.requirements.requirements_extractor import RequirementsExtractor
from app.translator.translator import RequirementsTranslator
import time

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

    print("\n🔹 Entities Analyzed:")
    for ent in functional_entities:
        print(f"- {ent}")

    print("\n" + "-" * 50)

    # Extrair requisitos funcionais
    requirements_extractor = RequirementsExtractor(key_list)
    functional_requirements = requirements_extractor.extract_functional_requirements(texto)

    print("\n🔹 Functional Requirements Extracted:")
    if functional_requirements:
        for idx, req in enumerate(functional_requirements, 1):
            print(f"{idx}. {req}")
            time.sleep(1)
    else:
        print("\nNo functional requirements could be extracted from the text!")
        
    traduzir = (
        input("\nDeseja traduzir os requisitos para português? (y/n): ").strip().lower()
    )

    # Traduzir requisitos para português
    if traduzir == "y":
        requirements_translator = RequirementsTranslator()
        translated_requirements = requirements_translator.translate_to_portuguese(
            functional_requirements
        )

        print("\nRequisitos Funcionais (Traduzidos para Português):")

        for req in translated_requirements:
            time.sleep(1)
            print(f"- {req}")

        print("\n")
    else:
        print("\nNo functional requirements could be extracted from the text!\n")

if __name__ == "__main__":
    main()