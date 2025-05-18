from enum import Enum

class Sections(Enum):
    PLAYER = 0
    
    # Upper Sections
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    UPPER_SECTION_BONUS = 7

    # Lower Sections
    THREE_OF_A_KIND = 8
    FOUR_OF_A_KIND = 9
    FULL_HOUSE = 10
    SMALL_STRAIGHT = 11
    LARGE_STRAIGHT = 12
    YAHTZEE = 13
    CHANCE = 14
    YAHTZEE_BONUS = 15

    # Total
    TOTAL = 16