import numpy as np

a = np.array([2,3,4],dtype=np.int) # 确定array的type
print(a.dtype)

b = np.zeros((3,4))
print(b)

c = np.ones((3,4))
print(c)

d = np.empty((3,4),dtype=float) # 选中一块内存进行显示，值不能确定
print(d)

e = np.arange(10,20,2) #有序数列 [10,20),步长为2
print(e)

f = np.arange(12).reshape((3,4)) # 3行4列的有序array 
print(f)

g = np.linspace(1,10,5) # 1到10，共5段,同样可以使用reshape
print(g)

i = np.eye(3) # i矩阵，对角线为1的n*n矩阵
print(i)
