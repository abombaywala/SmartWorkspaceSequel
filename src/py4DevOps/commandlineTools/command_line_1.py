import os
import sys
import subprocess
from pprint import pprint

# System check
print(sys.byteorder)
print(sys.getsizeof(1))
A = 'A'
print(sys.getsizeof(A))
print(sys.platform)

if sys.version_info.major < 3:
    print("You need to update your Python version")
elif sys.version_info.minor < 7:
    print("You are not running the latest version of Python")
else:
    print("All is good.")

# ENV variables
print(os.getcwd())
print(os.environ.get('LOGLEVEL'))
os.environ['LOGLEVEL'] = 'DEBUG'
print(os.environ.get('LOGLEVEL'))
print(os.getpid())

sp = subprocess.run(['ls','-l'],
                            capture_output=True,
                            universal_newlines=True)
print(sp.stdout)
print(sp.stderr)

sp = subprocess.run(['ls','/doesnotexist'],
                            capture_output=True,
                            universal_newlines=True)

print(sp.stdout)
print(sp.stderr)

# Raise error with subprocess, if subprocess has stderr
sp = subprocess.run(['ls', '/doesnotexist'],
                             capture_output=True,
                             universal_newlines=True,
                             check=True)