### Closures
def outer_func(msg):
    # message = msg

    def inner_func():
        # print(message)
        print(msg)

    return inner_func

# hi_func = outer_func("Hi!") # A function can be stored as a variable.
# bye_func = outer_func("Bye!")
# hi_func()
# bye_func()

### Decorators
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before the {original_function.__name__} function.")
        return original_function(*args, **kwargs)
    return wrapper_function

# @decorator_function # this is same as decorator_display = decorator_function(display)
# def display():
#     print('display function executed.\n')


# @decorator_function
# def display_info(name, age):
#     print(f"display_info function executed with '{name}' and '{age}' arguments\n")

# decorator_display = decorator_function(display)
# decorator_display()
# display()
# display_info("Rahul", 31)

### Logging example for Decorators
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info(f"Executed with args: {args}, and kwargs:{kwargs}")
        return orig_func(*args, **kwargs)
    
    return wrapper

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"\nExecuted in {t2} seconds.\n")
    return wrapper

# @decorator_function
@my_logger
def display_info(name, age):
    print(f"display_info function executed with '{name}' and '{age}' arguments\n")

display_info("Virat", 34)