lista = []


maxElementosParaDigitar = 6


while len(lista) < maxElementosParaDigitar:
    numeroDigitado = int(input("digite um numero: "))
    lista.append(numeroDigitado)
    continue

if len(lista) == maxElementosParaDigitar:
    print("Fim do programa")
