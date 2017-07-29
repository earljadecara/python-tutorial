# Introduction
Garage = "Ferrari", "Honda", "Porsche", "Toyota"

for each_car in Garage:
    print(each_car)

print '\n'
# Print function and strings
#   print
print('Single Quotes')
print("double quotes")
#   concatenating int/float on string
print 'can do this for int', 13
print 'can do this for float', 0.13
#   escaping characters
print('you\'ll have success here')
print("you'll have success here too")

print '\n'
# Math
#   Addition
print 1+3
#   Multiplication
print 1*3
#   Subtraction
print 1-3
#   Division(int)
print 1/3
#   Division(float)
print 1/3.0

print '\n'
# Variables
var1 = 13
var2 = 31
var3 = 'Hey!'
print var3, (var1 + var2)

print '\n'
# While loop
condition = 1
print '--Start loop--'
while condition < 10:
    print(condition)
    condition += 1
print '--End loop--'

print '\n'
# For loop
exampleList = [1, 5, 6, 6, 2, 1, 5, 2, 1, 4]

print '--Start loop--'
for x in exampleList:
    print(x)
print '--End loop--'
print '--Start loop--'
for x in range(1, 11):
    print(x)
print '--End loop--'

print '\n'
# If...Else
x = 5
y = 8
if x > 55:
    print('x is greater than 55')
else:
    print('x is not greater than 55')

print '\n'
# If...Elif...Else
x = 5
y = 10
z = 22
if x > y:
    print('x is greater than y')
elif x < z:
    print('x is less than z')
else:
    print('if and elif never ran...')