""";;;;;;;;;;;
c=0
while c<=6:
    if (c==3 or c==6):
        break
    else:
        print(c)
    c=c+1
...............

for i in range(1,7):
    if i==3 or i==6:
        continue
    else:
        print(i)

c=1
while c<7:
    if c==3 or c==6:
        continue
    else:
        print(c)
    c=c+1

c=1
while c<50:
    if c%3==0:
        print("fizzzz",c)

    elif c%5==0:
        print("divi by 5",c)
        #continue
    elif c%3==0 and c%5==0:
        print("both",c)

    c=c+1
    .............
    print("even odd using lambda")
l=[1,21,55,44,82,35,22]
print(list(filter(lambda x:x%2==0,l)))
print(list(filter(lambda n:n%2!=0,l)))
................
print("even odd using lambda")
l=[1,21,55,44,82,35,22]
print(list(filter(lambda x:x%2==0,l)))
print(list(filter(lambda n:n%2!=0,l)))
print(list(map(lambda n:n*n,l)))
print(list(reversed(l)))
print(sum(l))
print(list(filter(lambda b:b<80,l)))
print(list(map(lambda w:w*w,l)))
print(list(map(lambda c:c*c*c,l)))

    """
















