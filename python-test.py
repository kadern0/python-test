"""Program that prints hello world"""
#!/usr/bin/python

import json
import numpy as np

a = np.array([5,8,12])

print(a)

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

print("hello world!")
