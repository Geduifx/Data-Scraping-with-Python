"""
PyCharm
ctrl+. fold selection.
ctrl+/ comments.
ctrl+p show info.
ctrl+d duplicate line.
ctrl+q see documentation.
ctrl+f search and highlight.
ctrl+r replace.
alt+shift+c shows all recent changes.
ctrl+shift+a find all actions.
ctrl+shift+n navigate files.
ctrl+e recent files, then sift+enter opens duplicate tab.
ctrl+alt+L reformat to fix format issues.
ctrl+alt+I to auto-indent the selection.

Hold pointer at function or object and documentation will show up.
Multiple tabs side by side
TODO list #TODO: example of to do.
Refactor - change variable name in multiple occurrences.
"""

name = input("what's your name?? ")
print("Hello " + name)

# types of variables:
# int - whole number.
# float - number with decimal points.
# bool - boolean, True or False.
# str - string.

birth_year = input("what's your birth year?? ")
age = 2022 - int(birth_year)
print(age)

pirmas = str(input("pirmas skaicius "))
antras = input("antras skaicius ")
print("suma " + str(int(pirmas) + int(antras)))
print("sujungti skaiciai " + pirmas + antras)

course = 'Python for Beginners'
print(course.upper())
print(course)
print(course.find('y')) #0123
print(course.replace('for', '4')) #0123

print(10+3)
print(10/3)
print(10//3)
print(10 % 3)  # returns what is left after division
print(2**3)
x = 10
x = x + 3
x += 3  #same as above line

x = 3 > 2 #returns True, == equal, != not equal
print(x)

price = 25
print(price > 10 and price < 30)
and
or
not

temp = 25
if temp > 30:
    print("it's hot")
    print('drink')
elif temp > 20:
    print('nice day')
elif temp > 10:
    print('cold day')
else:
    print('very cold')
print('done')

weight = int(input("what's your weight? ")) #int converts str to number
units = input('(K)g or (L)bs: ')
if units.upper() == 'K':  # Case sensitive, so covert with upper.
    print("converted to Lbs = " + str(weight / 0.45))
else:
    print ("converted to Kg = " + str(weight * 0.45))

i = 1
while i <= 1_00:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i * 'X')
    i = i + 1

#  Lists.
names = ['John', 'Bob', 'Tom', 'Mary']
print(names)
print(names[1])
print(names[-1])  # last element in list, similar with -2
names[1] = 'Booooooob'  # change second item in list
print(names)
print(names[0:3]) #specific range from list

names = ['John', 'Bob', 'Tom', 'Mary']
print(names)
names.append("Lucy") #add to the list, list."many other functions available"
print(names)
names.insert(0, "Anna")
print(names)
names.remove('Lucy')
print(names)
print("Mary" in names)
print(len(names))
names.clear()
print(names)

names = ['John', 'Bob', 'Tom', 'Mary']
print(names)
for item in names: # for loop (good for sequence of objects), print every item from list
    print(item)
print('----------------')
i = 0 # same but with WHILE
while i < len(names):
    print(names[i])
    i = i +1

numbers = range(5) #range generates range
print(numbers)
for i in numbers:
    print(i)

numbers = range(5, 10, 2) # range: start, end, step
print(numbers)
for x in numbers:
    print(x)

numbers = (1, 2, 3) # tuples use (), while lists use [], tuples can't  be changed.

# Naming: variables_different, functions, ClassesDifferent
# Class is used do define new types which can have methods with atributes.

class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point1 = Point()
# point1."two methods that we defined are available"
point1.draw()

# Inheritance, reusing code, DON'T REPEAT CODE
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass #Python doesn't like empty classes, so we tell to pass this line and don't worry :)
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()


# Dictionary, list of key = value pairs
customer = {
    'name': 'John',
    'age': 30
}
print(customer['name'])
print(customer.get('birthday', 'nothing'))  # key is not available, so instead of error it will show 'nothing'
customer['name']='Tom'#replace value
print(customer['name'])

