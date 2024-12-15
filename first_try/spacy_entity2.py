import spacy
import time  # Importar a biblioteca para manipular o tempo

# Carregar o modelo de língua portuguesa
nlp = spacy.load("pt_core_news_sm")

palavras_chave = [
    "corte", "costura", "consulta", "fatura", "atividade", "produto final", "entrega", "pagar", "processo de fabrico", "encomenda", "medidas", "especialista",
    "observações", "correções", "aceita", "planeadas", "estampagem", "tricotagem", "atividades", "não planeadas", "associadas", "fabrico", "manual", "customizado", 
    "resposta", "processo", "atende", "percebe", "pretende", "cria", "série", "tira", "necessárias", "parte", "efetua", "escolhido", "corretas", "atividade", 
    "produção", "associada", "montar", "ocorrer", "prova", "associa", "recolhidas", "deverá", "respetiva", "aproximar", "objetivos", "produzido", "entregue", 
    "definir", "exemplo", "efetuar", "execução", "poderão", "iniciar", "necessita", "gerir", "especializada", "gerido", "adaptado", "inicia-se", "recebe", "criar", 
    "ajustar", "associá-los", "identificada", "regista", "verifica", "seleciona", "registadas", "enviada", "prepara", "inicia", "registar", "detetados", "gerado", 
    "acionado", "corrigir", "passa", "realizada", "permitir", "enviados", "incluir", "informado", "embalado", "preparado", "registando", "gerar", "anexá-la", 
    "permitir", "alterar", "ajudando"
]

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

    # Destacar frases que contêm palavras-chave e identificar entidades
    def identificador(doc, palavras_chave):
        sent_iter = iter(doc.sents)
        aprovados = []

        for sent in sent_iter:
            if any(palavra in sent.text for palavra in palavras_chave):
                frase_completa = sent.text.strip()

                while not frase_completa.endswith("."):
                    try:
                        frase_completa += " " + next(sent_iter).text.strip()
                    except StopIteration:
                        break

                frase_sem_virgulas = frase_completa.replace(",", "")
                entidades = [(ent.text, ent.label_) for ent in nlp(frase_completa).ents]
                palavras_encontradas = [palavra for palavra in palavras_chave if palavra in frase_completa]

                # Ignorar frases sem entidades
                if not entidades:
                    continue

                print("\n--------------------------------------------\n")
                print(f"Frase: {frase_completa}")
                print(f"Frase sem vírgulas: {frase_sem_virgulas}")
                print(f"Entidade(s): {entidades}")
                print(f"Palavras-chave: {palavras_encontradas}\n")

                resposta = input("Deseja salvar esta iteração? (s/n): ").strip().lower()
                if resposta == "s":
                    aprovados.append({
                        "frase": frase_completa,
                        "frase_sem_virgulas": frase_sem_virgulas,
                        "entidades": entidades,
                        "palavras_chave": palavras_encontradas
                    })

        # Aguardar 2 segundos antes de exibir as iterações aprovadas
        time.sleep(2)

        # Mostrar as iterações aprovadas ou informar que não há resultados
        if aprovados:
            print("\n-------------------- Iterações aprovadas --------------------\n")
            for iteracao in aprovados:
                print(f"Frase: {iteracao['frase']}")
                print(f"Frase sem vírgulas: {iteracao['frase_sem_virgulas']}")
                print(f"Entidade(s): {iteracao['entidades']}")
                print(f"Palavras-chave: {iteracao['palavras_chave']}\n")
                print("--------------------------------------------\n")
        else:
            print("\nNenhuma iteração foi aprovada. Não há resultados para mostrar.")

    # Destacar e imprimir as frases que contêm palavras-chave, frases sem vírgulas, entidades e palavras-chave
    identificador(doc, palavras_chave)

processar_texto()
