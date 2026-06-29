tup=()
print(tup)
#using str
tup=("geeks","for")
print(tup)
#using list
li=[1,2,3,4,5]
print(tuple(li))
#using built-in function
tup=tuple("geeks")
print(tup)
t=(12,True,"jam")
#error   t[2]=20
print(t)
for i in t:
    print(i,end=" ")
tup=tuple("geeks")
print(tup[0])
print(tup[3:])
print(tup[:3])
# truple unpacking
tup=("geeks","for","jam")
a,b,c=tup
print(a)
print(b)
print(c)
tu=tuple("kamani scincecollege")
print(t[0])
print(t[1:12:2])
print(t[0:10:3])
print(t[3:1])
print(t[1:15:6])
print(t[10:0:-1])
print(t[15:0:-2])
