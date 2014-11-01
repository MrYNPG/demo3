#coding:utf8
__author__ = 'pengpeng'

#try:
#    open('xiao')
#    print 'hello'
#except IOError,msg:
#    print '你所指定的文件不存在'

print'++++++++\n'

d = {'a':1,'b':2,'c':3}
#
#del d['a']
#print d
#
#d.clear()
#print d

#del d
#print d
d1 = d.fromkeys(d,0)
print d1
d1 = {'a':1,'b':2,'c':3}

print d1.get('a')
print d1.get('c','no')
print d.pop('a','ynno')
print d.pop('c','nono')
print d.pop('d','ynno')
print '\n'
d1 = {'a':4,'b':5,'c':6}
d = {'a':1,'b':2,'c':3}
print d.setdefault('a',3)
print d.setdefault('v',9)
d.update(d1)
print d
print d1
print d1.values()

for i in d:

    print i
#元组的拆分
t = (1,2,3,4,5)
q,w,e,r,y = t
print q,w,e,r,y
#字典的操作中
import time

for k,v in d.items():               #   遍历字典  将 键值同时 遍历出来
    print k,
    print v
    #time.sleep(0.1)

#参数传递多个值
def f(*p):
    for i in p:
        print i
f(1,2,3)
print '\n'
def f1(u,**d):
    #print u
    for k,v in  u.items():
        print k,
        print v
f1({'yin':1,"peng":2,'y':4})

def f2(x,*y,**z):
    print x
    print y
    print z

f2(1,y=3)
x = 2
z = 3
y = lambda x,z:x**z
print y
print '\n'
#def cf(x,y):
#    return x+y


sum = reduce(lambda x,y:x+y,range(1,101))
print sum
#help(cmp)
t = cmp(1,3)
t1 = cmp(3,1)
t2  = cmp(1,1)
print t,t1,t2  #  cmp 相等返回 0  前面的大于后面的 返回 1  小于后面的返回 -1

t3 = isinstance(d,tuple)
print t3






