# Python Decorator Playground

An interactive environment for experimenting with Python decorators.

## Available Decorators

1. `@log_calls`
   - Logs function calls with arguments and return values
   - Example: `@log_calls`

2. `@repeat(times)`
   - Repeats a function call multiple times
   - Example: `@repeat(times=3)`

3. `@singleton`
   - Ensures only one instance of a class exists
   - Example: `@singleton`

4. `@validate_types`
   - Validates argument types
   - Example: `@validate_types(x=int, y=str)`

## Usage

1. Run examples:
```python
examples()
```

2. Create your own decorated function:
```python
@log_calls
def my_function(x, y):
    return x + y

result = my_function(5, 3)
```

3. Exit:
```python
exit()
```