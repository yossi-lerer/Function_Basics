# part 1
# step 1
def greet(name):
    print(f"Hello {name}")
greet("Agent X")
# part 2
def add(a, b):
    print(f"the result of {a} + {b} is {a + b}")
add(3, 4)
# part 3
def square(n):
    print(f"the square {n}** {n**2}")
square(5)
square(12)
# part 4
def greet_with_title(name, title="Agent"):
    print(f"Hello, {title} {name}")
greet_with_title(name = "yossi")
greet_with_title("Gad", "King")
# part 5
def describe(name, level, active):
    print(f"Name: {name}")
    print(f"Level: {level}")
    print(f"Active: {active}")
describe(level=7, name="yossi", active=True) 
# part 6
def multiply(a, b=2):
    print(f"The result of {a} * {b} is {a * b}")
multiply(5)
multiply(564446546857478945278452157845257854, 354321452145742)