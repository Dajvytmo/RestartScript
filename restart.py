import sys
 
# length of arguments
arg_length = len(sys.argv)

# full restart method
def full():
    print("full")

# orig method
def orig():
    print("orig")

# blue method
def blue():
    print("blue")

# green method
def green():
    print("green")

# orig no restart method
def origNR():
    print("orig_no_restart")

# blue no restart method
def blueNR():
    print("blue_no_restart")

# green no restart method
def greenNR():
    print("green_no_restart") 

# full restart
if arg_length == 1:
    full()

# orig, blue and green
elif arg_length == 2 :
    
    if sys.argv[1] == "orig":
        orig()

    elif sys.argv[1] == "blue":
        blue()

    elif sys.argv[1] == "green":
        green()

    else:
        print("Wrong argument")

# blue and green with no restart
elif arg_length == 3:

    if sys.argv[1] == "orig":
        if sys.argv[2] == "norestart":
            origNR()
        else:
            print("Wrong argument")

    elif sys.argv[1] == "blue":
        if sys.argv[2] == "norestart":
            blueNR()
        else:
            print("Wrong argument")

    elif sys.argv[1] == "green":
        if sys.argv[2] == "norestart":
            greenNR()
        else:
            print("Wrong argument")

    else:
        print("Wrong argument")

else:
    print("Too many arguments")
