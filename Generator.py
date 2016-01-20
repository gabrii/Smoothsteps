import sys
try:
    deg = int(sys.argv[1])
except IndexError:
    deg = 7
der = (deg+1)/2
print 'from sympy import *'
for i in range(deg, -1, -1):
    print 'a'+str(i)+',',
print 'x = symbols("'+ ' '.join(['a_'+str(i) for i in range(deg, -1, -1)]+['x'])+'")'
def derc(i, j):
    l = i+1
    i = 1
    for k in range(j):
        l-=1
        i*=l
    return i
print 'k = ',
for i in range(deg, -1, -1):
    print 'a'+str(i)+'*x**'+str(i),
    if i != 0:
        print '+',
print
print 'r = solve(['
for j in range(0, der,):
    print '\ta'+str(j)+' ,'
    print '\t',
    for i in range(deg, -1+j, -1):
        if j == 1000:
            print 'a'+str(i),
        else:
            print str(derc(i, j))+'*a'+str(i),
        if i != 0+j:
            print '+',
        if i == 0 and j == 0:
            print '-1',
    print ',',
    print
print '],',
print '[',
for i in range(deg, -1, -1):
    print 'a'+str(i)+',',
print '])'

print '''
k = k.subs(r)
text_file = open("functions/{{}}.txt", "w")
text_file.write("f(x) = "+str(k).replace('**', '^')+'\\n')
k = diff(k, x)
i = 1
while k != 0:
	text_file.write('Derivative '+str(i)+' = '+str(k).replace('**', '^')+'\\n')
	i+=1
	k = diff(k, x)
text_file.close()
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.01);
y = [k.subs({'x':i}) for i in x]
plt.ylim(0, 1)
plt.xlim(0, 1)
plt.plot(x, y)
plt.savefig('plots/{{}}.png')'''.replace('{{}}', str(deg))
