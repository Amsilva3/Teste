from datetime import datetime

current_date_and_time = datetime.now()
text_date_and_time = current_date_and_time.strftime("%a, %b %d, %Y. %H:%M %S")
print(text_date_and_time)

print(" ")
NameList = []
QuantityNames = 3
LastNameList = []
QuantityLastName = 3
BirthDate = []
QuantityBirthDate = 3
result = []
while len(NameList) < QuantityNames or len(LastNameList) < QuantityLastName or len(BirthDate) < QuantityBirthDate:
    Nomes = input("Enter your Name: ")
    NameList.append(Nomes)
    Sobrenomes = input("Enter your Last Name: ")
    LastNameList.append(Sobrenomes)
    Nascimento = input("Enter your Birth Date: ")
    BirthDate.append(Nascimento)
    continue
if NameList != QuantityNames or LastNameList != QuantityLastName or BirthDate != QuantityBirthDate:
    for x in zip(NameList, LastNameList, BirthDate):
        result.append(x)
    print("")
    print("Name:", NameList)
    print("")
    print("Last Name:", LastNameList)
    print("")
    print("Birth date:", BirthDate)
    print("")
    print("List result:", result)
    print("")
    print("")

    print("End of program!")
