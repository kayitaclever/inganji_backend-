from datetime import date
class Customer:
    def __init__(self, name, email, phone, user_id):
        self.name = name
        self.user_id = user_id
        self.email = email
        self.phone = phone
        self.frequency = 0
        self.last_visited = None
    

    def frequency_visit(self):
        self.frequency +=1
        self.last_visited = date.now()
    

    def track_frequency_visit(user_id):
        if user_id in users:
            user = users[user_id]
            user.frequency_visit()
        else:
            user = Customer(user_id)
            user.frequency_visit()
            users[user_id] = user
    



    
