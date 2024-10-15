def toon_menu():
    print("\n--TinyGames--")
    print(" Optie 1 Raad Het Getal!")
    print(" Optie 2 Galgje")
    print(" Optie 3 afsluiten")


def optie1():
    print("Je hebt Raad Het Getal gekozen, laten we beginnen.")
    import Raad_het_getal_spelletje_2

def optie2():
    print("Je hebt Galgje gekozen, laten we beginnen.")
    import galgje

def optie3():
    print("Optie 3 afsluiten")


def main():
    while True:
        toon_menu()
        keuze = input("Maak een keuze (1-3): ")

        if keuze == '1':
            optie1()
        elif keuze == '2':
            optie2()
        elif keuze == '3':
            optie3()
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()
