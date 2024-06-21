class ShoppingItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} x {self.price} = {self.total_price()}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        item = ShoppingItem(name, price, quantity)
        self.items.append(item)

    def display_items(self):
        print("Daftar Belanjaan:")
        for item in self.items:
            print(item)
        print(f"Total Biaya: {self.total_cost()}")

    def total_cost(self):
        return sum(item.total_price() for item in self.items)

def main():
    cart = ShoppingCart()
    while True:
        print("\nTambah item ke keranjang belanja:")
        name = input("Nama item: ")
        price = float(input("Harga item: "))
        quantity = int(input("Jumlah item: "))
        
        cart.add_item(name, price, quantity)
        
        more = input("Tambah item lagi? (y/n): ")
        if more.lower() != 'y':
            break

    cart.display_items()

if __name__ == "__main__":
    main()