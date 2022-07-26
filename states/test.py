import random

priz = 9

spisok = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}


def lot(spisok, priz):
    summa = 0
    while (round(priz, 2) > 0):
        for i in spisok:
            spisok[i] += round(random.uniform(0, 1), 5)
            priz -= spisok[i]
            print(priz)
    for x in spisok:
        summa += spisok[x]
    return print(spisok, "\n", summa)


print(lot(spisok, priz))
