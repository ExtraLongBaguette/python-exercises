
items = []

def main():
    while (True):
        print("Ostoslistasi sisältää seuraavat tuotteet:")
        for i in range(len(items)):
            print("- " + str(i) + ") " + items[i])
        print("\n")

        print("Voit valita alla olevista toiminnoista:")
        print("1) Lisää")
        print("2) Poista")
        print("0) Lopeta")

        command()
        print("\n")

def command():
    args = -1
    while (args < 0 or args > 2):
        args = int(input("Valintasi: "))
    if (args == 0):
        quit()
    elif (args == 1):
        name = input("Anna lisättävä tuote: ")
        items.append(name)
    elif (args == 2):
        index = input("Anna poistettavan tuotteen numero: ")
        del items[int(index)]

if __name__ == '__main__':
    main()