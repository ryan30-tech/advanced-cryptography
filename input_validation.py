import re

def validate_integer(value):
    try:
        num = int(value)
        return True, num
    except ValueError:
        return False, None

def validate_email(email):
    # Simple regex for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password):
    # Password must be at least 8 chars, contain uppercase, lowercase, digit, and special char
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[@$!%*?&]', password)):
        return True
    return False

# Example usage
user_input = input("Enter a number: ")
is_valid, number = validate_integer(user_input)
print("Valid integer:", is_valid, "Value:", number)

email = input("Enter your email: ")
print("Valid email:", validate_email(email))

password = input("Enter your password: ")
print("Strong password:", validate_password(password))
