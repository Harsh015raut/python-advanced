#Try --> means simply try or check
while(True):
    print("Press 'q' to quit")
    a = input("Enter a Number:")
    if a == 'q':
        break
    try:
        print("Trying")
        a = int(a)     #Code which might throw execption
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"Your inout resulted as in an error{e}") #Handles the Exception

print("Thanks for playing this game")