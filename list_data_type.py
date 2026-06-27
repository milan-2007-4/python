#list pro
a=[1,2,2,3,4]
print(a[2])
print(a[0])
for i in a:
    print(i,end="")
a.append('mengo')
for i in a:
    print(i)
x=a.count(2)
a.remove(4)
print(a)

