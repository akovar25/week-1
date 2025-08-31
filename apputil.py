

# add code below ...

def palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]




def parentheses(s):
    stack = []
    # Evaluate characters for parentheses
    for char in s:
        # If opening bracket, push to stack
        if char == '(':
            stack.append(char)
        # If closing bracket, check for matching opening bracket
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    # If stack is empty, all parentheses were matched
    return not stack