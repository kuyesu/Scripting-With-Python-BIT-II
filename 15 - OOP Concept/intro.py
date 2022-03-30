# declare class
class Apple:
    color = ""
    flavour = ""

# Creating instance of a new class
RedApple = Apple()
GreenApple = Apple()

class CreamApple(Apple):
    tree = ""

CreamApple2 = CreamApple()

# accessing the elements of the class
RedApple.color = "Red"
RedApple.flavour = "Sweet"
CreamApple2.color = "Cream"
CreamApple2.flavour = "Sweet"