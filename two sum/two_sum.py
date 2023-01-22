def twoSum(nums, target):
    # Initialize an empty dictionary
    num_indices = {}
    # Iterate through the array
    for i, num in enumerate(nums):
        # Check if the target minus the current element exists in the dictionary
        if target - num in num_indices:
            # If it does, return the indices
            return [num_indices[target - num], i]
        # If it doesn't, add the current element's index to the dictionary
        num_indices[num] = i
    # If no solution is found, return []
    return []

