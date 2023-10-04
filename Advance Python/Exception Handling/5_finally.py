#Finally is a clause which is executed no matter what the error may occur.
try:
    i = int(input("ENter a Number:"))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We were done finally")