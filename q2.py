def is_palindrome(string):
    # Remove all non-alphanumeric characters
    string = ''.join(c for c in string if c.isalnum())
    
    # Convert the string to lowercase
    string = string.lower()
    
    # Reverse the string
    rev_string = string[::-1]
    
    # Check if the string is a palindrome
    if string == rev_string:
        return True
    else:
        return False
