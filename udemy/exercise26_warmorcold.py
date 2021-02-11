def temperature(user_input):
    if user_input > 7:
        return "Warm"
    elif user_input <= 7:
        return "Cold"