import spacy
import sys

# Carregar o modelo de língua portuguesa
nlp = spacy.load("pt_core_news_sm")

palavras_chave = [
    "corte", "costura", "consulta", "fatura", "atividade", "produto final", "entrega", "pagar", "processo de fabrico", "encomenda", "medidas", "especialista","observações","correções", "aceita", "planeadas", "estampagem", "tricotagem", "atividades", "não planeadas", "associadas", "fabrico", "manual", "customizado", "resposta", "processo", "atende", "percebe", "pretende", "cria", "série", "tira", "necessárias", "parte", "efetua", "escolhido", "corretas", "atividade", "produção", "associada", "montar", "ocorrer", "prova", "associa", "recolhidas", "deverá", "respetiva", "aproximar", "objetivos", "produzido", "entregue", "definir", "exemplo", "efetuar", "execução", "poderão", "iniciar", "necessita", "gerir", "especializada", "gerido", "adaptado", "inicia-se", "recebe", "criar", "ajustar", "associá-los", "identificada", "regista", "verifica", "seleciona", "registadas", "enviada", "prepara", "inicia", "registar", "detetados", "gerado", "acionado", "corrigir", "passa", "realizada", "permitir", "enviados", "incluir", "informado", "embalado", "preparado", "registando", "gerar", "anexá-la", "permitir", "alterar", "ajudando"
]

texto = """
A GlobalPrint Solutions, Lda. necessita de um sistema de software para gerir os seus serviços de impressão e personalização de materiais gráficos. A GlobalPrint é especializada na produção de cartazes, cartões de visita, panfletos, calendários e outros materiais personalizados para empresas e clientes individuais. Cada projeto é gerido de forma independente e adaptado às necessidades específicas do cliente.
O processo inicia-se com um(a) Designer Gráfico, que recebe do cliente um pedido detalhado. O(a) Designer é responsável por criar ou ajustar os modelos gráficos e associá-los a uma nova Ordem de Produção, identificada por um número único. Caso o cliente seja novo, o(a) Designer regista no sistema os dados do cliente, incluindo nome, contacto, tipo de cliente (individual ou empresa) e histórico de pedidos.
Após a criação da Ordem de Produção, um(a) Técnico de Impressão verifica os detalhes do projeto e seleciona os materiais necessários, como tipo de papel, gramatura, cores de tinta e acabamentos (ex.: laminação, verniz). Todas as especificações são registadas no sistema, incluindo observações técnicas, prazos e quantidade de unidades a produzir.
Em seguida, a Ordem de Produção é enviada para a fila de produção. Um(a) Operador(a) de Máquina prepara os equipamentos e inicia o processo de impressão. Durante a impressão, o sistema deve registar automaticamente os dados da produção, como tempo gasto, consumo de materiais e possíveis defeitos detectados. Se houver algum problema técnico, um alerta é gerado, e um(a) Técnico de Manutenção é acionado(a) para corrigir a falha.
Depois da impressão, o material passa por uma etapa de revisão de qualidade, realizada por um(a) Inspetor(a). Caso sejam identificados problemas, o sistema deve permitir o registo da ocorrência e o reenvio para correção. Apenas materiais aprovados são enviados para os acabamentos finais, que podem incluir cortes, dobragens ou encadernações.
O cliente é informado automaticamente sobre o estado do projeto a cada etapa por meio de notificações enviadas por e-mail ou SMS. Após a finalização, o pedido é embalado e preparado para entrega. Um(a) Assistente de Logística agenda a entrega, registando a transportadora e a previsão de chegada. O sistema deve gerar a fatura automaticamente e anexá-la ao pedido.
Além disso, o sistema deve permitir a inclusão de pedidos urgentes, que podem alterar a ordem de produção, e gerar relatórios detalhados sobre desempenho, uso de recursos e prazos de entrega, ajudando os gestores na tomada de decisões estratégicas.
"""

def processar_texto(texto):
    # Processar o texto com spaCy
    doc = nlp(texto)
    
    # Destacar frases que contêm palavras-chave e identificar entidades
    def identificador(doc, palavras_chave):
        
        sent_iter = iter(doc.sents)
        
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
                
                if entidades:
                    print(f"Frase: {frase_completa}")
                    print(f"Frase sem vírgulas: {frase_sem_virgulas}")
                    print(f"Entidade(s): {entidades}")
                    print(f"Palavras-chave: {palavras_encontradas}\n\n")
                    
                    print(f"Como {entidades} estão associadas as palavras {palavras_encontradas}?\n")
                    print("-------------------------------------------------------------------\n")
                    
    # Destacar e imprimir as frases que contêm palavras-chave, frases sem vírgulas, entidades e palavras-chave
    identificador(doc, palavras_chave)

    sys.exit()

processar_texto(texto)
