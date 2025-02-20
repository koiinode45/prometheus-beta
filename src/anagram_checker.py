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
    # Remove any whitespace and convert to lowercase to normalize input
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Quick check: if lengths are different, they can't be anagrams
    if len(word1) != len(word2):
        return False
    
    # Create character frequency dictionaries 
    char_count1 = {}
    char_count2 = {}
    
    # Count character frequencies for both words
    for char in word1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in word2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare the character frequency dictionaries
    return char_count1 == char_count2