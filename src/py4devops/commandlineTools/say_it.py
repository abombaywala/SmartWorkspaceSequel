#!/usr/bin/env python

def say_it():
    greeting = 'Hello'
    target = 'Joe'
    message = f'{greeting} {target}'
    print(message)

# We add this line to avoid running function while import
if __name__ == '__main__':
    say_it()