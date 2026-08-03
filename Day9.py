i=1
while i<=10:
    print(i)
    i+=1

j=2
while j<=20:
    print(j)
    j+=2

k=10
while k>=1:
    print(k)
    k-=1

k=1
while k<=10:
    if k==6:
        break
    print(k)
    k+=1

l=0
while l<5:
    l += 1
    if l==3:
        continue
    print(l)


m=7
i=1
while i<=10:
    print(m,"x",i,"=",m*i)
    i=i+1