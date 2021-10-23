cars = []
def main():
    while(True):
        print('Käytettävisssä olevat toiminnot:')
        print('1) Anna auton tiedot')
        print('2) Tulosta autojen tiedot')
        print('0) Lopeta')
        handleCommands()

def handleCommands():
    command = input('Valintasi: ')
    if (command == '0'):
        quit()
    elif (command == '1'):
        model = input('Anna auton merkki: ')
        price = input('Anna auton hinta: ')
        cars.append([model, price])
    elif (command == '2'):
        print('Listalta löytyy seuraavat automerkit ja hinnat:')
        for i in range(len(cars)):
            print(cars[i][0], cars[i][1])
    else:
        print('Tuntematon valinta, yritä uudelleen.')
    print('\n')

if __name__ == "__main__":
    print('Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.')
    main()