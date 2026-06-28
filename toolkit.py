# part 1
# step 1
def greet(name):
    print(f"Hello {name}")
greet("Agent X")
# step 2
def add(a, b):
    print(f"the result of {a} + {b} is {a + b}")
add(3, 4)
# step 3
def square(n):
    print(f"the square {n}** {n**2}")
square(5)
square(12)
# step 4
def greet_with_title(name, title="Agent"):
    print(f"Hello, {title} {name}")
greet_with_title(name = "yossi")
greet_with_title("Gad", "King")
# step 5
def describe(name, level, active):
    print(f"Name: {name}")
    print(f"Level: {level}")
    print(f"Active: {active}")
describe(level=7, name="yossi", active=True) 
# step 6
def multiply(a, b=2):
    print(f"The result of {a} * {b} is {a * b}")
multiply(5)
multiply(5, 7)
def print_largest(a, b, c):
    if a >= b and a >= c:
        print(f"the {a} is largest then {b, c}")
    elif b >= a and b >= c:
        print(f"the {b} is largest then {a, c}")
    elif c >= a and c >= b:
        print(f"the {c} is largest then {a, b}")
print_largest(3,8,5)
print_largest(10,2,7)
print_largest(4,4,1)
# step 8
def show_fahrenheit(c):
    print(f"the Celsius convet to Fahrenheit is {(c * 9 / 5) + 32}")
show_fahrenheit(0)
show_fahrenheit(100)
show_fahrenheit(37.5)