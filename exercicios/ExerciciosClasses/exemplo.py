class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

    # Another instance method
    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Create instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing instance attributes
print(f"{dog1.name} is a {dog1.species}.")
print(f"{dog2.name} is a {dog2.species}.")

# Calling instance methods
dog1.bark()
dog2.describe()
