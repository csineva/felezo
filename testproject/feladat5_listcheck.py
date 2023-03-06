# Készíts egy Python függvényt, ami egy listát és egy pozitív egész számot vár paraméterként.
#
# Készíts egy új listát, aminek az elemei az eredeti lista azon számai, amik oszthatóak az adott pozitív egész számmal maradék nélkül.
# Az új listával térjen vissza a függvény. A Python programod hívja is meg a függvényt a lentebb található tesztesetekkel
# és jelenítsd meg a terminálon a visszakapott lista elemeit.
#
# Pl:
# function_name([1, 2, 3, 4, 5, 6], 2) => [2, 4, 6])
# function_name([1, 2, 3, 4, 5, 6], 3) => [3,6])
#
# Ezekre tesztelj (legyen meghívva a függvény ezekkel az adatokkal):
# [2,3,4,5,6,7,8], 4 => [4,8]
# [2,3,4,5,6,7,8], 3 => [3,6]
# [2,3,4,5,6,7,8,9,10], 5 => [5,10]

def listcheck(numbers: list, divider: int):
    remainderless = []  # ebben a listában tároljuk el az ellenőrzött számokat

    for number in numbers:  # ciklussal végigiterálunk a numbers lista elemein
        if number % divider == 0:  # ha az adott elem maradék nélkül osztható a divider-el,
            remainderless.append(number)  # akkor eltároljuk a remainderless listában
    return remainderless  # visszatérünk a leválogatott listával


print(listcheck([2, 3, 4, 5, 6, 7, 8], 4))
print(listcheck([1, 2, 3, 4, 5, 6], 3))
print(listcheck([2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
