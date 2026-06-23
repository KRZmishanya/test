#import numpy as np
#A = np.array([[1, 2], [3, 4]])
#B = np.array([[5, 6], [7, 8]])
#C = A + B
#print(C)
import numpy as np

a = np.ones((3, 4),dtype = int)
b = np.arange(12).reshape((4, 3))
print(a)
print(b)
c = np.dot(a,b)
print(c)