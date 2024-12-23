from decorators import log_calls, repeat, singleton, validate_types
import random

@log_calls
def greet(name):
    return f"Hello, {name}!"

@repeat(times=3)
def generate_number():
    return random.randint(1, 10)

@singleton
class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def connect(self):
        return f"Connected to {self.connection_string}"

@validate_types(x=int, y=int)
def add_numbers(x, y):
    return x + y

def run_examples():
    print("\n=== Function Decorator Example ===")
    result = greet("Alice")
    print(f"Result: {result}\n")

    print("=== Decorator with Arguments Example ===")
    numbers = generate_number()
    print(f"Generated numbers: {numbers}\n")

    print("=== Singleton Class Decorator Example ===")
    db1 = Database("mysql://localhost:3306")
    db2 = Database("mysql://localhost:3306")
    print(f"Same instance: {db1 is db2}")
    print(f"Connection: {db1.connect()}\n")

    print("=== Type Validation Decorator Example ===")
    try:
        result = add_numbers(5, 3)
        print(f"Valid addition: {result}")
        result = add_numbers("5", 3)
    except TypeError as e:
        print(f"Type error caught: {e}")