import numpy as np

n = np.loadtxt("D:\CodeData\PaperCode\DataSet\LFR2000\LFR0.7\\label.txt")
b = n[:,-1]
print(max(b))