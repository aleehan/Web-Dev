class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return f"{self.name} makes a generic animal sound"

    def describe(self):
        return f"{self.name} is a {self.age} year old {self.species}"

    def __str__(self):
        return (
            f"Animal({self.name}), age = {self.age}, "
            f"species = {self.species}"
    )

class Dog(Animal):
    def __init__(self, name, age, breed, is_trained = False):
        super().__init__(name, age, species="Dog")
        self.breed = breed
        self.is_trained = is_trained

    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self, item):
        if self.is_trained:
            return f"{self.name} fetches the {item} and brings it back!"
        return f"{self.name} ignores the {item} and runs around."

    def __str__(self):
        trained_status = "trained" if self.is_trained else "not trained"
        return (
            f"Dog(name={self.name!r}, age={self.age}, "
            f"breed={self.breed!r}, trained={trained_status})"
        )


class Cat(Animal):
    def __init__(self, name, age, color, is_indoor=True):
        super().__init__(name, age, species="Cat")
        self.color = color
        self.is_indoor = is_indoor

    def speak(self):
        return f"{self.name} says: Meow~"

    def purr(self):
        return f"{self.name} curls up and purrs ... Purrr."

    def __str__(self):
        location = "indoor" if self.is_indoor else "outdoor"
        return (
            f"Cat(name={self.name!r}, age={self.age}, "
            f"color={self.color!r}, {location})"
        )