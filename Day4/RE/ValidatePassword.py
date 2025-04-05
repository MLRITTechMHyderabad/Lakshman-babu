import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):  # Uppercase
        return False
    if not re.search(r'[a-z]', password):  # Lowercase
        return False
    if not re.search(r'[0-9]', password):  # Digit
        return False
    if not re.search(r'[@$!%*?&#]', password):  # Special characters
        return False
    return True

# Test passwords
passwords = ["WeakPass", "Lakshman@25", "NoSpecial1", "short!1", "Secure#123"]

# Checking validity
for pwd in passwords:
    result = "Valid" if is_strong_password(pwd) else "Invalid"
    print(f"{pwd} -> {result}")
