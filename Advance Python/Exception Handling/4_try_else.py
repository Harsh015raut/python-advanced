try:
    i = int(input("ENter a Number:"))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We were successfull") #Executed only when try is not going in except i.e. try ran successfully