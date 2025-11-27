Dictionary = {
    'France':'Paris',
    'Germany':'Berlin',
    'Italy':'Rome',
    'Spain':'Madrid',
    'Portugal':'Lisbon',
    'Greece':'Athens',
    'Netherlands':'Amsterdam',
    'Belgium':'Brussels',
    'Sweden':'Stockholm',
    'Norway':'Oslo'
} #     made a dictionary for the country and their capital

'''In need of adding the countries and their capital'''

def run(): #    defined the first function 
    print('QUIZ TIME!')
    
    while True: #   stated a while loop
        ready = str(input('Are you ready? '))
        if ready.casefold().strip() == 'yes'.casefold().strip(): #  made it case insensitive and space insensitive
            start() #   goes to a different function
            break #     breaks out of loop
        else:
            print('Say yes ') #     asks the user to say 'yes' or loop goes on
        
def start(): #  defined second function
    correct_ans = 0 #   sets score to 0

    for country, capital in Dictionary.items(): #   made a loop for all items in 'Dictionary'
        answer = str(input(f'What is the capital of {country}? ')) #    ask question
        if answer.casefold().strip() == capital.casefold().strip():
            print('You are correct! Yahay!')
            correct_ans += 1 #   adds to score counter
        else:
            print('You are wrong:(')
    
    if correct_ans >5 and correct_ans<10: #     provides feedback depending on score
        print(f'You got {correct_ans} questions right! Very smart.')
        retry() #  goes to another function
    elif correct_ans <5:
        print(f"You got {correct_ans}/10, it's okay, you'll get em next time!")
        retry()
    elif correct_ans == 5:
        print(f"Nice! you got {correct_ans}/10 - half the mark.")
    else:
        print(f'You got {correct_ans}/10, PERFECT!')
        retry()

def retry(): #  made a function that repeats the first if they want to try again
    retry_ = str(input("Do you want to try again? "))
    if retry_.casefold().strip() == ('yes').casefold().strip():
        run()
    else:
        print('Okay, I understand, have a great day!')


run() #     runs first function