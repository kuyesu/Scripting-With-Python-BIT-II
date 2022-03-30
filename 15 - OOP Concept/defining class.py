# Creating a class and object with class and instance attributes

class Dog:
    # class instance
    attr1 = "Daniel"

    # class attribute
    def __init__(self,name):
        self.name = name

if __name__ == "__main__":
    dog1 = Dog("Rogers")
    dog2 = Dog("Tommy")

    # accessing class attributes
    print("This class attribut {}".format(dog1.__class__.attr1))
    print("Class attribute dog 2 {}".format(dog2.__class__.attr1))

    # accessing the classs instances

    print(f"This is {dog1.name}")
    print(f"This is {dog2.name}")