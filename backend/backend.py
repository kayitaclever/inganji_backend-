# class sign up
class signup:
    def __init__(self,First_Name,Last_Name,Email_Address,Phone_No,Account_password,Password_Conf,Delivery_Location) :
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Email_Address=Email_Address
        self.Phone_No=Phone_No
        self.Account_password=Account_password   
        self.Password_Conf=Password_Conf
        self.Delivery_Location=Delivery_Location
    def password_conf(self):
        if(self.Account_password==self.password_conf):
            print( f" Please add your {self.Delivery_Location}")
        else:
            print(f"please enter the correct password")
    def signup_confirmation(self,firstname,lastname,password,confirmation,email,location,signup):
         self.firstname=firstname
         self.lastname=lastname
         self.password=password
         self.cofirmation=confirmation
         self.email=email
         self.location=location
         self.signup=signup
         if(self.First_Name == self.firstname and self.Last_Name ==self.lastname and self.Email_Address ==self.email
            and self.Account_password==self.password and self.Delivery_Location ==self.location):
             self.signup_confirmation==self.signup
