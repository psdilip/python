def temperature (user_input):
    if user_input > 25:
        return "Hot"
    elif user_input >= 15 and user_input <= 25:
        return "Warm"
    elif user_input < 15:
        return "Cold"