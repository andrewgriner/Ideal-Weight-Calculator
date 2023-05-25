//This code calculates the ideal weight based on height, must be over 5 foot for it to work
//Andrew Griner 5/25/2023
#include <iostream> 
#include <limits> // Include the <limits> header for input validation

int height(int feet, int inches) { //function that converts feet into inches to make it easier to calculate
    if (feet < 0 || inches < 0) {
        std::cout << "ERROR! Invalid input. Height values must be non-negative." << std::endl;
        return -1;
    }
    else if (inches >= 12) { //Error msg for the user entering more the 12 inch
        std::cout << "ERROR! Invalid input. Inches value must be less than 12." << std::endl;
        return -1;
    }
    int feet_to_inches = feet * 12;  // Converting feet to inches
    int total_height = feet_to_inches + inches;  // adds with the inches the user gave
    return total_height;
}

int calculate_weight(int height_inches) { //this is the fuction that actually calculates the weight
    if (height_inches == -1) {
        return -1;
    }
    int base_weight = 110;  // Starting weight for 5 feet height
    int inches_above_5feet = std::max(0, height_inches - 60);  // Calculate the inches above 5 feet
    int ideal_weight = base_weight + (inches_above_5feet * 5);  // Increase weight by 5 pounds for each inch above 5 feet
    return ideal_weight;
}

int main() { //main driver function
    std::string repeat;
    do {
        int user_height_f, user_height_i;
        std::cout << "What is your height in feet? ";
        std::cin >> user_height_f;

        // Validate input to ensure it's an integer
        if (std::cin.fail()) {
            std::cin.clear(); // Clear error state
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignore invalid input
            std::cout << "ERROR! Invalid input. Please enter a valid integer." << std::endl;
            continue;
        }

        std::cout << "What is your height in inches? ";
        std::cin >> user_height_i;

        // Validate input to ensure it's an integer
        if (std::cin.fail()) {
            std::cin.clear(); // Clear error state
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignore invalid input
            std::cout << "ERROR! Invalid input. Please enter a valid integer." << std::endl;
            continue;
        }

        int total_height = height(user_height_f, user_height_i);
        if (total_height == -1) {
            continue;
        }

        if (total_height < 60) { //Error msg for someone less then 60 inches tall
            std::cout << "ERROR! Your height is less than 5 feet." << std::endl;
            continue;
        }

        int ideal_weight = calculate_weight(total_height);
        if (ideal_weight != -1) {
            std::cout << "The ideal weight based on your height is " << ideal_weight << " pounds." << std::endl;
        }

        std::cout << "Do you want to calculate again? (y/n) ";
        std::cin >> repeat;
    } while (repeat == "y" || repeat == "Y"); //lopping aspect

    return 0;
}

