list1 = [45,776,3,2,True,56.7,"Harsh"]
# for item in list1:
#     print(item)
# #Now i want to get the index of items
# index = 0
# for item in list1:
#     print(item,index)
#     index+=1

#For making index simple we use enumerate
for index,item in enumerate(list1):
    print(index,item)
