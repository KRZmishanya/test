# # rg = np.random.default_rng(1)
# # a = np.array(10* rg.random(12)).reshape(3,4)
# # time = np.linspace(0,4,5)
# # ind = np.argmax(a,axis=0)
# # print(a)
# # print(ind)
# # a_max = a[ind, range(a.shape[1])]
# # print(np.all(a_max == a.max(axis=0)))
# #================Some numpy & pandas=================#
# import numpy as np
# import matplotlib as plt

# def main():
#     time = np.linspace(0,4,5)

# import numpy as np
# import matplotlib.pyplot as plt
# def mandelbrot(h, w, maxit=20, r=2):
#     """Returns an image of the Mandelbrot fractal of size (h,w)."""
#     x = np.linspace(-2.5, 1.5, 4*h+1)
#     y = np.linspace(-1.5, 1.5, 3*w+1)
#     A, B = np.meshgrid(x, y)
#     C = A + B*1j
#     z = np.zeros_like(C)
#     divtime = maxit + np.zeros(z.shape, dtype=int)

#     for i in range(maxit):
#         z = z**2 + C
#         diverge = abs(z) > r                    # who is diverging
#         div_now = diverge & (divtime == maxit)  # who is diverging now
#         divtime[div_now] = i                    # note when
#         z[diverge] = r                          # avoid diverging too much
#     print(divtime[500:555,700:750])
#     return divtime
# plt.clf()
# plt.imshow(mandelbrot(500, 500))
# plt.show()
# import numpy as np 
# a = np.arange(4)
# b = np.arange(4,8)
# c = np.arange(8,12)
# d = np.arange(12,16)
# vs = np.ix_(a,b,c,d)
# g = np.dstack((a,b,c))
# print(g)
# print(ax)
# print(bx)
# print(cx)
# print(dx)
# print(np.shape(ax),np.shape(bx),np.shape(cx),np.shape(dx))
# print(ax+dx,'\n',bx+cx)
# print("================ RESULT ===============")
# print((ax+dx)@(bx+cx))
import numpy as np
rg = np.random.default_rng(1)
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = rg.normal(mu, sigma, 10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=200, density=True)       # matplotlib version (plot)
# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=200, density=True)  # NumPy version (no plot)
plt.plot(.5 * (bins[1:] + bins[:-1]), n) 
plt.show()