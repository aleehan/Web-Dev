from models import Animal, Dog, Cat


def print_section(title):
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")


def main():

    print_section("Creating Animals")

    generic_animal = Animal(name="Unknown", age=3, species="Creature")
    dog1 = Dog(name="Rex", age=5, breed="German Shepherd", is_trained=True)
    dog2 = Dog(name="Buddy", age=2, breed="Golden Retriever", is_trained=False)
    cat1 = Cat(name="Whiskers", age=4, color="orange", is_indoor=True)
    cat2 = Cat(name="Shadow", age=7, color="black", is_indoor=False)

    print(generic_animal)
    print(dog1)
    print(dog2)
    print(cat1)
    print(cat2)


    print_section("All Animals - describe()")

    animals = [generic_animal, dog1, dog2, cat1, cat2]

    for animal in animals:
        print(animal.describe())


    print_section("Polymorphism - speak()")

    for animal in animals:
        print(animal.speak())


    print_section("Dog-specific: fetch()")

    print(dog1.fetch("ball"))
    print(dog2.fetch("stick"))

    print_section("Cat-specific: purr()")

    print(cat1.purr())
    print(cat2.purr())


    print_section("Filtering - Dogs only")

    dogs = [a for a in animals if isinstance(a, Dog)]
    for dog in dogs:
        print(f"{dog.name} ({dog.breed}) - trained: {dog.is_trained}")

    print_section("Filtering - Cats only")

    cats = [a for a in animals if isinstance(a, Cat)]
    for cat in cats:
        location = "indoor" if cat.is_indoor else "outdoor"
        print(f"{cat.name} ({cat.color}) - {location}")


if __name__ == "__main__":
    main()