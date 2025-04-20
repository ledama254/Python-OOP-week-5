# smartphone.py

# Parent class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # encapsulated attribute

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage

# Child class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, refresh_rate):
        super().__init__(brand, model, storage)
        self.refresh_rate = refresh_rate

    def play_game(self, game_name):
        print(f"Playing {game_name} at {self.refresh_rate}Hz on {self.brand} {self.model} 🎮")

# Test the class
phone1 = Smartphone("Samsung", "S21", 128)
phone1.call("0712345678")
print("Storage:", phone1.get_storage())

gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, 144)
gaming_phone.play_game("PUBG Mobile")
