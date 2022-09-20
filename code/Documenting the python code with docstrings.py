#Documenting the python code with Docstrings

class Person:
    '''This is Person class'''

    name=""

    def print_name(self):
        '''This is print_name function'''
        print("name")


print(dir(Person)) #prints all the methods in Person along with parent inherited once
print(help(Person)) #prints the functions with documentations in Person class
