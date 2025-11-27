Dictionary = {
    '1':'31',
    '2':'28',
    '3':'31',
    '4':'30',
    '5':'31',
    '6':'30',
    '7':'31',
    '8':'31',
    '9':'30',
    '10':'31',
    '11':'30',
    '12':'31'
} # Made a dictionary of the month number and days in the month

#   makes a separate function, which is called when the user says it's leap year on month 2/february
def leap_y(ly, m):
    if ly == 'yes': # if leap year then change the number of days in month(2) of dictionary to 29
        Dictionary["2"] = "29"
        print(f"The 2nd month has {Dictionary[m]} days")
    else:
        print(f"The 2nd month has {Dictionary[m]} days")
#   then print the number of days

# Created a main function that asks the user what month they want to know the days to
def month_n():
    month = str(input("Input a number to see its corresponding number of days: "))
    if month == '1':
        print(f"The 1st month has {Dictionary[month]} days")
        #    If month is 2, ask user if it's leap year, if yes call leap_y function
    elif month == '2': 
        #   turns the input to string, lowercases it and removes the spaces
        leap = str(input("Is it leap year? ").lower().strip)
        leap_y(leap, month)
    elif month == '3':
        print(f"The 3rd month has {Dictionary[month]} days")
    elif month in Dictionary:
        print(f"The {month}th month has {Dictionary[month]} days")
    else:
        #   prints message if user input not in Dictionary
        print(f"Sorry the month number:{month}, can't be found")
    
    #   asks the user if they want to try again
    again = input("Do you want to input again? ").lower().strip()
    if again == 'yes':
        month_n()
    elif again =='no':
        print('Okay')
    else:
        print('...')        

#   calls function
month_n()
