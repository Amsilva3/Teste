from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%a, %b %d, %Y. %H:%M %S")
print(data_e_hora_em_texto)

print(" ")
ListaNomes = []
QtdeNomes = 3
ListaSobrenomes = []
QtdeSobrenomes = 3
DataNascimento = []
QtdeDataNascimento = 3
result = []
while len(ListaNomes) < QtdeNomes or len(ListaSobrenomes) < QtdeSobrenomes or len(DataNascimento) < QtdeDataNascimento:
    Nomes = input("Digite seu nome: ")
    ListaNomes.append(Nomes)
    Sobrenomes = input("Digite seu sobrenome: ")
    ListaSobrenomes.append(Sobrenomes)
    Nascimento = input("Digite a data de Nascimento: ")
    DataNascimento.append(Nascimento)
    continue
if ListaNomes != QtdeNomes or ListaSobrenomes != QtdeSobrenomes or DataNascimento != QtdeDataNascimento:
    for x in zip(ListaNomes, ListaSobrenomes, DataNascimento):
        result.append(x)
    print("")
    print("Nomes:", ListaNomes)
    print("")
    print("Sobrenome:", ListaSobrenomes)
    print("")
    print("Data de Nascimento:", DataNascimento)
    print("")
    print("resultado das duas listas:", result)
    print("")
    print("")

    print("Final do Programa!")
