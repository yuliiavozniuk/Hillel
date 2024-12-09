class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f'Item: {self.name}, {self.price}, {self.description}, {self.dimensions}'

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'User: {self.name} {self.surname}, {self.numberphone}'

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        if item in self.products:
            self.total -= self.products[item] * item.price
        self.products[item] = cnt
        self.total += cnt * item.price

    def __str__(self):
        items_str = '\n'.join(f'{item.name}: {cnt} pcs.' for item, cnt in self.products.items())
        return f'User: {self.user.name} {self.user.surname}\nItems:\n{items_str}'

    def get_total(self):
        return self.total




lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)
print(apple)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40

buyer_2 = User("Yuliia", "Vozniuk", "07858884")
print(buyer_2)
cart_2 = Purchase(buyer_2)
cart_2.add_item(lemon, 7)
cart_2.add_item(apple, 9)
print(cart_2)