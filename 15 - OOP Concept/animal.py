class Animal:
    sound = ""
    def __init__(self, name):
        self.name =  name

    def speak(self):
        print("I'm {} and I {}".format(name = self.name, sound = self.sound))

class Dog(Animal):
    sound = "barks"

dog1 = Dog("Halmet")
dog1.speak()


# if __name__ == "__main__":
#     dog = Animal("brk")
#     dog.sound = "barks"
#     dog.name = "Tom"
#     dog.speak()
