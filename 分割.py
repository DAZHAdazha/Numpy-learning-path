import numpy as np

A = np.arange(12).reshape((3,4))
print(A)

# split方法可以将4列分为1,2块，但是无法3块
print(np.split(A,2,axis=1)) # 将其分成两列
print(np.split(A,3,axis=0)) # 将其分成三行

print(np.array_split(A,3,axis=1)) # 进行不等分割,4列分为3块

print(np.vsplit(A,3)) # vertical split
print(np.hsplit(A,2)) # horizontal split

