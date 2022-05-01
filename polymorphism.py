

#Parent Class Member
class Member:
    name = "Lori"
    account = "B123"
    drink = "Pinot Noir"

    def info(self):
            entry_name = input("Please enter your first name: ")
            entry_account = input("Please enter account number: ")
            entry_drink = input("Please enter your drink of choice: ")
            if (entry_name == self.name and entry_account == self.account):
                print("Hello, {}, and welcome back! Let's get you a {}!".format(entry_name, entry_drink))
            else:
                print("Please enter a correct name and account number.")
                
#Child Class Guest
class Guest(Member):
    name = "unknown"
    email = "guest@gmail.com"
    password = "newpassword"

    def info(self):
            entry_name = input("Please enter your first name: ")
            entry_email = input("Please enter email: ")
            entry_password = input("Please enter your password: ")
            if (entry_name == self.name and entry_email == self.email):
                print("Welcome, {}! Let's grab you a drink!".format(entry_name))
            else:
                print("Please enter a correct name and email address.")

#Child Class Employee
class Employee(Member):
    employee_id = "E234"
    employee_password = "work"


    def info(self):
            entry_name = input("Please enter your first name: ")
            employee_id = input("Please enter your employee id: ")
            employee_password = input("Please enter your employee password: ")
            if (employee_id == self.employee_id and employee_password == self.employee_password):
                print("Hello, {}, time to clock in and enjoy your shift!".format(entry_name))
            else:
                print("Please enter a correct employee id and password.")
    
    












guest = Member()
guest.info()

new = Guest()
new.info()

employee = Employee()
employee.info() 
