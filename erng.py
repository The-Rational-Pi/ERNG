from __future__ import division
import numpy as np
import sys
import os
maxfloat = sys.float_info.max

units = ['m','s','kg','A','K','cd','mol','$']
print '///////////////////////////////////////////////'
print '/// THE ENGINEERING RANDOM NUMBER GENERATOR ///'
print '///////////////////////////////////////////////'

num = input("How many random numbers shall I generate? ")
#===============================================================================
#generate the file
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
del f
#===============================================================================
#initialise the tex file
t = open('data.tex','w')
t.write('\documentclass{article}\n')
t.write('\usepackage{fullpage}\n')
t.write('\usepackage{amsmath}\n')
t.write('\\begin{document}\n')
t.write('\\begin{align}\n')
#===============================================================================
#load the file in read mode
f = open('out.docx','r')
for line in f:
    line = line.replace('$','\\$')
    things = line.split(' ')
    t.write(things[0])
    for i in range(1,len(things)):
        parts = things[i].split('^')
        if len(parts) == 1:
            t.write('\\text{'+parts[0]+'}'+'\\ ')
        else:
            t.write('\\text{'+parts[0]+'}'+'^{'+parts[1]+'}'+'\\ ')
    t.write('\\\\ \n')

#end the tex document and close the files
t.write('\end{align}')
t.write('\end{document}')
f.close()
t.close()
#===============================================================================
#compile the generated data.tex file into a pdf
os.system('pdflatex '+t.name)





    

