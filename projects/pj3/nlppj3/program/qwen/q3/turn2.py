
import re

def is_valid_email(email):
    """
    Validates whether an email address is valid or not.
    """
    # Define the regex pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the match() function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
