"""  LIST  IN PYTHON """


"""this is method of list"""
#1. APPEND
m=[]
m.append("this")
print(m)

#2. CLER
m=["this","apple"]
m.clear()
print(m)

#3. COUNT
m=["this","apple"]
print(m.count("this"))

#4.EXTEND
m=["this","apple"]
s =[]
s.extend(m)
print(s)

#5. INDEX
m=["this","apple"]
print(m.index("this"))

#6. POP
m=["this","apple"]
m.pop(1)
print(m)

#7. REMOVE
m=["this","apple"]
m.remove("this")
print(m)

#8. SORT
m=["this","apple"]
m.sort()
print(m)



# len function in list
l =["banna","apple",456]

print(len(l))

# type function in list
print(type(l))

#constructor in list

l =list((34,54,65))
print(type(l))

#Access of item in list
l =[90,987,"apple"]
print(l[2])
print(l[1:2])

#Check of itme is adject
l = ["apple","banna","eat"]
for x in l:
    if "a" in l:
        print("this is in list")
    else:
        print("not adject")
print(l)

#Change of item of list
l = [34,55,"this",44]
l[2]="change"
print(l)

l[1:3]="check"
print(l)

#Insert in list
l=[23,44,33,"this"]
l.insert(3,"change")
print(l)

#Remove index in list
m=[23,44,33,"this"]
m.pop(1)
print(m)

#Remove specific index
n=["banna","appl","this"]
n.remove("appl")
print(n)

#Del in list
c =[44,45,33,32]
del c[1]
print(c) 


#program
lis=[]
for i in range(3):
    s = input("enter your")
    lis.append(s)
print(lis)

#Question 
lis =[]
for i in range(10):
    s = int(input("enter "))
    if s%4==0:
        print("this is disvisble")
        lis.append(s)
    else:
        print("not divisble")
        
print(lis)