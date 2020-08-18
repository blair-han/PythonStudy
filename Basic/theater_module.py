## Module

# normal price
def price(people):
    print("The price for {} people is ${}.".format(people, people * 15))

# discount price in the morning
def price_morning(people):
    print("The price for {} people in the morning is ${}.".format(people, people * 10))

# discount price for soldier
def price_soldier(people):
    print("The price for {} soldiers is ${}.".format(people, people * 7))
