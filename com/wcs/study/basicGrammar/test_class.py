# -*- coding: UTF-8 -*-
class Parent:
    """这是doc文档丫丫"""

    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print self.__class__, '被销毁'

    def __str__(self):
        return '%s,姓名: %s,年龄：%s,selfCount:%d,count: %d' % (self.__doc__,self.name, self.age, self.count, Parent.count)

    def add(self, *arg):
        for a in arg:
            self.count += a
        print self.count

try:
    p = Parent('张三', 22)
    p.add(44, 55, 66)
    print __name__
    print p
except RuntimeError, e:
    print '出错啦。。。', e
except TypeError, e:
    print 'TypeError啦。。。', e
else:
    print '这里是else'
finally:
    print '这里是finally哼哼'
