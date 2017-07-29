# Function
#   Define function
def example():
    print('this code will run')
    z = 4 + 9
    print(z)
#   Call function
example()

print '\n'
# Function Parameters
def simple_addition(num1, num2):
    answer = num1 + num2
    print 'num1 is', num1
    print(answer)
simple_addition(5, 8)

print '\n'
# Function Parameters Defaults
def basic_window(width,height,font='TNR'):
    # let us just print out everything
    print(width, height, font)
basic_window(350, 500)
basic_window(350, 500, font='courier')

print '\n'
# Global and Local Variables
#   Global variable
x = 13
def example(modify):
    print(modify)
    modify += 10
    print(modify)
    return modify

x = example(x)
print(x)
