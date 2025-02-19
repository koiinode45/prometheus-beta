def remove_char_length(string: str, char: str) -> int:
    """
    Remove all occurrences of a specific character from a string and return its length.
    
    Args:
        string (str): The input string from which to remove characters
        char (str): The character to be removed from the input string
    
    Returns:
        int: The length of the modified string after removing all occurrences 
             of the specified character
    
    Raises:
        TypeError: If string or char is not a string
        ValueError: If char is not a single character
    """
    # Validate input types
    if not isinstance(string, str):
        raise TypeError("Input 'string' must be a string")
    if not isinstance(char, str):
        raise TypeError("Input 'char' must be a string")
    
    # Validate char is a single character
    if len(char) != 1:
        raise ValueError("Input 'char' must be a single character")
    
    # Remove the specified character and return the length
    modified_string = string.replace(char, '')
    return len(modified_string)