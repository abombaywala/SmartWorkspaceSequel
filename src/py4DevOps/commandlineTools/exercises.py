import sys

if sys.stdin and sys.stdin.isatty():
    # running interactively
    print("running interactively from command-line")
else:
    print('Run from Somewhere Else')

def test():
    print('I am the best')

if __name__ == '__main__':
    test()

