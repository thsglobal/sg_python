from random import random, randint
import math as m
import my_functions.os_functions

print(m.floor(m.pi))
print(m.pi)
print(m.ceil(m.pi))

print(random())
print(randint(1,100))

print(my_functions.os_functions.work_dir)
print(my_functions.os_functions.num_cpus())

# 3 Ways to install packages using PIP (PIP installs Packages):
# Try to import and use context actions
# Python packages tap at the bottom
# from the terminal "pip install <Package_Name>"

import requests

r = requests.get("https://www.bbc.co.uk")
print(r,type(r))
print(r.status_code)
print(r.content)