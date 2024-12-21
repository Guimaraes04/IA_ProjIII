import time
from app.requirements.requirements_extractor import RequirementsExtractor
from app.translator.translator import RequirementsTranslator


def main():
    print(
        "Insira o texto a ser analisado (cole o texto e pressione na tecla Enter duas vezes para analisar): "
    )

    linhas = []

    while True:
        linha = input()

        if linha == "":
            break

        linhas.append(linha)

    texto = "\n".join(linhas)

    requirements_extractor = RequirementsExtractor()
    functional_requirements = requirements_extractor.extract_functional_requirements(
        texto
    )

    if not functional_requirements:
        return print("\nNo functional requirements could be extracted from the text!\n")

    print("\nExtracted Functional Requirements:")

    for req in functional_requirements:
        time.sleep(1)
        print(f"- {req}")

    print("\n")
    print("-" * 50)

    # Perguntar ao utilizador se deseja traduzir para português
    traduzir = (
        input("\nDeseja traduzir os requisitos para português? (y/n): ").strip().lower()
    )

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


main()
