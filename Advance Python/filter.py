def greater_5(num):
    if num>5:
        return True
    else:
        return False
l = [1,2,3,4,5,6,7,8,9]
#Filter syntax
print(list(filter(greater_5,l)))

#Filter makes a list of items for whom the function has returned True.
