print('Hello world!')
a = 10 + 20j
b = 30 + 40j
c = a * b
print(c)
d = list(range(10))
print(d)
'''
Sequences represent ordered and finite collections of items.
Negative numbers can be used to index backward.
'''
my_sequence = "Bill Cheatham"
print(my_sequence.index('a'), my_sequence[-13])
print(my_sequence.index('a', 9, 12))
my_sequence = [0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]
print(len(my_sequence), min(my_sequence), max(my_sequence),
      my_sequence.count(1))
'''
Lists represent an ordered collection of items of any type.
The use of square brackets indicates a list syntax.
Remember that the items in a list can be of different types.
'''
empty = []
mixed = [0, 'a', empty, 'WheelHoss']
print(mixed)
squares = [i * i for i in range(10) if i % 2 == 0]
print(squares)
url = "gt.motomomo.io/v2/api/asset/143"
print(url.split('/'))
print('{1} comes after {0}, but {1} comes before {2}'.format(
  'first', 'second', 'third'))
