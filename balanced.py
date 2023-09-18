# Define a function is_balanced that checks if a given expression is balanced in terms of brackets.

def is_balanced(expression):
    stack = []  # Initialize an empty stack to store opening brackets

    # Iterate through half of the expression length (rounded up)
    for i in range(int((len(expression) / 2) + 1)):
        # Remove pairs of brackets from the expression
        expression = expression.replace("{}", "")
        expression = expression.replace("()", "")
        expression = expression.replace("[]", "")
        
        # If the expression becomes empty, exit the loop
        if not expression:
            break

    # Check if the final expression is empty, which indicates balanced brackets
    return not len(expression)

# Define two test expressions
expression1 = "([]{})"
expression2 = "([)]"

# Test the is_balanced function with the two expressions and print the results
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
