def calcPercentual(): #função para calcular  porcentual
    sp = 67836.43 #define os valor de SP
    rj = 36678.66 #define os valor de RJ
    mg = 29229.88 #define os valor de MG
    es = 27165.48 #define os valor de ES
    outros = 19849.53 #define os valor de Outros
    total = sp + rj + mg + es + outros #soma todos os valores e cria um total
    sp_percentual = (sp / total) * 100 #calcula o percentual do São Paulo no faturamento da empresa
    rj_percentual = (rj / total) * 100 #calcula o percentual do Rio de Janeiro no faturamento da empresa
    mg_percentual = (mg / total) * 100 #calcula o percentual do Minas Gerais no faturamento da empresa
    es_percentual = (es / total) * 100 #calcula o percentual do Espirito Santo no faturamento da empresa
    outros_percentual = (outros / total) * 100 #calcula o percentual de outros estados no faturamento da empresa
    print(f"O percentual que São Paulo representa no faturamento da distribuidora é {sp_percentual:.2f}%") #printa o valor do percentual
    print(f"O percentual que Rio de Janeiro representa no faturamento da distribuidora é {rj_percentual:.2f}%")#printa o valor do percentual
    print(f"O percentual que Minas Gerais representa no faturamento da distribuidora é {mg_percentual:.2f}%")#printa o valor do percentual
    print(f"O percentual que Espírito Santo representa no faturamento da distribuidora é {es_percentual:.2f}%")#printa o valor do percentual
    print(f"O percentual que outros estados representam no faturamento da distribuidora é {outros_percentual:.2f}%")#printa o valor do percentual

calcPercentual()
