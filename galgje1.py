import random

woordenlijst = ["python","loop","format","integer","float","google"]

woord = random.choice(woordenlijst).lower()

foute_pogingen = 0
max_foute_pogingen = 6
geraden_letters = []

def gekozen_woord(woord, geraden_letters):
    raadbalk = ''
    for letter in woord:
        if letter in geraden_letters:
            raadbalk += letter + ' '
        else:
            raadbalk += '_ '
    return raadbalk.strip()


print(f"Je mag {max_foute_pogingen} keer fout raden.")
print(gekozen_woord(woord, geraden_letters))

while foute_pogingen < max_foute_pogingen and set(geraden_letters) != set(woord):
    gok = input("Raad een letter: ".lower())

    if len(gok) != 1 or not gok.isalpha():
        print("Vul een letter in: ")
        continue

    if gok in geraden_letters:
        print(f"je hebt '{gok}' al geraden.")

    elif gok in woord:
        print(f"Goed geraden! letter '{gok}' zit in het woord.")
        geraden_letters.append(gok)
    else:
        foute_pogingen += 1
        print(f"Helaas! letter {gok} zit niet in het woord. \n Je hebt nog {max_foute_pogingen - foute_pogingen} pogingen over.")

    print(gekozen_woord(woord, geraden_letters))

if set(geraden_letters) == set(woord):
    print("Goedzo! je hebt het woord geraden \n Het spel is afgelopen.")
else:
    print(f"Helaas je hebt het woord niet geraden. Het woord was '{woord}'. ")



