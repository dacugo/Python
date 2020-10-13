"""
vals = [1,2,3]
vals[0], vals[1] = vals[1], vals[2]
print(vals)


for i in range(1):
    print("#")

else:
    print("#")


var = 0
while var<6:
    var += 1
    if var %2 == 0:
        continue
    print("#")



var = 1
while var<10:
    print("#")
    var = var<<1
    print(var)


a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c+d+e)



lst = [3,1,-2]
print(lst[lst[-1]])



vals = [0,1,2]
vals.insert (0,1)
del vals[1]
print(vals)


nums = [1,2,3]
vals = nums
del vals[1:2]
print(nums)
print(vals)

lst1 = [1,2,3]
lst2 = []
for v in lst1:
    lst2.insert(0,v)
print (lst2)



lst = [1,2,3]
for v in range (len(lst)):
    lst.insert(1,lst[v])
print (lst)

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range (3):
    s += t[i][i]
print (s)


"""

lst = [[0,1,2,3] for i in range(2)]
print (lst[2][0])


