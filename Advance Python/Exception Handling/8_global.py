a = 18 #global variable
def func():
    global a #Use global variable
    print(a)
def func1():
    
    a = 8 #Local Variable
    print(a)

func1()
func()