from __future__ import division
import numpy as np
import sys
maxfloat = sys.float_info.max

units = ['m','s','kg','A','K','cd','mol','$']
print '///////////////////////////////////////////////'
print '/// THE ENGINEERING RANDOM NUMBER GENERATOR ///'
print '///////////////////////////////////////////////'

num = input("How many random numbers shall I generate? ")

f = open('out.docx','w')

for i in range(num):
    mag = np.random.randint(0,11)
    val = 2*10**mag*np.random.random()-10**mag #float between -1e10 and 1e10
    unitnum = np.random.randint(1,10)
    unitarray = [0]*len(units)
    for j in range(unitnum):
        a = np.random.randint(0,len(units)) #random index of units
        sign = np.random.randint(0,2)*2-1 #+1 or -1
        unitarray[a]+=sign

    out_str = '{0:.2f} '.format(val)
    for j in range(len(units)):
        if unitarray[j]!=0:
            if unitarray[j]==1:
                this_str = units[j]+' '
            else:
                this_str = units[j]+'^'+str(unitarray[j])+' '
            out_str+=this_str
            del this_str
    f.write(out_str+'\n')
f.close()
