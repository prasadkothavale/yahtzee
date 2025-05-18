import random
from sections import Sections

MAX_ROLLS = 3
MAX_ROUNDS = 13
DICE_COUNT = 5

class Game:
    def __init__(self, player):
        # Initialize score sheet with sections having score = 0 and used = False
        self.score_sheet = (Sections.TOTAL.value + 1) * [(0, False)] 
        
        # Initialize dice with a list of tuples (value, keep)
        self.dice = [(0, False)] * DICE_COUNT

        self.score_sheet[Sections.PLAYER.value] = (player, False)
        self.rolls = 0
        self.rounds = 0
        
    def get_dice_values(self):
        return [d[0] for d in self.dice]
    
    def get_dice_keep(self):
        return [d[1] for d in self.dice]


    def roll_dice(self):
        if self.rolls >= MAX_ROLLS:
            raise Exception("No more rolls left")
        self.rolls += 1
        for i in range(len(self.dice)):
            if not self.dice[i][1]:
                self.dice[i] = (random.randint(1, 6), False)
        return self.dice[:]
    
    def keep_dice(self, dice_to_keep):
        for i in range(len(self.dice)):
            if i in dice_to_keep:
                self.dice[i] = (self.dice[i][0], True)
            else:
                self.dice[i] = (self.dice[i][0], False)
        return self.dice[:]
    
    def __reset_dice(self):
        self.dice = [(0, False)] * DICE_COUNT
        self.rolls = 0
        return self.dice[:]
    
    def get_score_sheet(self):
        return self.score_sheet[:]
    
    def get_score(self):
        return self.score_sheet[Sections.TOTAL.value][0]
    
    def is_game_over(self):
        return self.rounds >= MAX_ROUNDS
    
    def get_player(self):
        return self.score_sheet[Sections.PLAYER.value]
    
    def get_available_categories(self):
        available_categories = []
        for i in range(1, len(self.score_sheet)):
            if not self.score_sheet[i][1] and i not in [Sections.YAHTZEE_BONUS.value, Sections.UPPER_SECTION_BONUS.value, Sections.TOTAL.value, Sections.PLAYER.value]:
                available_categories.append([Sections(i).value, Sections(i).name, self.get_possible_section_score(Sections(i))])
        return available_categories
    
    def score_section(self, section):
        if self.rolls == 0:
            raise Exception("You must roll the dice before scoring")
        if self.rounds >= MAX_ROUNDS:
            raise Exception("No more rounds left")
        if self.score_sheet[section.value][1]:
            raise Exception("Section already scored")
        if section == Sections.YAHTZEE_BONUS:
            raise Exception("Yahtzee bounus will be automatically calculated if applicable and the player has already scored a Yahtzee, please provide the section to score")
        if section == Sections.UPPER_SECTION_BONUS:
            raise Exception("Upper section bonus will be automatically calculated if applicable, please provide the section to score")
        
        # Calculate score based on the section
        score = 0
        dice_values = self.get_dice_values()
        
        if section in [Sections.ACE, Sections.TWO, Sections.THREE, Sections.FOUR, Sections.FIVE, Sections.SIX]:
            score = sum(d for d in dice_values if d == section.value)
        
        elif section == Sections.THREE_OF_A_KIND:
            score = sum(d for d in dice_values if any(dice_values.count(d) >= 3 for d in set(dice_values)))

        elif section == Sections.FOUR_OF_A_KIND:
            score = sum(d for d in dice_values if any(dice_values.count(d) >= 4 for d in set(dice_values)))

        elif section == Sections.FULL_HOUSE:
            if len(set(dice_values)) == 2 and any(dice_values.count(value) == 3 for value in set(dice_values)):
                score = 25
        
        elif section == Sections.SMALL_STRAIGHT:
            small_straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
            for straight in small_straights:
                if (all(d in straight for d in set(dice_values))):
                    score = 30
                    break
        
        elif section == Sections.LARGE_STRAIGHT:
            if len(set(dice_values)) == 5:
                score = 40

        elif section == Sections.YAHTZEE:
            if len(set(dice_values)) == 1:
                score = 50

        elif section == Sections.CHANCE:
            score = sum(dice_values)

        else:
            raise Exception("Invalid section")
        
        if len(set(dice_values)) == 1 and self.score_sheet[Sections.YAHTZEE.value][1]:
            self.score_sheet[Sections.YAHTZEE_BONUS.value] = (self.score_sheet[Sections.YAHTZEE_BONUS.value][0] + 100, True)

        if not self.score_sheet[Sections.UPPER_SECTION_BONUS.value][1]:
            upper_section_score = 0
            for i in [Sections.ACE, Sections.TWO, Sections.THREE, Sections.FOUR, Sections.FIVE, Sections.SIX]:
                if self.score_sheet[i.value][1]:
                    upper_section_score += self.score_sheet[i.value][0]
            if upper_section_score >= 63:
                self.score_sheet[Sections.UPPER_SECTION_BONUS.value] = (35, True)

        self.score_sheet[section.value] = (score, True)
        self.rounds += 1
        self.rolls = 0
        self.__reset_dice()

        total_score = 0
        for i in range(1, len(self.score_sheet) - 1):
            total_score += self.score_sheet[i][0]
        self.score_sheet[Sections.TOTAL.value] = (total_score, self.is_game_over())

        return self.score_sheet[:]  
    
    def get_possible_section_score(self, section):
        
        # Calculate score based on the section
        score = 0
        dice_values = self.get_dice_values()
        
        if section in [Sections.ACE, Sections.TWO, Sections.THREE, Sections.FOUR, Sections.FIVE, Sections.SIX]:
            score = sum(d for d in dice_values if d == section.value)
        
        elif section == Sections.THREE_OF_A_KIND:
            score = sum(d for d in dice_values if any(dice_values.count(d) >= 3 for d in set(dice_values)))

        elif section == Sections.FOUR_OF_A_KIND:
            score = sum(d for d in dice_values if any(dice_values.count(d) >= 4 for d in set(dice_values)))

        elif section == Sections.FULL_HOUSE:
            if len(set(dice_values)) == 2 and any(dice_values.count(value) == 3 for value in set(dice_values)):
                score = 25
        
        elif section == Sections.SMALL_STRAIGHT:
            if len(set(dice_values)) >= 4:
                score = 30
        
        elif section == Sections.LARGE_STRAIGHT:
            if len(set(dice_values)) == 5:
                score = 40

        elif section == Sections.YAHTZEE:
            if len(set(dice_values)) == 1:
                score = 50

        elif section == Sections.CHANCE:
            score = sum(dice_values)
        
        return score
    
