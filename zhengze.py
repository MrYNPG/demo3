#coding:utf8
__author__ = 'pengpeng'
print '\n++++正则表达式+++++\n'

import re

s = 'yinpeng'
t = r'^y'
print re.findall(t,s)
