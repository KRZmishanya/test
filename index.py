# rg = np.random.default_rng(1)
# a = np.array(10* rg.random(12)).reshape(3,4)
# time = np.linspace(0,4,5)
# ind = np.argmax(a,axis=0)
# print(a)
# print(ind)
# a_max = a[ind, range(a.shape[1])]
# print(np.all(a_max == a.max(axis=0)))
#================Some numpy & pandas=================#
import numpy as np
import pandas as pd
import matplotlib as plt

def main():
    time = np.linspace(0,4,5)
    print(time)
