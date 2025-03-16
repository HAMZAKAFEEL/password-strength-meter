
import re

def check_password_strength(password):
    if len(password) < 6:
        return "Weak (Password too short, should be at least 6 characters)"
    
    strength = 0
    
    if re.search(r'[a-z]', password): 
        strength += 1
    if re.search(r'[A-Z]', password): 
        strength += 1
    if re.search(r'\d', password):  
        strength += 1
    if re.search(r'[@$!%*?&]', password): 
        strength += 1

    if strength == 1:
        return "Weak (Try adding uppercase, numbers, or special characters)"
    elif strength == 2:
        return "Medium (Add more variety for better security)"
    elif strength >= 3:
        return "Strong (Good password!)"


password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)