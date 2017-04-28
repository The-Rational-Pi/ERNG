from __future__ import division
import numpy as np
import sys
import os
maxfloat = sys.float_info.max

units = ['m','s','kg','A','K','cd','mol','$']
print('///////////////////////////////////////////////')
print('/// THE ENGINEERING RANDOM NUMBER GENERATOR ///')
print('///////////////////////////////////////////////')

num = input("How many random numbers shall I generate? ")
#===============================================================================
#generate the units
f = open('out.docx','w')
for i in range(num):
    mag = np.random.randint(0,11)
    val = 2*10**mag*np.random.random()-10**mag #float between -1e10 and 1e10
    unitnum = np.random.randint(1,20)
    unitarray = [0]*len(units)
    for j in range(unitnum):
        a = np.random.randint(0,len(units)) #random index of units
        sign = np.random.randint(0,2)*2-1 #+1 or -1
        unitarray[a]+=sign

#===============================================================================
#simplify into derived units
    maxpower=3
    derived_units=['Pa','J','C','V']
    definitions={'Pa':[-1,-2,1,0,0,0,0,0],'J':[2,-2,1,0,0,0,0,0],'C':[0,1,0,1,0,0,0,0],'V':[2,-3,1,-1,0,0,0,0]}

    derived_unitarray = [0]*len(units)
    numder=len(derived_units)
    power_array=np.indices(tuple([maxpower*2+1 for x in derived_units]))-maxpower-1
    power_list=[0]*len(derived_units)
    for y in range(len(derived_units)):
        power_list[y]=power_array[y].flatten()
    bestunits=unitarray
    bestpowers=[0]*len(derived_units)
    for x in range(len(power_list[0])):
        newunits=unitarray
        powers=[power_list[y][x] for y in range(len(derived_units))]
        for y in range(len(derived_units)):
            unit=derived_units[y]
            newunits=[newunits[k]-powers[y]*definitions[unit][k] for k in range(len(unitarray))]
            #newunits=list(np.array(newunits)-powers[y]*np.array(definitions[unit]))
        if sum([abs(k) for k in newunits])+sum([abs(k) for k in powers])<sum([abs(k) for k in bestunits])+sum([abs(k) for k in bestpowers]):
            bestpowers=powers
            bestunits=newunits
    derived_unitarray=bestpowers
    unitarray=bestunits
        
#===============================================================================
#write the file
    out_str = '{0:.2f} '.format(val)
    for j in range(len(units)):
        if unitarray[j]!=0:
            if unitarray[j]==1:
                this_str = units[j]+' '
            else:
                this_str = units[j]+'^'+str(unitarray[j])+' '
            out_str+=this_str
            del this_str
    for j in range(len(derived_units)):
        if derived_unitarray[j]!=0:
            if derived_unitarray[j]==1:
                this_str = derived_units[j]+' '
            else:
                this_str = derived_units[j]+'^'+str(derived_unitarray[j])+' '
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
#===============================================================================
#fuck with the strings and make it a proper tex file
for line in f:
    line = line.replace('$','\\$')
    things = line.split(' ')
    t.write('&'+things[0])
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





    

