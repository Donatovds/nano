import random
Getal = random.randrange(1,11)

AantalPogingen = 5
def raadspel():
    print("Mijn computer heeft een getal tussen de 1-10 bedacht.")

    for i in range(AantalPogingen):
        PogingenOver = AantalPogingen - i

        RaadGetal = int(input('Raad het getal! \n Vul een getal in:'))

        if PogingenOver == 1:
            print('Helaas!, je hebt het getal niet geraden, start opnieuw. ')
            break

        if RaadGetal == Getal:
            print('Je hebt het getal goed geraden! bedankt voor het spelen. ')
            break

        elif RaadGetal != Getal:
            print('Fout! Pobeer het nog een keer. ')

            print(f'Je hebt nog {PogingenOver-1} pogingen over. ')


