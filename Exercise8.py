#   Create a list
List = [
    "Jake" "Zac", "Ian", "Ron", "Sam", "Dave"
]

# Create function when user wants to add names to list
def add():
    while True:
            #   store name in added and make it capitalized
            added = input("\nAdd name here: ").capitalize()
            if added.strip() != "" and added.lower() != "show":
                #   if input not black and not 'show' add input to list
                List.append(added)
                #   print 'assist'
                print("\ntype 'show' to show current list")
                print("enter to stop")
            elif added.lower() == "show": # if input = 'show' show list
                    print(f"\n{List}")
            elif added.strip() == "": # if input is blank break out of loop
                 break
            else: # if input is something else, continue loop
                    print("...")     

# Create function when user wants to minus names from list
def minus():
    while True:
            #   store name in minus and make it capitalized
            minus = input("\nRemove name: ").capitalize()
            if minus.strip() != "" and minus.lower() != "show":
                #   if input not black and not 'show' remove input from list
                List.remove(minus)
                #   print 'assist'
                print("\ntype 'show' to show current list")
                print("enter to stop")
            elif minus.lower() == "show": # if input = 'show' show list
                    print(f"\n{List}")
            elif minus.strip() == "": # if input is blank break out of loop
                 break
            else: # if input is something else, continue loop
                    print("...") 

def search(): # Create loop till search is over
     while True:
            print("") # Add space
            #   Ask user the name they want to find
            user = input("Who do you want to find? ").capitalize()
            if user in List: #  if name in list; show where and ask if user wants to find more names
                more = input(f"\n{user} is found at index {List.index(user)}\n\nDo you want to find more? ")
                if more.lower() == "yes": # if yes print space then continue to loop
                    print("")
                elif more.lower() == "no": # if no print okay then ask if want to subtract
                    sub = input("Do you want to remove names? ").lower()
                    if sub == 'yes':
                         minus()
                    else:
                        print("\nOkay")
                        break
                else: # print loading then continue loop
                    print("...")
            else: # If name not in list, print name not in list and 'help'
                help = input("...\n---Sorry name not in list---\ntype:\n'show' to show current list\n'add' to add to list\n'exit' to leave\n")
                if help.lower() == "exit": #    If exit then break loop
                    break
                elif help.lower() == "add": #   if add call add
                     add()
                elif help.lower() == "show": #  if show print list
                     print(f"\n{List}")
                else: # If no help, go back to search
                     print("...")

#   main loop
while True:
    #   Display list and ask user if user wants to add
    a = input(f"This are current names in the list: \n\n{List}\n\nDo you want to add more? ")
    if a == "yes": #    If yes enter loop till adding is finished
        add()
    elif a == "no": #   If no go to search names loop
        search()
        break # exit main loop
    else:
        print("...")
    

