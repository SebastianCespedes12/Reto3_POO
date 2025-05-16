class MenuItem:
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price
    def calcuar_precio_total(self, items):
        total = 0
        for i in items:
            Total += i.price
        return total
class Beverage(MenuItem):
    def __init__(self, name, price, size:str):
        super().__init__(name, price)
        self.size = size
        if size == "small":
            self.price = 1500
        elif size == "medium":
            self.price = 2000
        else:
            self.price = 3000
class MainCourse(MenuItem):
    def __init__(self, name , price, rice:bool, salad:bool):
        super().__init__(name, price)
        self.rice = rice
        self.salad = salad
        if rice == True:
            self.price += 2000
        if salad == True:
            self.price += 1500
class Apetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.price = price
class Dessert(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.price = price
class Order:
    def __init__(self):
        self.orden = []
    def anadir_orden(self, item: "MenuItem"):
        self.orden.append(item)
    def calcular_precio_total(self):
        total = 0
        for i in self.orden:
            total += i.price
        return total
    def mostrar_orden(self):
        for i in self.orden:
            print(f"{i.name} - {i.price}")
        print(f"Total: {self.calcular_precio_total()}")

if __name__ == "__main__":
    order = Order()
    order.anadir_orden(Beverage("Coca-Cola", 0, "small"))
    order.anadir_orden(MainCourse("Pollo Asado", 10000, rice=True, salad=False))
    order.anadir_orden(Apetizer("Empanada", 2500))
    order.anadir_orden(Dessert("Helado", 3000))
    order.anadir_orden(MainCourse("Carne Encebollada", 12000, rice=True, salad=True))
    order.anadir_orden(Dessert("Torta de chocolate", 3500))
    order.anadir_orden(MainCourse("Pescado frito", 11000, rice=False, salad=True))
    order.anadir_orden(Apetizer("Patacón", 2000))
    order.anadir_orden(Beverage("Coca-Cola", 0, "medium"))
    order.anadir_orden(Beverage("Coca-Cola", 0, "large"))
    order.mostrar_orden()
