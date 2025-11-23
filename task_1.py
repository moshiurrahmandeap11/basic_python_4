# Palindrome Checker

def is_palindrome(s):
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_s == cleaned_s[::-1]

# Example usage
print(is_palindrome("A man a plan a canal Panama"))  # Should return True
print(is_palindrome("Hello"))  # Should return False