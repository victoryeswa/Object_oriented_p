#creation of an class
#store management system ....in the picture
#class Item:
    #pass
    
    #def calculate_total_price(self):

#assigning attributes to instances
#item1 = Item()
#item1.name = 'Phone'
#item1.price = 100
#item1.quantity = 5


#item2 = Item()
#item2.name = 'laptop'
#item2.price = 1000
#item2.quantity = 3
import csv

#solving the above using __init__
class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
    all = []

    def __init__(self, name: str, price, quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f'price {price} not greater than or equal to zero'
        assert quantity >=0, f'quantity {quantity} not greater than or equal to zero'

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity 

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    
Item.instantiate_from_csv()
print(Item.all)


item1 = Item('Phone', 100, 1)
item2 = Item('laptop', 1000, 3)
item3 = Item('Cabe', 1000, 3)
item4 = Item('Mouse', 58, 5)
item5 = Item('Keyboard', 75, 5)

print(Item.all)

for instance in Item.all:
    print(instance.name)


