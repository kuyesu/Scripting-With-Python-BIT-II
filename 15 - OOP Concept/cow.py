class Cow:
    sound = "Moow"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am {} and my sound is {}".format(self.name, self.sound))


halmet = Cow(str(input("Enter the cow name: ")))
halmet.speak()
help(Cow)