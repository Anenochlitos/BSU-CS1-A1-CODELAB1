#   Define password and max attempts
password = "12345" or 12345
attempts = 5

# Create a while loop
while True:
    # Ask user the password 
    answer = input("What's the password? ")
    if answer != password: #    If password is not correct: repeat, unless max attempt reached
        if attempts == 1:
            print("The authorities have been alerted!!")
            break
        else:
            print("Wrong password")
            attempts -=1
            print(f"attempts: {attempts}")
    else:
        print("Correct password")
        break
