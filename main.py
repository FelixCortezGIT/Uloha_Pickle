import pickle

class Countries:
    def __init__(self):
        self.cities = {
            "Slovensko": "Bratislava",
            "Cesko": "Praha",
            "Spojene Kralovstvo": "London",
            "Nemecko": "Berlin",
            "Francuzsko": "Paris"
        }
    def add(self, country, city):
        self.cities[country] = city
    def remove(self, country):
        removed = self.cities.pop(country, None)
        if removed is None:
            print("krajina sa nenasla")
        else:
            print(f"krajina {country} bola odstranena")
    def find(self, country):
        return self.cities.get(country, "krajina sa nenasla")
    def find_by_city(self, city):
        for country, capital in self.cities.items():
            if capital == city:
                return country
        return print("hlavne mesto sa nenaslo")
    def show_all(self):
        for country, city in self.cities.items():
            print(country, "->", city)
    def edit(self, country, new_country, new_city):
        if country not in self.cities:
            print("krajina sa nenasla")
        self.cities[new_country] = new_city
        del self.cities[country]
        print("udaje boli zmenene")
    def save(self):
        with open("capitals.pkl", "wb") as file:
            pickle.dump(self.cities, file)
    def load(self):
        with open("capitals.pkl", "rb") as file:
            self.cities = pickle.load(file)


def wait_enter():
    input("\npokracuj stlacenim enter...")

def menu():
    world = Countries()
    while True:
        print("1) pridaj")
        print("2) odober")
        print("3) zmen udaje")
        print("4) najdi podla krajiny")
        print("5) najdi podla mesta")
        print("6) ukaz cely zoznam")
        print("7) uloz do suboru capitals.pkl")
        print("8) nacitaj zo suboru capitals.pkl")
        print("0) koniec")
        choice = input("tvoja volba: ")
        if choice == "1":
            new_country = input("zadaj nazov krajiny: ").strip()
            new_city = input("zadaj nazov mesta: ").strip()
            world.add(new_country, new_city)
            print(f"krajina {new_country} s hlavnym mestom {new_city} boli pridane do zoznamu")
            wait_enter()
        elif choice == "2":
            country = input("odstran krajinu: ")
            world.remove(country)
            wait_enter()
        elif choice == "3":
            country = input("krajinu ktoru chces prepisat: ")
            new_country = input("nazov novej krajiny: ")
            new_city = input("nazov noveho mesta: ")
            world.edit(country, new_country, new_city)
            wait_enter()
        elif choice == "4":
            country = input("ktoru krajinu hladas: ")
            world.find(country)
            wait_enter()
        elif choice == "5":
            city = input("hladaj mesto: ")
            world.find_by_city(city)
            wait_enter()
        elif choice == "6":
            world.show_all()
            wait_enter()
        elif choice == "7":
            world.save()
            print("zoznam bol ulozeny")
            wait_enter()
        elif choice == "8":
            world.load()
            print("zoznam bol nacitany")
            wait_enter()
        elif choice == "0":
            print("koniec")
            break
        else:
            print("neplatna volba")
            wait_enter()

menu()


#
# world = Countries()
# print(world.find("Slovensko"))
# world.add("Hungary", "Pest")
# world.show_all()
# world.remove("Nemecko")
# world.show_all()
# world.edit("Hungary", "Madarsko", "Budapest")
# world.show_all()
# print(world.find_by_city("Bratislava"))
# world.save()
# world.add("Canada", "Ottawa")
# world2 = Countries()
# world2.load()
# print(world2.cities)
# world.show_all()
