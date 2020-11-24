

#*TO DO LIST APPLICATION
import time
from prettytable import PrettyTable


print("\nMy TO-DO LIST")
instructions = "\n1: Enter A or a to add new TO-DO.\n2: Enter D or d to delete TO-DO.\n3: Enter U or u to update TO-DO.\n4: Enter E or e to exit the program.\n5: Enter L or l to check your TO-DO List. "
print(instructions)
my_to_do_list = []

#python package to create beautiful ascii tables for console applications
x = PrettyTable()
#create a separate function for to-do list as we will need this in several places. to avoid code repetition
# we create a simple method and call it whenever we want.
def my_list():
    x.field_names = ["Items Name"]
    for i in my_to_do_list:
        x.add_row([i])
        # sleep the program for one sec to add some suspension
        # time.sleep(1)
    # print(x)
    print(x.get_string(title="TODO List"))


running = True
while running:
    user_input = input("\nWhat do you want to do? (A, D, U, E, L) : ").lower()
    if user_input == "a":
        new_todo = input("\nPlease enter your new TO-DO:  ").lower()
        print(f"Your current TO-DO is : {new_todo}")
        my_to_do_list.append(new_todo)
    elif user_input == "d":
        #loop untill a user enter a correct item name.
        while True:
            item_name = input("\nPlease enter the name of an item you want to delete: ").lower()
            try:
                #check first if the item is present in to-do list
                if item_name in my_to_do_list:
                    #ask user for confirmation if he/she really wants to update or not
                    choice = input(f"Are you sure to delete {item_name} from your TO-DO List? Y/N : ").lower()
                    if choice == "y":
                        #remove the item from to-do list
                        my_to_do_list.remove(item_name)
                        print("Your updated TO-DO List.")
                        #call my_list() function to load all the items in a list
                        my_list()
                        #terminate the while loop
                        break
                else:
                    print("Item not found.")
            except Exception:
                print("Something went wrong.")
    elif user_input == "u":
        #loop untill a user enter a correct item name.
        while True:
            item_name = input("\nPlease enter the name of an item you want to update: ").lower()
            try:
                #check first if the item is present in to-do list
                if item_name in my_to_do_list:
                    #ask user for confirmation if he/she really wants to update or not
                    choice = input(f"\nAre you sure to update {item_name} from your TO-DO List? Y/N : ").lower()
                    if choice == "y":
                        updated_item = input(f"Please enter the name you want to update {item_name} with : ")
                        #get the the index of an item you want to update
                        index = my_to_do_list.index(item_name)
                        #replace the item with your updated item
                        my_to_do_list[index] = updated_item
                        print("Your updated TO-DO List.")
                        #call my_list() function to load all the items in a list
                        my_list()
                        #terminate the while loop
                        break
                else:
                    print("Item not found.")
            except Exception:
                print("Something went wrong.")
    elif user_input == "e":
        ask_user = input("Are you sure to exit? Y/N: ").lower()
        if ask_user == "y":
            running = False
    elif user_input == "l":
        my_list()
    elif user_input == "" or user_input == " ":
        print("Please enter something.")
    else:
        print("Please enter a valid value.")

my_list()

