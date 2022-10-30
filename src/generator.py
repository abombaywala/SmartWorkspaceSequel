'''
Generators
You can use generators in a similar way as range objects. They perform some operation on data in chunks as requested. They pause their state in between calls. This means that you can store variables that are needed to calculate output, and they are accessed every time the generator is called.
To write a generator function, use the yield keyword rather than a return statement.
generator keeps track of its state, and hence the variable n in each call to the generator reflects the value previously set.

Q: Implement a Fibonacci generator to print first n fibbonaci numbers:
'''
import sys


def fib():
  first = 0
  last = 1
  while True:
    first, last = last, first + last
    yield first


def print_n_fib(n):
  f = fib()
  for i in range(n):
    print(next(f))


def fib_odd_even(n):
  f = fib()
  for i in range(n):
    j = next(f)
    if j % 2 == 0:
      print(f"{j}  Even")
    else:
      print(f"{j}  Odd")


print_n_fib(10)

list_o_nums = [x for x in range(100)]
gen_o_nums = (x for x in range(100))

print(f"size of list is: {sys.getsizeof(list_o_nums)} bytes.")
print(f"size of generator is: {sys.getsizeof(gen_o_nums)} bytes.")

value = input("Please enter a string:\n")
print(f'You entered {value}')
up_list = [x.upper() for x in "smogtether"]
print(up_list)

fib_odd_even(15)