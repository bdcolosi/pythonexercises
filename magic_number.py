# prompt the user for a number
# compare the number given in magic_number value 

user_input = int(input("Guess the magic number: "))
magic_number = 27 

if user_input == magic_number:
    print("You have read my mind.")
else: 
    print("Sorry you lose!")
