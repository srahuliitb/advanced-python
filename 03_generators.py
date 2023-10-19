import sys

### Example 1
def my_generator(num):
    for i in range(num):
      yield i ** 3

value = my_generator(int(9e6))

print(f"Cube of numbers:\n{'-' * 50}")
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))

value = my_generator(9)
value1 = my_generator(900)
value2 = my_generator(90000)
value3 = my_generator(9000000)

print(f"\nSize of generator for 9 values = {sys.getsizeof(value)} bytes.")
print(f"Size of generator for 900 values = {sys.getsizeof(value1)} bytes.")
print(f"Size of generator for 90000 values = {sys.getsizeof(value2)} bytes.")
print(f"Size of generator for 9000000 values = {sys.getsizeof(value3)} bytes.\n")

### Example 2
def infinite_sequence():
    result = 1
    while True:
      yield result
      result *= 5

val = infinite_sequence()

print(f"Infinite Sequence:\n{'-' * 50}")
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
