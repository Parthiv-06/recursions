def is_palindrome(s):
    # Base case: if the string is empty or has one character
    if len(s) <= 1:
        return True
    # Check the first and last characters
    if s[0] != s[-1]:
        return False
    # Recursive case: check the substring without the first and last characters
    return is_palindrome(s[1:-1])

# Example usage
input_string = "racecar"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
