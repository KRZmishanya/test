#import numpy as np
#A = np.array([[1, 2], [3, 4]])
#B = np.array([[5, 6], [7, 8]])
#C = A + B
#print(C)
import numpy as np
a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])
c = a[:, np.newaxis] + b
print(c)
print(np.__version__)