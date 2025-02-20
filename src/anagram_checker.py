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
    @staticmethod
    def _clean_word(word: str) -> str:
        """
        Clean a word by removing whitespace and converting to lowercase.
        
        Args:
            word (str): Input word or phrase
        
        Returns:
            str: Cleaned word with only alphanumeric characters
        """
        return ''.join(sorted(char.lower() for char in word if char.isalnum()))
    
    # Clean and sort the words
    word1 = anagram_checker._clean_word(word1)
    word2 = anagram_checker._clean_word(word2)
    
    # Compare cleaned words
    return word1 == word2