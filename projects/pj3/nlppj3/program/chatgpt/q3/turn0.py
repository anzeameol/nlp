
import re

def validate_email(email):
    # Regular expression for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
email1 = "test@example.com"
email2 = "invalid_email_address"
print(validate_email(email1))  # Output: True
print(validate_email(email2))  # Output: False
