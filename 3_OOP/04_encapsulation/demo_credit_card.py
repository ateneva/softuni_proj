class CreditCard:
    def __init__(self, number, expiry_date, cvv, name, pin):
        self.number = number
        self.expiry_date = expiry_date
        self._cvv = cvv         # protected attribute
        self.name = name
        self.__pin = pin        # private attribute

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return
        raise ValueError("Old pin is not correct")

class ChildCredit(CreditCard):
    def __init__(self, number, expiry_date, cvv, name, pin, child_name):
        super().__init__(number, expiry_date, cvv, name, pin)
        self.child_name = child_name
        self._cvv = cvv

card = CreditCard(1234567891012345, "2022-10", 256, "Test Name", 7887)

# will raise an attribute error if you try to access mangled variable the usual way
#print(card.__pin)
#print(card.pin)

# the private variable can still be accessed by using the mangled name
# can be seen by stepping through the class in debug mode
print(card._CreditCard__pin)


# VERY BAD PRACTICE
# modifying a private variable outside the class
# card.pin = 123456
# print(card.pin)

# GOOD PRACTICE
card.change_pin(7887, 1234)
print(card._CreditCard__pin)
print(card._cvv)
