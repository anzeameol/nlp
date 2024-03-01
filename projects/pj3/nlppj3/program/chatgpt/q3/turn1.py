
import re

email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def validate_email(email):
    if re.match(email_regex, email):
        return True
    else:
        return False

# Example usage:
email = "example@example.com"
if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
