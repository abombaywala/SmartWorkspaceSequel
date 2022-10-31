import re


def double(input):
  '''double input'''
  return input * 2


def triple(input):
  '''Triple input'''
  return input * 3


functions = [double, triple]
for function in functions:
  print(function(3))

items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]
print(sorted(items, key=lambda item: item[2]))

cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
Rostam Batmanglij <rostam@vpwk.com>,
Chris Tomson <ctomson@vpwk.com,
Bobbi Baio <bbaio@vpwk.com'''
email_search = re.search(r'\w+\@\w+\.\w+', cc_list)
print(email_search)
'''
Matching using groups and named groups
'''
matched = re.search(r'(?P<user_name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
print(f'''
name: {matched.group("user_name")}
Secondary Level Domain: {matched.group("SLD")}
Top Level Domain: {matched.group("TLD")}''')

matched = re.findall(r'\w+\@\w+\.\w+', cc_list)
print(matched)

# Compiling
# performance gains can be had by compiling the regular expression into an object. This object can be reused for matches without recompiling:

regex_email = re.compile(r'\w+\@\w+\.\w+')
print(regex_email.search(cc_list))
