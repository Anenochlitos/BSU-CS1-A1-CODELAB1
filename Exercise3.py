
Acknwldg = ('No') # Variable to store user input
Des = {
    'name': 'Name: ',
    'hometown': 'Hometown: ',
    'age': 'Age: ',
    'greetings' : 'Hello' 
} # Dictionary to store description strings
Myinfo = { 'name': 'Chrysler', 
          'hometown': 'Philippines', 
          'age': '17'
}


print(Des['greetings']) #   Print greeting message

Username= input('What is your name? ') #    Ask user for input
Userage= input('What is your age? ')
Userhometown = input('Where are you from? ') 

def Acknowledgement(): #    Define a function
    global Username #   Make variable global to use inside function
    repeat = False #    Turning off repeat initially to make sure no bug occurs...
    ans_not_yes = False #   and loop works properly if I ever call it again
    
    Myinfoqstn = input('Would you like to know more about me? ') #  stores user input
    
    repeat = True #   boolean variable to control the while loop

    while repeat == True: #    While loop
        if Myinfoqstn.casefold() == 'Yes'.casefold(): #   Used casefold so input = case insensitive
            print(f'Nice to meet you {Username}, you can check my info below:\n' +
                f'{Des['name']}{Myinfo['name']}\n' +
                f'{Des['hometown']}{Myinfo['hometown']}\n' +
                f'{Des['age']}{Myinfo['age']}') #   Separated lines for readability
        elif Myinfoqstn.casefold() == 'No'.casefold(): 
            print('Please be nice')
            ans_not_yes = True #   Change boolean variable to true to enter next while loop
        else:
            print('Please answer with a Yes or No only')
            Acknowledgement() #     Calls function again
        break #     Breaks the while loop to avoid infinite looping

    while ans_not_yes == True:
        insult = input('Type Yes to continue: ')
        if insult.casefold() == 'Yes'.casefold(): 
            print('You a nice person')
            Acknowledgement()
            break
        else:
            print('Please be good to your kind')
        

'''I defined a program that asks the user for input 
and runs a conditional statement based on their answer until the answer I want is met'''

Acknowledgement() #     Call the function
print('Thank you for your patience, have a great day ahead ;)')