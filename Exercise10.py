''' 
Make a main function that asks user for a number
make function to see if value is odd or even
make function return the value
print returned value from main function'''

#   create function
def oore(value):
    check_odd_even = value%2 #  stores the remainder of user input
    return check_odd_even   #   returns the value when called
        
#   Create main function
def ask():
    while True:
        value = int(input("Input a number: ")) #    ask user for a number then stores it in value
        calculate = oore(value)#    calculate stores the value inside check_odd_even from oore
        if calculate == 0: #    if the value is 0, divisible by 2 then print even, else print odd
            print(f"{value} is even")
        else:
            print(f"{value} is odd")
            #   asks user if want to exit or keep going
        exit = input("type 'exit' to exit\nhit enter to keep going").lower()
        if exit == "exit":
            break   #   if exit is typed then exit loop else print blank line and continue loop
        else:
            print("")


#   if run as main program, call function
if __name__ == "__main__":
    ask()
