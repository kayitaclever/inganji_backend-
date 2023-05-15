# 90% of mamambogas use features phone, which use 2G(They don't display images, video )
# features phone only accept "string".
# it is in this case that Inganji, displays the application in form of string to the feautures phone


class Mamamboga:
    def_init_(self,mama_mboga):
        self.items=[]
        self.sales=[]
        self.income=0
# This is what mamamboga will see in her features phone
    def display_in_feature_phone(self):
        print("----Welcome to Kijani fruits and vegetables account")
        print("1. View your items")
        print("2. View your sales")
        print("3. View your income ")
        print("0.Exit")
#  mamamboga will be able to press one, and take her to the items she has at the Kijani store
# if she doesn't have any item, it will print "No items available at kijani"s  store
    def view_items(self):
        if not self.items:
            print(f"{self.mama_mboga} No items available at  Kijani store")
        else:
            print("items:")   
            for item in self.items:
                print(item)
    #  If mamamboga press 2 on her features phone, she will be able to access, her sales.
    # and know which items are selling most
    def view_sales(self):
        if not self.sales:
            print(f"{self.mama_mboga}you have no sales at Kijani store")

        else:
    
            print(f" {self.mama_mboga}total sales:{self.sales}")

#    if mamamboga press 3, she will be able to view her income
    # total income that will be send using chula
    def view_income(self):
        print(f"Total income: {self.income}" )

    



