def height(feet, inches):
    if feet < 0 or inches < 0:
        print("Invalid input. Height values must be non-negative.")
        return None
    elif inches > 12:
        print("Invalid input. Inches value must be less than or equal to 12.")
        return None
    feet_to_inches = feet * 12  # Converting feet to inches
    total_height = feet_to_inches + inches  # adds with the inches the user gave
    return total_height


def calculate_weight(height_inches):
    if height_inches is None:
        return None
    base_weight = 110  # Starting weight for 5 feet height
    inches_above_5feet = max(0, height_inches - 60)  # Calculate the inches above 5 feet
    ideal_weight = base_weight + (inches_above_5feet * 5)  # Increase weight by 5 pounds for each inch above 5 feet
    return ideal_weight


while True:
    try:
        user_height_f = int(input("What is your height in feet? "))
        user_height_i = int(input("What is your height in inches? "))
        total_height = height(user_height_f, user_height_i)
        if total_height is None:
            continue
        if total_height < 60:
            print("Your height is less than 5 feet.")
            continue
        ideal_weight = calculate_weight(total_height)
        if ideal_weight is not None:
            print(f"The ideal weight based on your height is {ideal_weight} pounds.")
    except ValueError:
        print("Invalid input. Height values must be integers.")

    repeat = input("Do you want to calculate again? (y/n) ")
    if repeat.lower() == "n":
        break

