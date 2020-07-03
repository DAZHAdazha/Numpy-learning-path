import numpy as np

a = np.random.random((2,4)) # 随机生成2*4的矩阵，每个元素为0-1
print(a)

print(np.sum(a))
print(np.sum(a))
print(np.min(a))
print(np.min(a,axis=1)) # 求出每一行的最小值
print(np.min(a,axis=0)) # 求出每一列的最小值
print(np.max(a))

print('----------------------')

A = np.arange(2,14).reshape((3,4))
print(A)

print(np.argmin(A)) # 求出最小值的索引
print(np.argmax(A)) # 求出最大值的索引
print(np.mean(A)) # 求出平均值 或者A.mean(),也可以写np.average(A)
print(np.median(A)) # 求出中位数
print(np.cumsum(A)) # 求出累加数列
print(np.diff(A)) # 求出每一行的相邻的元素的差
print(np.nonzero(A)) # 求出非0的数 输出有点奇怪
print(np.sort(A)) # 逐行排序
print(np.transpose(A)) # 也可以写写成A.T
print(np.clip(A,5,9)) # 将小于5的元素变成5，将大于9的元素变成9

