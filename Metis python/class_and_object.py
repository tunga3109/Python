#Классы стр 170

class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} is a restaurant of {self.cuisine_type} food')
    
    def open_restaurant(self):
        print(f'{self.restaurant_name} is opened at 5 clock')
    
    def set_number_served(self,number):
        self.number_served = number
    
    def increment_number_served(self,num):
        self.number_served += num

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flovers = ['plombir','chocolate','white']
    
    def describe_ice_cream(self):
        for kind in self.flovers:
            print(kind)
    
    def describe_restaurant(self):
        print(f'{self.restaurant_name} is a restaurant of {self.cuisine_type}')

cream = IceCreamStand('Yashka','IceCream')
cream.describe_restaurant()

    


    
#class User:
#
#
#    def __init__(self,first_name,last_name):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.occupation = 'cuisiner'
#        self.login_attempts = 0
#    
#    def describe_user(self):
#        print(f'First name - {self.first_name}\nLast name - {self.last_name}\nOccupation - {self.occupation}')
#    
#    def greet_user(self):
#        print(f'Hello,{self.first_name}')
#    
#    def increment_login_attempts(self):
#        self.login_attempts += 1
#    
#    def reset_login_attempts(self):
#        self.login_attempts -= self.login_attempts
#
#class Privileges():
#    priv = ['разрешено добавлять сообщения','разрешено удалять пользователей','разрешено банить пользователей']
#    
#    def __init__(self,privileges=priv):
#        self.privileges = privileges
#    
#    def show_privileges(self):
#        for privilege in enumerate(self.privileges):
#            print(f'{privilege[0]} - {privilege[1]}')
#
#class Admin(User):
#
#    def __init__(self,first_name,last_name):
#        super().__init__(first_name,last_name)
#        self.privileg = Privileges()
#


    



#admin = Admin('Tunga','Chan')
#admin.privileg.show_privileges()
#print(admin.privileg.priv)

#tung = User('Tunga','Chan')
#tung.increment_login_attempts()
#tung.increment_login_attempts()
#tung.increment_login_attempts()
#tung.increment_login_attempts()
#tung.increment_login_attempts()
#tung.increment_login_attempts()
#print(tung.login_attempts)
#tung.reset_login_attempts()
#print(tung.login_attempts)
#   
#restaurant = Restaurant('Sushi Vesla','Asian')
#restaurant.describe_restaurant()
#restaurant.set_number_served(13)
#print(restaurant.number_served)
#restaurant.increment_number_served(100)
#print(restaurant.number_served)