List = []


MaxNumbersToPut = 6


while len(List) < MaxNumbersToPut:
    NumberToBeEntered = int(input("Enter a Number: "))
    List.append(NumberToBeEntered)
    continue

if len(List) == MaxNumbersToPut:
    print("End of Program!")
