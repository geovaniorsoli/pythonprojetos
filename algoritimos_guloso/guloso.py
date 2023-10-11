def guloso(frutas_abranger, frutas):
    frutas_selecionadas = []  
    
    while frutas_abranger:
        melhor_fruta = None
        frutas_abrangidas_por_melhor_fruta = set()

        for fruta, frutas_abrangidas in frutas.items():
            comum = frutas_abranger & frutas_abrangidas
            if len(comum) > len(frutas_abrangidas_por_melhor_fruta):
                melhor_fruta = fruta
                frutas_abrangidas_por_melhor_fruta = comum
        
        frutas_abranger -= frutas_abrangidas_por_melhor_fruta
        frutas_selecionadas.append(melhor_fruta)
        del frutas[melhor_fruta] 

    return frutas_selecionadas

frutas_abranger = {
    "maca", "banana", "pera", "uva", 
    "morango",
}

frutas = {
    "frutas1": {"maca", "banana"},
    "frutas2": {"banana", "pera"},
    "frutas3": {"pera", "uva"},
    "frutas4": {"morango", "abacaxi"},
    "frutas5": {"melancia", "kiwi"},
    "frutas6": {"laranja", "limao"},
    "frutas7": {"maca", "limao", "laranja"},
    "frutas8": {"morango", "kiwi", "uva"},
    "frutas9": {"abacaxi", "melancia"},
    "frutas10": {"banana", "uva", "limao"}
}

resultado = guloso(frutas_abranger, frutas)
print("o conjunto que mais contem item é: ", resultado)
