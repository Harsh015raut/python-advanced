a = [3,6,7,8,9,2,4,56,78,99,122]
b = []
for item in a:
    if item%2==0:
        b.append(item)
print(b)

#List comprehension

c = [i for i in a if i%2==0] #-->#Shortcut
print(c)
#List comprehension is an elegant way to buil list based on existing list based on condition.cab be used for dictionary as well as set

t = [1,2,3,4,5,6,7,78,9,9] #Set comprehension
s = {i for i in t}
print(s)