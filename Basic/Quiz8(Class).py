## 
'''
(Output example)
There are total 3 properties in the market.
Sydney Apartment Sold 500000 2015
Lidcombe Duplex Sold 700000 2013
Lidcombe House Rent 2400/1200 2000
'''

class Property:

    # Initialise property 
    def __init__(self, location, property_type, deal_type, price, completion_year):
        self.location = location
        self.property_type = property_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year


    # Show property info
    def show_detail(self):
        print("{} {} {} {} {}".format(self.location, self.property_type, self.deal_type, self.price, self.completion_year))


property_list = []

property_list.append(Property("Sydney", "Apartment", "Sold", "500000", 2015 ))
property_list.append(Property("Lidcombe", "Duplex", "Sold", "700000", 2013 ))
property_list.append(Property("Lidcombe", "House", "Rent", "2400/1200", 2000 ))

print("There are total {} properties in the market.".format(len(property_list)))
for i in property_list:
    i.show_detail()

