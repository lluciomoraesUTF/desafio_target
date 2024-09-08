def calcPercentual():
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    outros = 19849.53
    total = sp + rj + mg + es + outros
    sp_percentual = (sp / total) * 100
    rj_percentual = (rj / total) * 100
    mg_percentual = (mg / total) * 100
    es_percentual = (es / total) * 100
    outros_percentual = (outros / total) * 100   
    print(f"O percentual que São Paulo representa no faturamento da distribuidora é {sp_percentual:.2f}%")
    print(f"O percentual que Rio de Janeiro representa no faturamento da distribuidora é {rj_percentual:.2f}%")
    print(f"O percentual que Minas Gerais representa no faturamento da distribuidora é {mg_percentual:.2f}%")
    print(f"O percentual que Espírito Santo representa no faturamento da distribuidora é {es_percentual:.2f}%")
    print(f"O percentual que outros estados representam no faturamento da distribuidora é {outros_percentual:.2f}%")

calcPercentual()
