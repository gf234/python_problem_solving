import re

s = input()

parser = re.compile(r'^(100+1+|01)+$')
a = re.match(parser, s)
if a:
    print('SUBMARINE')
else:
    print('NOISE')
