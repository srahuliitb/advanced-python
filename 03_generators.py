def my_generator(num):
  for i in range(num):
    yield i ** 3

value = my_generator(int(9e6))

print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))