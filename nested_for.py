print("nested for loop")
for i in range(3): 
    for j in range(4): 
        print('i=',i,'\t','j=',j)

print("print piramid")
for i in range(1,6): 
    for j in range(1,i+1): 
        print('* ',end='') 
    print()
