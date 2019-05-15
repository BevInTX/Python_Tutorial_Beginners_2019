class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark!")


class Cat(Mammal):
    def annoy(self):
        print("annoy")


def main():
    dog = Dog()
    dog.walk()
    dog.bark()
    
    cat = Cat()
    cat.walk()
    cat.annoy()


if __name__ == "__main__":

    main()
