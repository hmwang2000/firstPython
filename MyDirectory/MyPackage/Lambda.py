Max=lambda x,y:x*(x>=y)+y*(y>x)
Min=lambda x,y:x*(x<=y)+y*(y<x)

#a=int(input('1:'))
a=12
#b=int(input('2:'))
b=21

print(a*(a>=b))
print(a*(a<b))

print(Max(a,b))
print(Min(a,b))

print("-------------------------------------")

print(True) # True
print(False) # False
print(1) # 1
print(0) # 0
print(True==1) # True
print(True==2) # False 只有1是true，其他值不是
print(True==0) # False
print(False==0) # True
print(False==2) # False 只有0是false，其他值不是
print(True>False) # True
print(True>0) # True
print(False>0) # False
print(False<1) # True
print(False<0) # False
