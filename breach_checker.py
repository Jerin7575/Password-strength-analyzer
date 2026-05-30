def is_breached(password:str):
    common = {"password","123456","qwerty","admin123"}
    return password.lower() in common
