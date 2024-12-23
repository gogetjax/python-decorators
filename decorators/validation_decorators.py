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