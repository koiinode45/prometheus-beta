def pancake_sort(arr):
    """
    Implement the pancake sort algorithm.
    
    Pancake sort works by flipping the largest unsorted element to the top 
    and then flipping it to its correct position at the end of the unsorted portion.
    
    Args:
        arr (list): The list to be sorted in ascending order.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-comparable elements.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Check if all elements are comparable
    try:
        sorted(arr)
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # Main pancake sort algorithm
    def flip(sublist, k):
        """Reverse the first k elements of the list."""
        left = 0
        while left < k:
            sublist[left], sublist[k] = sublist[k], sublist[left]
            left += 1
            k -= 1
        return sublist
    
    # Iterate through the list from end to beginning
    for size in range(len(arr), 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = arr[:size].index(max(arr[:size]))
        
        # If max element is not already at the end
        if max_idx != size - 1:
            # If max element is not at the beginning, flip it to the top
            if max_idx != 0:
                arr = flip(arr, max_idx)
            
            # Flip the max element to its correct position
            arr = flip(arr, size - 1)
    
    return arr