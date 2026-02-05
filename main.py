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


    # def save(self):
    #
    # def load(self):
    #

world = Countries()
print(world.find("Slovensko"))
world.add("Hungary", "Pest")
world.show_all()
world.remove("Nemecko")
world.show_all()
world.edit("Hungary", "Madarsko", "Budapest")
world.show_all()
print(world.find_by_city("Bratislava"))
