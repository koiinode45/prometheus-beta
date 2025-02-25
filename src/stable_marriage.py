from typing import List, Dict, Tuple

def stable_marriage(men_preferences: List[List[str]], women_preferences: List[List[str]]) -> Dict[str, str]:
    """
    Implement the Gale-Shapley algorithm for the Stable Marriage Problem.
    
    Args:
        men_preferences (List[List[str]]): Preference lists for men, 
            where each sublist contains women ranked from most to least preferred.
        women_preferences (List[List[str]]): Preference lists for women, 
            where each sublist contains men ranked from most to least preferred.
    
    Returns:
        Dict[str, str]: A stable matching where keys are men and values are their matched women.
    
    Raises:
        ValueError: If the input lists are invalid (different lengths, mismatched names, etc.)
    """
    # Validate input
    if not men_preferences or not women_preferences:
        raise ValueError("Preference lists cannot be empty")
    
    if len(men_preferences) != len(women_preferences):
        raise ValueError("Number of men and women must be equal")
    
    # Convert names to sets to validate consistency
    men_names = set(range(len(men_preferences)))
    women_names = set(range(len(women_preferences)))
    
    # Initialize data structures
    matches = {}  # Current matching of women to men
    men_free = list(men_names)  # Initially all men are free
    women_partners = {w: None for w in women_names}  # Current partner of each woman
    men_proposal_index = {m: 0 for m in men_names}  # Track which woman each man will propose to next
    
    # Continue while there are free men
    while men_free:
        # Pick a free man
        man = men_free.pop(0)
        
        # Get his next preferred woman to propose to
        if men_proposal_index[man] >= len(men_preferences[man]):
            raise ValueError(f"Insufficient preferences for man {man}")
        
        woman = men_preferences[man][men_proposal_index[man]]
        men_proposal_index[man] += 1
        
        # If woman is free, accept proposal
        if women_partners[woman] is None:
            matches[man] = woman
            women_partners[woman] = man
        else:
            # Check if woman prefers new man to current partner
            current_partner = women_partners[woman]
            
            # Create preference maps for easy comparison
            woman_prefs = {m: rank for rank, m in enumerate(women_preferences[woman])}
            
            # If new man is preferred, reject current partner
            if woman_prefs.get(man, float('inf')) < woman_prefs.get(current_partner, float('inf')):
                matches[man] = woman
                women_partners[woman] = man
                men_free.append(current_partner)
            else:
                # Revert man to free list
                men_free.append(man)
    
    # Create final matching with names (if applicable)
    return matches