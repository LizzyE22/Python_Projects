
#parent class 
class User:
    name = 'Sandy'
    email = ''
    account_number = 9

#child class Employee with unique attributes 
class Employee(User):
    position = 'manager'
    weekly_hours = 40

#child class Client with unique attributes
class Client(User):
    phone_number = ''
    wine_club = True
