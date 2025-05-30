def score_upper_section(dice, category):
    """
    Calculate the score for the upper section of the Yahtzee game.
    
    Args:
        dice (list): List of dice values.
        category (int): The category to score (1-6).
        
    Returns:
        int: The score for the given category.
    """
    return sum(d for d in dice if d == category)


def score_three_of_a_kind(dice):
    """
    Calculate the score for the Three of a Kind category.
    
    Args:
        dice (list): List of dice values.
        
    Returns:
        int: The score for Three of a Kind, or 0 if not applicable.
    """
    return sum(d for d in dice if any(dice.count(d) >= 3 for d in set(dice)))


def score_four_of_a_kind(dice):
    """
    Calculate the score for the Four of a Kind category.
    
    Args:
        dice (list): List of dice values.
        
    Returns:
        int: The score for Four of a Kind, or 0 if not applicable.
    """
    return sum(d for d in dice if any(dice.count(d) >= 4 for d in set(dice)))


def score_full_house(dice):
    """
    Calculate the score for the Full House category.
    
    Args:
        dice (list): List of dice values.
        
    Returns:
        int: The score for Full House, or 0 if not applicable.
    """
    unique_dice = set(dice)
    if len(unique_dice) == 2 and any(dice.count(d) == 3 for d in unique_dice):
        return 25
    return 0


def score_small_straight(dice):
    """
    Calculate the score for the Small Straight category.
    
    Args:
        dice (list): List of dice values.
        
    Returns:
        int: The score for Small Straight, or 0 if not applicable.
    """
    sorted_dice = sorted(dice)
    straight_count = 1
    last = sorted_dice[0]
    for d in sorted_dice[1:]:
        straight_count = straight_count + 1 if d == last + 1 else 1
        last = d
        if straight_count == 4:
            return 30
    return 0


def score_large_straight(dice):
    """
    Calculate the score for the Large Straight category.
    
    Args:
        dice (list): List of dice values.
        
    Returns:
        int: The score for Large Straight, or 0 if not applicable.
    """
    if len(set(dice)) == 5:
        return 40
    return 0


def is_yahtzee(dice):
    return len(set(dice)) == 1


def score_yahtzee(dice):
    """
    Calculate the score for the Yahtzee category.
    
    Args:
        dice (list): List of dice values.
        
    Returns:
        int: The score for Yahtzee, or 0 if not applicable.
    """
    if is_yahtzee(dice):
        return 50
    return 0


def score_chance(dice):
    """
    Calculate the score for the Chance category.
    
    Args:
        dice (list): List of dice values.
        
    Returns:
        int: The score for Chance.
    """
    return sum(dice)


def score_yahtzee_bonus(dice, is_yahtzee_played):
    """
    Calculate the Yahtzee bonus score.
    
    Args:
        dice (list): List of dice values.
        yahtzee_score (int): The score for the Yahtzee category.
        
    Returns:
        int: The bonus score for Yahtzee, or 0 if not applicable.
    """
    if len(set(dice)) == 1 and is_yahtzee_played:
        return 100
    return 0

