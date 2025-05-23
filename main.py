from app.verb.verb_extractor import VerbFinder 
from app.entities.analyse_entities import AnalyseEntities
from app.requirements.requirements_extractor import RequirementsExtractor
from app.translator.translator import RequirementsTranslator
from app.features.features_extractor import SystemFeatureExtractor
import time

# Criar instâncias das classes
verb_finder = VerbFinder()
translator = RequirementsTranslator()

def main():
    key_list = [
        "managers", "scanners", "company", "database", "stakeholders", "server", "maintenances", 
        "automation", "manager", "branch", "sensors", "team", "subsidiary", "dashboard", "consultant", 
        "productions", "tool", "specialist", "tailor", "planner", "worker", "analyst", 
        "enterprise", "person", "driver", "shipping", "employees", "compliance", "accountant"
    ]

    key_features = [
        "inventory", "stock", "supplier", "purchase order", "warehouse", "product", "lot number",
        "production", "manufacturing", "process planner", "cutting", "sewing", "assembly", "garment",
        "rfid scanner", "sensors", "machine", "conveyor belt", "control room", "monitoring",
        "temperature", "analytics", "plc", "automation", "dashboard",
        "energy", "smart meter", "power consumption", "electricity", "usage limit", "alerts",
        "optimization", "waste reduction", "customer feedback", "crm", "consultant",
        "quality assurance", "reporting tool", "service enhancement",
        "customer", "accountant", "invoice", "payment", "debt", "receipt", "regular customer",
        "urban waste", "collection", "recycling", "contract", "container", "nfc tag", "waste type",
        "collection route", "truck driver", "points system", "anomaly detection", "credit movement"
    ]

    print("Enter the text and press the Enter key on your keyboard to analyze: ")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)

    texto = "\n".join(linhas)

    # Criar instâncias dos extrators
    requirements_extractor = RequirementsExtractor(key_list)
    feature_extractor = SystemFeatureExtractor(key_features)

    functional_requirements = requirements_extractor.extract_functional_requirements(texto)
    system_features = feature_extractor.extract_features(texto)

    while True:
        print("\n📌 Select an option:")
        print("1️⃣  List the functional requirements found")
        print("2️⃣  List the system features found")
        print("3️⃣  Leave the program")

        opcao = input("Enter the desired option (1/2/3): ").strip()

        if opcao == "1":
            if functional_requirements:
                extracted_entities = []
                print("\n🔹 Functional Requirements Extracted:")

                for idx, req in enumerate(functional_requirements, 1):
                    found_keyword = next((word for word in key_list if word in req.lower()), "N/A")
                    full_sentence = verb_finder.find_verb_and_rest_of_sentence(req, found_keyword) if found_keyword != "N/A" else "N/A"

                    print(f"{idx}. {req}")
                    print(f"   🔹 (Keyword detected: **{found_keyword}**)")
                    print(f"   📝 The **{found_keyword}** {full_sentence}")
                    print("-" * 60)
                    extracted_entities.append(req)
                    time.sleep(1)

                # Perguntar se deseja traduzir
                traduzir = input("\nDo you want to translate the requirements into Portuguese? (y/n): ").strip().lower()
                if traduzir == "y":
                    translated_entities = translator.translate_to_portuguese(extracted_entities)
                    print("\n🔹 Requisitos Funcionais (Traduzidos para Português):")
                    for entity in translated_entities:
                        print(f"- {entity}")
                    print("-" * 60)
            else:
                print("\nNo functional requirements could be extracted from the text!")

        elif opcao == "2":
            if system_features:
                extracted_features = []
                print("\n🔹 System Features Identified:")

                for idx, feature in enumerate(system_features, 1):
                    found_keyword = next((word for word in key_features if word in feature.lower()), "N/A")
                    print(f"{idx}. {feature}")
                    print(f"   🔹 (Feature detected: **{found_keyword}**)")
                    print("-" * 60)
                    extracted_features.append(feature)
                    time.sleep(1)

                # Perguntar se deseja traduzir
                traduzir = input("\nDeseja traduzir as features para português? (y/n): ").strip().lower()
                if traduzir == "y":
                    translated_features = translator.translate_to_portuguese(extracted_features)
                    print("\n🔹 Features do Sistema (Traduzidas para Português):")
                    for feature in translated_features:
                        print(f"- {feature}")
                    print("-" * 60)
            else:
                print("\nNo system features could be extracted from the text!")

        elif opcao == "3":
            print("\n✅ Leaving the program...")
            break

        else:
            print("\n⚠️  Invalid option! Please try again.")

if __name__ == "__main__":
    main()
