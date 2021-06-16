#Komputer losuje numer, a użytkownik wpisuje swoje propozycje – komputer ocenia, czy podana wartość jest większa czy mniejsza od wylosowanej.
#Liczby możesz odgadywać do skutku. To zadanie jest dobre dla początkujących, ponieważ wykorzystuje podstawową znajomość składni Pythona.

#Czego użyjesz: random, integer, input/output, print while (loop), if / elif /else
import random


zakres = int(input("Podaj do jakiej liczby chcesz odgadywać: "))
findingNumber = int(random.randrange(0,zakres))
GetNumber = int(input("Jaką liczbę wylosowałem? "))

while GetNumber != findingNumber:
    if GetNumber>findingNumber:
        GetNumber=int(input("Za duża. Strzelaj dalej: "))
    elif GetNumber<findingNumber:
        GetNumber=int(input("Za mała. Spróbuj jeszcze raz. "))
print(f"Gratuluje!!! pomyślałem o {findingNumber}")