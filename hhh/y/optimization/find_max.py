#!/usr/bin/env python 

import os

# typeNum = os.sys.argv[1]
file = open('./out')
lines = file.readlines()
rst = [i.strip().split(',')[-1] for i in lines]
rst = map(eval, rst)
idx = range(len(rst))
dic = dict(zip(rst, idx))
print 'max: %f' % max(dic)
print 'idx: %d' % (dic[max(dic)]+1)
print 'lines: %d' % (len(lines))
