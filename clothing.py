def recomendar_roupa(temp_max, temp_min, chance_chuva, vento):
    """Gera recomendação de vestuário baseada no clima"""
    sensacao = "frio" if temp_max < 20 else "ameno" if temp_max < 26 else "calor"
    
    recomendacoes = []
    
    # Temperatura
    if sensacao == "frio":
        recomendacoes.append("jaqueta ou casaco")
    elif sensacao == "ameno":
        recomendacoes.append("blusa de manga longa ou camiseta com casaco leve")
    else:
        recomendacoes.append("roupas leves, como camiseta e shorts")
    
    # Chuva
    if chance_chuva > 50:
        recomendacoes.append("guarda-chuva é ESSENCIAL hoje")
    elif chance_chuva > 30:
        recomendacoes.append("guarda-chuva é recomendado")
    else:
        recomendacoes.append("guarda-chuva provavelmente não será necessário")
    
    # Vento
    if vento > 30:
        recomendacoes.append("leve um corta-vento, ventos fortes previstos")
    
    return f"Clima {sensacao}. " + " ".join(recomendacoes)
