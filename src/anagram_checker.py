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
    # Remove whitespace and convert to lowercase
    word1 = ''.join(word1.lower().split())
    word2 = ''.join(word2.lower().split())
    
    # Compare character counts
    return sorted(word1) == sorted(word2)