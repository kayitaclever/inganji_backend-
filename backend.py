# AVAILABLE GROCERIES
# mygroceries={"watermelon":200, "ovacado":200, "mango":100,"kiwi":20}
class AvailableGroceries:
    def __init__(self,item_name,price,addtobasket, available_groceries) :
        self.item_name=item_name
        self.price=price
        self.addtobasket=addtobasket
        self.groceries = available_groceries
    def add_to_cart(self,add):
        self.add=self.addtobasket
        if self.item_name in self.groceries and self.price in self.groceries:
            self.add==True
            
        else:
            self.add == False

        return self.add

itemOne = AvailableGroceries("kiwi", 200, False, {"kiwi": 200, "mango": 100})

print(itemOne.add_to_cart(False))

        

    