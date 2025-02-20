def anagram_checker(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    using all the original letters exactly once.
    
    Args:
        word1 (str): First word to compare
        word2 (str): Second word to compare
    
    Returns:
        bool: True if the words are anagrams, False otherwise
    """
    # Remove whitespace and convert to lowercase, keep only alphanumeric characters
    word1 = ''.join(char.lower() for char in word1 if char.isalnum())
    word2 = ''.join(char.lower() for char in word2 if char.isalnum())
    
    # Compare sorted characters
    return sorted(word1) == sorted(word2)