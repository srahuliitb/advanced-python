### Use mypy 06_type_hinting.py to run this fiel.

# This function won't throw any errors
def my_function(param: int) -> str:
    return f"After adding another number = {param + 21}"

# This function will throw error because we are returning a string instead of returning an int as per function signature.
# def bazinga(param: int) -> int:
#     return "Bazinga!"

print(my_function(10))
# print(bazinga(5))

### Example 2
def sum_list_elements(param: list[int]) -> int:
    sum = 0
    for item in param:
        sum += item
    return sum

print(sum_list_elements([1, 2, 3, 4, 5]))
