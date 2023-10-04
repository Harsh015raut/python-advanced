from functools import reduce
l = [1,2,3,4]
sum = lambda a,b: a+b
val = reduce(sum,l)
print(val)


