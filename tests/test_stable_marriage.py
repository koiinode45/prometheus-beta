import pytest
from src.stable_marriage import stable_marriage

def test_basic_stable_marriage():
    """Test a simple stable marriage scenario."""
    men_prefs = [
        [1, 0, 2],  # Man 0's preferences 
        [0, 2, 1],  # Man 1's preferences
        [1, 0, 2]   # Man 2's preferences
    ]
    women_prefs = [
        [1, 0, 2],  # Woman 0's preferences
        [0, 2, 1],  # Woman 1's preferences
        [1, 0, 2]   # Woman 2's preferences
    ]
    
    result = stable_marriage(men_prefs, women_prefs)
    
    # Verify matching is complete
    assert len(result) == len(men_prefs)
    
    # Check that the matching is unique (no duplicates)
    assert len(set(result.values())) == len(result)

def test_stable_marriage_named_preferences():
    """Test stable marriage with named preferences."""
    men_prefs = [
        ['Alice', 'Beth', 'Carol'],
        ['Carol', 'Alice', 'Beth'],
        ['Beth', 'Carol', 'Alice']
    ]
    women_prefs = [
        ['Bob', 'Mike', 'John'],
        ['John', 'Bob', 'Mike'],
        ['Mike', 'John', 'Bob']
    ]
    
    # Note: This would need adjustment if actual string-based matching is needed
    result = stable_marriage(
        [[men_prefs[0].index(p) for p in men_prefs[i]] for i in range(len(men_prefs))],
        [[women_prefs[0].index(p) for p in women_prefs[i]] for i in range(len(women_prefs))]
    )
    
    assert len(result) == len(men_prefs)

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Preference lists cannot be empty"):
        stable_marriage([], [])

def test_mismatched_input_length_raises_error():
    """Test that mismatched input lengths raise a ValueError."""
    with pytest.raises(ValueError, match="Number of men and women must be equal"):
        stable_marriage([[0, 1]], [[1, 0], [0, 1]])

def test_insufficient_preferences_raises_error():
    """Test that insufficient preferences raise a ValueError."""
    # Single item with fewer preferences than needed
    with pytest.raises(ValueError, match="Insufficient preferences for man 0"):
        stable_marriage([[0]], [[1]])
    
    # Multiple items, but one has insufficient preferences
    prefs_men = [[0, 1], [1]]  # Second list is too short
    prefs_women = [[0, 1], [1, 0]]
    with pytest.raises(ValueError, match="Insufficient preferences for man 1"):
        stable_marriage(prefs_men, prefs_women)

def test_stable_marriage_large_scenario():
    """Test a larger stable marriage scenario."""
    men_prefs = [
        [1, 0, 3, 2],
        [0, 2, 3, 1],
        [3, 1, 0, 2],
        [2, 0, 1, 3]
    ]
    women_prefs = [
        [2, 1, 3, 0],
        [3, 0, 2, 1],
        [1, 2, 0, 3],
        [0, 3, 1, 2]
    ]
    
    result = stable_marriage(men_prefs, women_prefs)
    
    # Verify match completeness and uniqueness
    assert len(result) == len(men_prefs)
    assert len(set(result.values())) == len(result)

def test_stability_property():
    """
    Verify the stability of the matching.
    A matching is stable if no man-woman pair exists where both prefer 
    each other to their current partners.
    """
    men_prefs = [
        [1, 0, 2],
        [0, 2, 1],
        [1, 0, 2]
    ]
    women_prefs = [
        [1, 0, 2],
        [0, 2, 1],
        [1, 0, 2]
    ]
    
    result = stable_marriage(men_prefs, women_prefs)
    
    # Check stability for every pair
    for man, woman in result.items():
        # Man's preference ranking of current partner
        current_partner_rank = men_prefs[man].index(woman)
        
        # Check against potentially better matches
        for potential_partner in men_prefs[man][:current_partner_rank]:
            # Find this woman's current partner
            current_partner = next(
                k for k, v in result.items() if v == potential_partner
            )
            
            # Woman's preferences
            woman_prefs = women_prefs[potential_partner]
            
            # Ensure neither prefers the other over current partner
            assert (
                woman_prefs.index(current_partner) < woman_prefs.index(man)
            ), f"Instability found between {man} and {potential_partner}"