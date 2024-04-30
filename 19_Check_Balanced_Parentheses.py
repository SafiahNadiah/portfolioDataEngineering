def is_balanced_parentheses(s):
    stack = []
    parentheses_mapping = {')': '(', ']': '[', '}': '{'}
 
    for char in s:
        if char in parentheses_mapping.values():
            stack.append(char)
        elif char in parentheses_mapping.keys():
            if not stack or stack.pop() != parentheses_mapping[char]:
                return False
        else:
            return False
 
    return not stack

"""
def is_balanced_parentheses(s): - This line defines a function named is_balanced_parentheses that takes a string s as input.

stack = [] - This line initializes an empty list called stack. This stack will be used to keep track of the opening parentheses encountered so far.

parentheses_mapping = {')': '(', ']': '[', '}': '{'} - This line defines a dictionary called parentheses_mapping where the keys are closing parentheses (')', ']', '}') and the values are their corresponding opening parentheses ('(', '[', '{'). This mapping is crucial for checking if the closing parentheses match the most recent opening parentheses in the stack.

for char in s: - This line starts a loop over each character (char) in the input string s.

if char in parentheses_mapping.values(): - This condition checks if the current character is an opening parenthesis (i.e., it's a value in parentheses_mapping). If it is, it means we've encountered an opening parenthesis, so we push it onto the stack.

stack.append(char) - This line adds the opening parenthesis to the stack.

elif char in parentheses_mapping.keys(): - This condition checks if the current character is a closing parenthesis (i.e., it's a key in parentheses_mapping). If it is, it means we've encountered a closing parenthesis.

if not stack or stack.pop() != parentheses_mapping[char]: - This line checks if the stack is empty or if the top of the stack (the most recently encountered opening parenthesis) does not match the expected opening parenthesis for the current closing parenthesis (char). If either condition is true, it means the parentheses are not balanced, so the function returns False.

else: - This line handles the case where the current character is neither an opening nor a closing parenthesis. In this case, it means the input string contains invalid characters, so the function immediately returns False.

return not stack - After iterating through all characters in the input string, if the stack is empty, it means all opening parentheses have been matched with their corresponding closing parentheses. Therefore, the function returns True. If the stack is not empty, it means there are unmatched opening parentheses, so the function returns False.

In summary, this function uses a stack to keep track of opening parentheses encountered so far. For each closing parenthesis encountered, it checks if it matches the most recent opening parenthesis on the stack. If the parentheses are balanced, the stack will be empty at the end. If there are unmatched parentheses, the stack will not be empty.
"""
