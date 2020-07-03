import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A,B)) # vertical stack 上下合并
print(C)
print(A.shape,B.shape,C.shape)

D = np.hstack((A,B)) # horizontal stack 左右合并
print(D)
print(A.shape,B.shape,D.shape)

E = A[:,np.newaxis] # np.newaxis为在该行/列增加一个维度 该操作为把[1,1,1] => [[1][1][1]]
F = B[:,np.newaxis]
print(E)
print(np.hstack((E,F))) 
print(np.vstack((E,F))) 

G = np.concatenate((A,B,B,A),axis=0) # 此方法可以加入参数axis,0为纵向合并，1为横向合并
print(G)





