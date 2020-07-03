import numpy as np

a = np.arange(4)
print(a)

b = a
c = a
d = b
a[0] = 5
print(a)

# 浅拷贝，所有引用都会变化
print(b)
print(c)
print(d)
print('-------------')
b = a.copy() # deep copy
e = b
a[2] = 55
print(a)
print(b) # b不会改变
print(d) # 注意d还是会改变
print(e) # e和b关联，所以不变
