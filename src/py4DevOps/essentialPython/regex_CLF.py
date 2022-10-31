'''
The Apache HTTP server  can be configured to save log files in different formats.
One widely used format is the Common Log Format (CLF). A variety of log analysis tools can understand this format.
Below is the layout of this format:
<IP Address> <Client Id> <User Id> <Time> <Request> <Status> <Size>
'''
import re

line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'

r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
r += r' - (?P<User>\w+) '
r += r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
r += r' (?P<Request>".+")'
print(r)

m = re.search(r, line)

print(m.group('IP'))
print(m.group('User'))
print(m.group('Time'))
print(m.group('Request'))