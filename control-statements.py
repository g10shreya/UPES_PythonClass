while True:
    # Prompt the user for input
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break  # Exit the loop
    else:
        # Convert the input to a number
        try:
            number = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")
            continue  # Prompt for a new number if input is invalid

        # Determine if the number is positive, negative, or zero
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
