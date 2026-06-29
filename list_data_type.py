#list pro
a=[1,2,2,3,4]
print(a[2])
print(a[0])
for i in a:
    print(i,end="")
a.append('mengo')
for i in a:
    print(i)
print(a.count(2))
a.remove(a[5])
print(a)
a.insert(2,32)
print(a)
s=[1,5,4,2,3,6,7]
s.sort()
print(s)
ind=a.index(4)
print(ind)
total=a.count(2)
print(total)
s.reverse()
print(s)
b=a.copy()
print(b)
del a
#print(a)
n=[['ads',"abc",8+7j],[1,2,3,'mengo']]
print(n)
print(n[1])
print(n[0][2])
print(n[1][2])
