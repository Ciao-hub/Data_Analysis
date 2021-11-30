'''
Date: 2021-08-01 12:01:36
LastEditTime: 2021-09-10 20:11:21
'''
'''
#!/usr/bin/env python3
print("output #1: I am excited to learn Python")

x = 4
y = 5 
z = x + y
print("four plus five equals {0:d}".format(z)) #花括号为占占位符，表示将要传给print一个具体的值，即z
'''

'''
import numpy as np
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
d = np.array([Person("Bob",16),Person("Hanzo",18)])
print(d)
print(d.dtype)
'''
'''
import numpy as np
a1 = np.array([1,2,3])
print(a1)

print('\n')

a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a2)

# print('\n')

# a3 = np.array([
#     [
#         [1,2,3],
#         [4,5,6]
#     ],
#     [
#         [7,8,9],
#         [10,11,12]
#     ]
# ]
# )
# print(a3)
'''
import numpy as np

np.random.seed(5)  
print(str(np.random.random()) + "\n")  

for i in range(5):  
    print(np.random.random())

np.random.seed(5)  
print("\n" + str(np.random.random()) + "\n") 

for i in range(5):  
    np.random.seed(5)  
    print(np.random.random())