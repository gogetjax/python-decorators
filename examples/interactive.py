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
                from .basic_examples import run_examples
                run_examples()
            else:
                exec(code)
        except Exception as e:
            print(f"Error: {e}")