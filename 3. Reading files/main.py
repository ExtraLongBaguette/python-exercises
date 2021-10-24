import os

def main():
    filePath = input("Anna tiedoston nimi: ")
    path = os.path.dirname(__file__)
    absPath = os.path.join(path, filePath)
    file = open(absPath)
    rows = file.readlines()
    rows.pop()
    for i in range(len(rows)):
        data = rows[i].split(';')
        print('Kello oli', data[2].replace('\n', '') + ', kun punnittiin marjoja', data[0] + '.')
    
    print('Kiitos ohjelman käytöstä.')

if __name__ == '__main__':
    main()