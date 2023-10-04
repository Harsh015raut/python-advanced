def read_file(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} nor found")

read_file("1.txt")
read_file("2.txt")
read_file("3.txt")
