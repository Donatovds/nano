import random

raad_getal = random.randrange(1,15)

pogingen = 5

for i in range(pogingen):
    aantal_pogingen= pogingen-i

    gok= int(input('raad het getal!'))

    if gok == raad_getal:
        print('Je hebt het juiste getal geraden!')

    if gok != raad_getal:
        print('Je hebt niet het juiste getal geraden')
