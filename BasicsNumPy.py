__author__ = 'Dhivya'
import numpy as an
a = an.array([1,2,3,4,5,6])
print a
# array([1, 2, 3, 4, 5, 6])
print a.ndim
# 1
print a.shape
#(6L,)
b= a.reshape((3,2))
print b

#{array([[1, 2],
 #      [3, 4],
 #     [5, 6]])

b[0][1]=88
print b

# array([[ 1, 88],
 #      [ 3,  4],
 #      [ 5,  6]])
print a
# array([ 1, 88,  3,  4,  5,  6])
c = a.reshape((3,2)).copy()
print c

#array([[ 1, 88],
 #      [ 3,  4],
 #      [ 5,  6]])
c[0][0] = 99
print c

#array([[99, 88],
 #      [ 3,  4],
 #      [ 5,  6]])
print a
# array([ 1, 88,  3,  4,  5,  6])

print a*2
# array([  2, 176,   6,   8,  10,  12])
print a**2
# array([   1, 7744,    9,   16,   25,   36])

# Use arrays themselves as indices
print a[an.array([2,3,4])]
# Out[27]: array([3, 4, 5])

a >5
#Out[28]: array([False,  True, False, False, False,  True], dtype=bool)
a[a>80]=100
print a
#Out[30]: array([  1, 100,   3,   4,   5,   6])
a.clip(0,4)
# Out[31]: array([1, 4, 3, 4, 4, 4])

print a.dtype
#Out[32]: dtype('int32')

x= an.array([1,2,3,an.NAN,5])
print x
# Out[36]: array([  1.,   2.,   3.,  nan,   5.])
an.isnan(x)
# Out[37]: array([False, False, False,  True, False], dtype=bool)

print x[~an.isnan(x)]
# Out[40]: array([ 1.,  2.,  3.,  5.])
an.mean(x[~an.isnan(x)])
# Out[41]: 2.75






















