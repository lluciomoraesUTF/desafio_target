import json #Importar o json para podermos manipular um arquivo json

def verificarFaturamento (dados):
    with open(dados, 'r') as file: #chama a função para ler o json
        dados = json.load(file) #Carrega o arquivo json para 
        faturamento = dados #define o faturamento com os dados de Json
        valores = [item['valor'] for item in faturamento if item['valor'] > 0] #Chama os valores do faturamento para o json para
        menor_valor = min(valores) #seleciona o valor mínimo para
        maior_valor = max(valores) #seleciona o valor máximo
        media_mensal = sum(valores) / len(valores) #realiza o caluclo da média
        dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal) #verifica quais dias tiveram um valor acima da média mensal
    return { #retorna os valores
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_da_media": dias_acima_da_media
    }

# Caminho para o json
arquivo_json = 'dados.json'

# Processa e imprime os resultaods
resultado = verificarFaturamento(arquivo_json)

print(f"Menor valor de faturamento: {resultado['menor_valor']:.2f}")
print(f"Maior valor de faturamento: {resultado['maior_valor']:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {resultado['dias_acima_da_media']}")