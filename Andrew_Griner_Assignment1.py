"""This code calculates a person ideal weight based on their height
one must be above 5 feet for this as the base height is 5 foot(60 inches)
Andrew Griner 5/25/2023"""

def height(feet, inches): #this function calculates the user height from feet to inches
    if feet < 0 or inches < 0:
        print("ERROR!Invalid input. Height values must be non-negative.\n") #if given a negative number this is the error msg
        return None
    elif inches > 12:
        print("ERROR! Invalid input. Inches value must be less than or equal to 12.\n") #if someone put more then 12 inches
        return None
    feet_to_inches = feet * 12  # Converting feet to inches
    total_height = feet_to_inches + inches  # adds with the inches the user gave
    return total_height


def calculate_weight(height_inches): #the function actually computing the ideal weight
    if height_inches is None:
        return None
    base_weight = 110  # Starting weight for 5 feet height
    inches_above_5feet = max(0, height_inches - 60)  # Calculate the inches above 5 feet
    ideal_weight = base_weight + (inches_above_5feet * 5)  # Increase weight by 5 pounds for each inch above 5 feet
    return ideal_weight


while True: #while loop so the questions loop until the user inputs 'n'
    try:
        user_height_f = int(input("What is your height in feet? "))
        user_height_i = int(input("What is your height in inches? "))
        total_height = height(user_height_f, user_height_i) #calling function height
        if total_height is None:
            continue
        if total_height < 60: #if statement to read error msg if under 5 foot
            print("ERROR! Your height is less than 5 feet.\n")
            continue
        ideal_weight = calculate_weight(total_height) #calling calculate_weight function
        if ideal_weight is not None:
            print(f"The ideal weight based on your height is {ideal_weight} pounds.\n") #ideal output
    except ValueError: #value error appears if string is given
        print("ERROR! Invalid input. Height values must be integers.\n")

    repeat = input("Do you want to calculate again? (y/n) \n") #loops
    if repeat.lower() == "n":
        break #breaks from the loop

