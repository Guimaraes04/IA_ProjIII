import spacy
import time

# Carregar o modelo de língua portuguesa
nlp = spacy.load("pt_core_news_sm")

def processar_texto():
    print("Insira o texto a ser analisado (cole o texto e pressione na tecla Enter duas vezes para analisar):")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)
    texto = "\n".join(linhas)

    # Processar o texto com spaCy
    doc = nlp(texto)

    # Destacar frases que contêm entidades e atender ao critério dos verbos
    def identificador(doc):
        sent_iter = list(doc.sents)  # Listar todas as sentenças
        aprovados = []

        for sent in sent_iter:
            encontrou_entidade = False
            for ent in sent.ents:
                # Obter os índices das palavras após a entidade
                if ent.end < len(sent):
                    primeira_palavra = sent[ent.end]  # Primeira palavra após a entidade
                    segunda_palavra = sent[ent.end + 1] if (ent.end + 1) < len(sent) else None

                    # Verificar se alguma das palavras é um verbo
                    if primeira_palavra.pos_ == "VERB" or (segunda_palavra and segunda_palavra.pos_ == "VERB"):
                        frase_completa = sent.text.strip()
                        frase_sem_virgulas = frase_completa.replace(",", "")

                        print("\n--------------------------------------------\n")
                        print(f"Frase: {frase_completa}")
                        print(f"Frase sem vírgulas: {frase_sem_virgulas}")
                        print(f"Entidade: {ent.text} ({ent.label_})\n")

                        resposta = input("Deseja salvar esta iteração? (s/n): ").strip().lower()
                        if resposta == "s":
                            aprovados.append({
                                "frase": frase_completa,
                                "frase_sem_virgulas": frase_sem_virgulas,
                                "entidade": (ent.text, ent.label_)
                            })
                        encontrou_entidade = True
                        break

            if not encontrou_entidade:
                print(f"A frase '{sent.text.strip()}' não contém entidade relevante ou não atende ao critério.\n")

        # Aguardar 2 segundos
        time.sleep(2)

        if aprovados:
            print("\n-------------------- Iterações aprovadas --------------------\n")
            for iteracao in aprovados:
                print(f"Frase: {iteracao['frase']}")
                print(f"Frase sem vírgulas: {iteracao['frase_sem_virgulas']}")
                print(f"Entidade: {iteracao['entidade']}\n")
                print("--------------------------------------------\n")
        else:
            print("\nNenhuma iteração foi aprovada. Não há resultados para mostrar.")

    # Processar as frases e filtrar com base no critério
    identificador(doc)

processar_texto()
