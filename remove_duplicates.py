def remove_duplicates(sequence):
    seen = set()        # Initialize an empty set to maintain a record of encountered elements
    result = []         # Create an empty list to collect the unique elements in their original order
    
    for item in sequence:
        if item not in seen:
            seen.add(item)   # Add the element to the set if it hasn't been encountered before
            result.append(item)   # Append the unique element to the result list
    
    return result

# Test case 1
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Expected Output: [2, 3, 4, 5, 6, 7]

# Test case 2
input_sequence2 = [1, 1, 1, 1, 1]
result2 = remove_duplicates(input_sequence2)
print(result2)  # Expected Output: [1] (all elements are duplicates)
