class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:

    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        result = f"User: {self.user}\n"
        result += "Items:\n"

        for item, cnt in self.products.items():
            result += f"{item.name}: {cnt} pcs.\n"

        return result


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)

cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)

print(cart.get_total())

cart.add_item(apple, 10)

print(cart)
print(cart.get_total())