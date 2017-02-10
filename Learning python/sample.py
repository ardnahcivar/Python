import sys
import json

x = sys.argv[1]
y = json.loads(x)
print(y['key'])

'''
x = sys.argv[1]
y = json.dumps(x)
print(type(y))
'''
