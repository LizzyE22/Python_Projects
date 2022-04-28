

sentence = "traveled to "

country_list = ['Spain', 'France', 'Italy', 'Portugal']

def country_function(name):
    lst = []
    for i in country_list:
        msg = "{} {} {}".format(name,sentence,i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('Type your name ')
        if name == '':
            print('Please type something')
        elif name == 'Lizzy':
            print('Sorry, you\'re cancelled')
        else:
            go = False
    lst = country_function(name)
    for i in lst:
        print(i)


myString = "hello world"



get_name()



fName = "Lizzy"
lName = "Esqueda"
print("Hello {} {}, welcome to Python".format(fName, lName))


txt1 = ("My name is {} {}".format(fName, lName))
print(txt1)


x = format(0.5, '%')
print(x)
