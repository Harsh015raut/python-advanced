#we use map only when we want to apply a thing to all values
def square(num):
    return num*num
l = [2,4,6]
#For applying square function to all values we will use map
print(map(square,l))
print(list(map(square,l)))
#map applies to all items of an input_list
