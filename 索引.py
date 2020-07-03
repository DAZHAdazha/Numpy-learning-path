import numpy as np

A = np.arange(3,15)
print(A)
print(A[3]) # 通过索引

B = np.arange(3,15).reshape((3,4))
print(B)
print(B[2]) # 输出第2行B
print(B[1][1]) # 输出第一行第一列 也可以写成A[1,1]
print(B[2,:]) # 输出第二行的所有数

print('----------')

# 输出每一行
for row in B:
    print(row)

print('----------')
# 输出每一列,先将B transpose
for column in B.T:
    print(column)

print('----------')
# 输出每一个元素 flat为迭代器,A.flatten()会返回把矩阵压平的单行序列
for item in A.flat:
    print(item)
