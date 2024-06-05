class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print(f"{self.name} the {self.breed} barks.")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print(f"{self.name} the {self.color} cat meows.")

# Membuat objek dari kelas Dog
dog = Dog("Rex", "Golden Retriever")
print(dog.name)  # Output: Rex
print(dog.breed)  # Output: Golden Retriever
dog.sound()  # Output: Rex the Golden Retriever barks.

# Membuat objek dari kelas Cat
cat = Cat("Whiskers", "Black")
print(cat.name)  # Output: Whiskers
print(cat.color)  # Output: Black
cat.sound()  # Output: Whiskers the Black cat meows.