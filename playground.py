from decorator_examples import log_calls, repeat, singleton, validate_types

# Basic function decorator
@log_calls
def greet(name):
    return f"Hello, {name}!"

# Decorator with arguments
@repeat(times=3)
def generate_number():
    import random
    return random.randint(1, 10)

# Class decorator
@singleton
class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def connect(self):
        return f"Connected to {self.connection_string}"

# Type validation decorator
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

def interactive_mode():
    print("\n=== Python Decorator Playground ===")
    print("Available decorators: @log_calls, @repeat, @singleton, @validate_types")
    print("Type 'exit()' to quit, 'examples()' to run examples, or enter Python code to execute")
    
    while True:
        try:
            code = input("\n>>> ")
            
            if code.lower() == 'exit()':
                break
            elif code.lower() == 'examples()':
                run_examples()
            else:
                exec(code)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    interactive_mode()