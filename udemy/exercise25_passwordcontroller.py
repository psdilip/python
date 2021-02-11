def password(user_input):
    if len(user_input) < 8:
        return False
    elif len(user_input) > 8:
        return True