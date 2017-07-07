# -*- coding: UTF-8 -*-
from numpy import genfromtxt, zeros
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score

# 读取数据为二维数组，target即标签
data = genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
target = genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

t = zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3

classifier = GaussianNB()
'''
classifier.fit(data, t)

print classifier.predict(data[0])


train, test, t_train, t_test = cv.train_test_split(data, t, test_size=0.4, random_state=0)

classifier.fit(train, t_train)
print classifier.score(test, t_test)
'''
scores = cross_val_score(classifier, data, t, cv=6)
print scores
