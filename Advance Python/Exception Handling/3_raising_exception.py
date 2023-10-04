def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not Good")  #Raise is used when we want to give our own exception.
    #We have given our own Error sentence to ValueError.
    
a = increment("6j")
print(a)