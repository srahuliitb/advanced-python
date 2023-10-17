### Closures
def outer_func(msg):
    # message = msg

    def inner_func():
        # print(message)
        print(msg)

    return inner_func

hi_func = outer_func("Hi!") # A function can be stored as a variable.
bye_func = outer_func("Bye!")
# hi_func()
# bye_func()

### Decorators
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before the {original_function.__name__} function.")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function # this is same as decorator_display = decorator_function(display)
def display():
    print('display function executed.\n')

@decorator_function
def display_info(name, age):
    print(f"display_info function executed with '{name}' and '{age}' arguments\n")

# decorator_display = decorator_function(display)
# decorator_display()
display()
display_info("Rahul", 31)