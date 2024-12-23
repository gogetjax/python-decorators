def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

def validate_types(**expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validate args
            for arg, value in zip(expected_types.keys(), args):
                if not isinstance(value, expected_types[arg]):
                    raise TypeError(f"Argument {arg} must be {expected_types[arg]}")
            
            # Validate kwargs
            for key, value in kwargs.items():
                if key in expected_types and not isinstance(value, expected_types[key]):
                    raise TypeError(f"Argument {key} must be {expected_types[key]}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator