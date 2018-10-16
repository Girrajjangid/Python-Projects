n=int(input("Enter value of n "))
for i in range(1,n):
    for j in range(0,n-i):
        print("-",end="-")
    for j in range(n,n-i,-1):
        print('{}-'.format(chr(96+j)),end="")
    for j in range(n-i+2,n+1):
        print('{}-'.format(chr(96+j)),end="")
    for j in range(0,n-i-1):
        print("-",end="-")
    print('-')
for j in range(n,n-i-1,-1):
        print('{}-'.format(chr(96+j)),end="")
for j in range(n-i+1,n):
        print('{}-'.format(chr(96+j)),end="")
print(chr(96+j+1))
for i in range(n-1,0,-1):
    for j in range(0,n-i):
        print("-",end="-")
    for j in range(n,n-i,-1):
        print('{}-'.format(chr(96+j)),end="")
    for j in range(n-i+2,n+1):
        print('{}-'.format(chr(96+j)),end="")
    for j in range(0,n-i-1):
        print("-",end="-")
    print('-')

        
