class OnOffer:
    def __init__(self, item_name, price, items_on_offer, add_to_cart):
        self.item_name = item_name
        self.price = price
        self.cart = add_to_cart
        self.items_on_offer = items_on_offer
    def check_offers(self):
        self.cart = True
        if self.item_name in self.items_on_offer and self.price in self.items_on_offer:
            self.cart = True
        return self.cart


offer_item = OnOffer("Banana", 200, {"mango":200, "Banana":200 }, False)

print(offer_item.check_offers())
    