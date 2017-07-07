# -*- coding: UTF-8 -*-
from numpy import genfromtxt, zeros
from pylab import plot, show, subplot, figure, hist, xlim

# 读取数据为二维数组，target即标签
data = genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
target = genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

print data.shape
print target.shape

# 画二维散点图
plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'ro')
plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'go')
# show()

# 画直方图
xmin = min(data[:, 0])
xmax = max(data[:, 0])

figure()
subplot(411)
hist(data[target == 'setosa', 0], color='b', alpha=.7)
xlim(xmin, xmax)
show()
