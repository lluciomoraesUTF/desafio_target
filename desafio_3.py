import json #Importar o json para podermos manipular um arquivo json

verificar_faturamento (dados):
    with open(dados, 'r') as file
    dados = json.load(file)
    faturamento = dados['faturamento']
    