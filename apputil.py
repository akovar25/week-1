

# add code below ...

def palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]




def parentheses(s):
    return s.count('(') == s.count(')')