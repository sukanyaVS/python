def fun(m):
    for i in range(m):
        yield i

for n in fun(3):
    print(n, end=" ")

def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()

for n in numbers:
  print(n)        