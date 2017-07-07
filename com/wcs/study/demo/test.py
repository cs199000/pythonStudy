# -*- coding: UTF-8 -*-
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

import numpy


# 绘制散点图
def drawScatter(x, y, z):
    # 创建散点图
    # 第一个参数为点的横坐标
    # 第二个参数为点的纵坐标
    '''
    pyplot.scatter(heights, weights)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Weights')
    pyplot.title('Heights & Weights Of Male Students')
    pyplot.show()
    '''

    ax = pyplot.subplot(111, projection='3d')  # 创建一个三维的绘图工程

    # 将数据点分成三部分画，在颜色上有区分度
    ax.scatter(x[:1000], y[:1000], z[:1000], c='y')  # 绘制数据点

    ax.set_zlabel('Z')  # 坐标轴
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    pyplot.show()


xList = numpy.random.uniform(0, 4000, size=10000)
yList = numpy.random.uniform(0, 20000, size=10000)
zList = (60 * xList * xList/yList/4000) / (5 * xList/4000 + xList/yList)

drawScatter(xList, yList, zList)
