class Car():
    def __init__(self, brand, count):
        self.brand = brand
        self.count = count
    
def main():
    brand = input("Anna automerkki: ")
    count = int(input("Anna automerkin lukumäärä varastossa: "))
    a = Car(brand, count)
    print("Varastossa on nyt", a.brand + "-merkkisiä autoja", a.count, "kpl.")
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()