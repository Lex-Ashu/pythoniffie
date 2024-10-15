legal_age = 21

print("-- Welcome to the Hacktoberfest bar! --")

try:
    age = int(input("How old are you? "))
    
    if age >= legal_age:
        print("Enjoy your beer!")
    elif age == 20:
        print("So close... just one more year!")
    elif age > 0:
        print(f"Sorry, {age} is too young for a beer. How about a soda?")
    else:
        print("Age can't be negative. Please enter a valid age.")
        
except ValueError:
    print("Invalid input! Please enter a valid number for age.")
