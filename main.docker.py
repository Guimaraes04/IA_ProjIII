import os
import asyncio
from app.verb.verb_extractor import VerbFinder 
from app.entities.analyse_entities import AnalyseEntities
from app.requirements.requirements_extractor import RequirementsExtractor
from app.translator.translator_docker import RequirementsTranslator
from app.features.features_extractor import SystemFeatureExtractor
import time

# Criar instâncias das classes
verb_finder = VerbFinder()
translator = RequirementsTranslator()

async def main():
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

    # Ler o texto de um arquivo
    with open("current_text.txt", "r") as file:
        texto = file.read()

    # Extrair requisitos funcionais
    requirements_extractor = RequirementsExtractor(key_list)
    functional_requirements = requirements_extractor.extract_functional_requirements(texto)

    print("\n🔹 Functional Requirements Extracted:")
    if functional_requirements:
        extracted_entities = []

        for idx, req in enumerate(functional_requirements, 1):
            found_keyword = next((word for word in key_list if word in req.lower()), "N/A")
            full_sentence = verb_finder.find_verb_and_rest_of_sentence(req, found_keyword) if found_keyword != "N/A" else "N/A"

            print(f"{idx}. {req}")
            print(f"   🔹 (Keyword detected: **{found_keyword}**)")
            print(f"   📝 The **{found_keyword}** {full_sentence}")
            print("-" * 60)
            extracted_entities.append(req)
            time.sleep(1)

        # Traduzir para portugues as entidades extraídas
        traduzir_entidades = os.getenv("TRANSLATE_ENTITIES", "n").strip().lower()
        if traduzir_entidades == "y":
            translated_entities = await translator.translate_to_portuguese(extracted_entities)
            print("\n🔹 Entidades Extraídas (Traduzidas para Português):")
            for entity in translated_entities:
                print(f"- {entity}")
            print("-" * 60)
    else:
        print("\nNo functional requirements could be extracted from the text!")

    
    listar_features = os.getenv("LIST_FEATURES", "n").strip().lower()

    if listar_features == "y":
        feature_extractor = SystemFeatureExtractor(key_features)
        system_features = feature_extractor.extract_features(texto)

        print("\n🔹 System Features Identified:")
        extracted_features = []

        if system_features:
            for idx, feature in enumerate(system_features, 1):
                found_keyword = next((word for word in key_features if word in feature.lower()), "N/A")
                print(f"{idx}. {feature}")
                print(f"   🔹 (Feature detected: **{found_keyword}**)")
                print("-" * 60)
                extracted_features.append(feature)
                time.sleep(1)

            # Traduzir para portugues as features extraídas
            traduzir_features = os.getenv("TRANSLATE_FEATURES", "n").strip().lower()
            if traduzir_features == "y":
                translated_features = await translator.translate_to_portuguese(extracted_features)
                print("\n🔹 Features Extraídas (Traduzidas para Português):")
                for feature in translated_features:
                    print(f"- {feature}")
                print("-" * 60)
        else:
            print("\nNo system features could be extracted from the text!")

if __name__ == "__main__":
    asyncio.run(main())