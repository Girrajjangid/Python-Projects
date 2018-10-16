from math import log10
from random import randint
l=[]
di={}
ranges=[]
mid=[]
N=int(input('Enter the quantity of numbers you want :-  '))
for i in range(N):
    l.append(randint(1,500))
new=list(set(l))
new.sort()

classes  = round((1+(3.22 * log10(len(new)))))
interval = round((max(l)-min(l))/classes)

t=min(new)
for i in range(classes+1):
    ranges.append([t,t+interval])
    mid.append((t+t+interval)/2)
    t+=interval
for i in range(classes+1):
    s=0
    for j in range(ranges[i][0],ranges[i][1]+1):
        s += l.count(j)
    di[i] = s

print('  Range\t\tFrequency\t  Mid')

t=min(new)
mean=0
for i in range(classes+1):
    print('%4d' % t ,' -', '%4d' % (t+interval),'\t' ,di[i],'\t\t',mid[i])
    mean+=di[i]*mid[i]
    t+=interval
print('\n\tMean =',(mean/N))
from math import sqrt
print('\tDeviation = ','%.3f'%sqrt(mean/N))


        
        
        
        
    