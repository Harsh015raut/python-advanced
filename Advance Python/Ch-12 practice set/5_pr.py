n = int(input("Enter a number :"))

table = [n*i for i in range(1,11)]
print(str(table))
with open("tables.txt","a") as f:
    f.write(str(table))
    f.write('\n')