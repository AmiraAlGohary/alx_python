from add_0 import add

a = 1
b = 2
 
print("{} + {} = {}".format(a, b, add(a,b)))

print("__name__ inside 0-add.py:", __name__)

if __name__ == "__main__":
    print("This is being run directly as a script.")