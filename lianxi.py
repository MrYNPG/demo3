#coding:utf8
__author__ = 'pengpeng'

print '+++++++++\n++++++++++++++'
print 'python 内建函数的应用\n'
l1 = [1,2,3]
print type(l1)
print  chr(65)
print hex(16)
print oct(8)
print ord('r')
print complex(3)
print float(2)
print long(2)
print tuple([1,2,3])
print tuple({'y':1,'i':2,'n':3})
s = str(1)
print type(s)

ss = '123123123123'
ss1 = ss.replace('1','x')
print ss1

ss2  = ss.replace('1','x',1)
print ss2
ss3 =  ss.replace('1','x',3)
print ss3
print '\n'
import string
str1 = 'hello world'
str2 = string.replace(str1,'hello','nihao')
print str2
#def x(a):
#    for i in a:
#        int(i)
#        if i:
#            return True
#        else:
#            return False
#a = [1,2,3,0]
#print filter(x,a)
def f(x):
    return  x%2!=0 and x% 3 !=0

print list(filter(f,range(1,100)))

def x(a):
        return a-3!=0

print filter(x,range(1,4))

l1 = [1,3,4,5]
l2 = ['yin','peng']

print zip(l2,l1)

def a(x):
    return x+1
print map(a,[1,2,3])


str4 = 'yi/n.p/e/ng'
print str4.capitalize()

ss3 = 'yin/p/eng/hello'
print ss3.split('/')
a = [1,2,3,4]
c = [2,3,4,5]
def b(x,y):
    return x*y
print map(None,a,c)
print map(b,a,c)   # map 先遍历 序列 a 和 c 然后先返回一个元组   再将元组的值返回 函数 b  （函数b  之前已经定义好了）
def a(x,y):
    return x+y
a(2,1)

if a:
    print 'yes'






