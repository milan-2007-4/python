a="abcdef"
b="ABCDEF"
print(a)
print(b)

s="AbbCDEF"
print(s[0])
print(s[4])
print(s[-3])
print(s[-2])

print("")
print(s[1:4])
print(s[:4])
print(s[4:])
print(s[::-1])

print("print using loop")
for char in s:
    print(char)
print("update str")
s="A"+s[1:]
print(s)
s="ABC"
del s
#print("s")
print("this are costem error")
print("replace str")
s="ABCD EF"
s1="H"+s[1:]
s2=s.replace("ABC","abc")
print(s1)
print(s2)
print("find lenth")
print(len(s))
s="HELLO world"
print(s.upper())
print(s.lower())
print("remove space")
s="  ABC  "
print(s.strip())
s="python is fun"
print(s.replace("fun","awesome"))
s1="hellow"
s2="world"
print(s1+" "+s2)
print(s*3)










