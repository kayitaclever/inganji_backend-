import datetime
import uuid

# Kijani inventory management system 
class Product:
    def __init__(self, name,category, quantity, price,expiry_date,mama_mboga):
    
        # self.image_url=image_url
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category=quantity
        self.expiry_date= expiry_date
        self.mama_mboga=mama_mboga
        total_products=[]
        total_price= 0

        # As our inventory will be having many Products with different properties and categories that can be 
        # confusing. Inganji choose to generate an Universal Unique identity( from the Universal Unique Identifier)
        #  for each product in the stock 


    def generate_sku(self):
        sku = str(uuid.uuid4())[:5].upper()
        return sku


    
    # This function is to calculate the discounted_price(the price  after applying the discount) 
    # discount is a reduction of money from actual price, due to different factors.
    # here Inganji apply discount on Products whose expiry_date is within 2 days or more.




    def get_discounted_price(self):
        if self.expiry_date is not None:
            days_until_expiry = (datetime.datetime.strptime(self.expiry_date, '%Y-%m-%d').date() - datetime.date.today()).days
        
        if days_until_expiry <= 2:
            return self.price * 0.95


        return self.price


    # Inganji get the fruits and vegetables from mama_mboga, actually mama mboga are their suppliers. 
    # what Inganji will get is the Hybrid commussion. This commussion is based on both the price of product 
    # and agrument between mama mboga on the commussion rate.   


    def calculate_hybrid_commission(self):

        # Calculate commission based on product price
        if self.price <= 1000:
            commission_rate= 0.1
            

        else:
            commission_rate=0.15

        commission= commission_rate*self.price   

     
             
        return commission        
    
    # Depending on the agrument between us and mama_mboga, we can come up with the commussion rate
    # this commission rate will be applied to the responding mama_mboga's products only

    def calculate_mama_mboga_commussion(self, commission_rate):
        commission = commission_rate * self.price
        return commission



    # def total_sales_price():

            
        
    # Inganji would like to update the stock after a single sale or more sale.
    # here we pass the sales as a parameter and reduct it from the quantity in stock    
    def update_quantity_after_sale(self, sold_quantity):
        self.quantity -= sold_quantity
        print(f"Updated quantity of {self.sku} after sale: {self.quantity}")

    

    # Inganji would like to update the quantity of stock after mama mboga updating her stock 
    # here we passed the new stock in parameter, and add it to the actual quantity


    def update_quantity_after_stock_arrival(self,new_stock):
        self.quantity+= new_stock
        print(f"updated quantity of {self.sku} after {self.mama_mboga} updated her newstock{self.new_stock}")

    
        
    # Get to know the details of the product
        
    def get_details_on_product(self):
        print(f"name:{self.name} code:{self.sku} price:{self.price} quantity:{self.quantity} expire date{self.expiry_date} supplier{self.mama_mboga}")




# Inganji would like to know all products that a single mama mboga brought 
# and total sales, so as for us we can be 
# able to calculate the total_price and know the amount we will
#  send mama mboga(reducting our commussion)


def get_mama_mboga_sales(purchases, mama_mboga_name):
    # here we are  Filtering  purchases made by a specific mama mboga
    mama_mboga_purchases = [p for p in purchases if p.mama_mboga == mama_mboga_name]

    # the total sales made by  the  specific mama mboga
    total_sales = sum(p.quantity * p.price for p in mama_mboga_purchases)

    #  a list of tuples containing the name of each product and the quantity purchased
    product_quantities = [(p.name, p.quantity) for p in mama_mboga_purchases]

    return product_quantities, total_sales


# def add_product(self,mama_mboga, new_product):
#     products.append(new_product)
#     return products


 

