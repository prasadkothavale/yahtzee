import unittest
from core import score_helper

class TestScoreHelper(unittest.TestCase):

    def test_score_upper_section(self):
        self.assertEqual(score_helper.score_upper_section([1,2,3,4,5], 1), 1)
        self.assertEqual(score_helper.score_upper_section([2,2,2,4,5], 2), 6)
        self.assertEqual(score_helper.score_upper_section([6,6,6,6,6], 6), 30)
        self.assertEqual(score_helper.score_upper_section([1,3,4,5,6], 2), 0)

    def test_score_three_of_a_kind(self):
        self.assertEqual(score_helper.score_three_of_a_kind([3,3,3,2,5]), 16)
        self.assertEqual(score_helper.score_three_of_a_kind([2,2,2,2,5]), 13)
        self.assertEqual(score_helper.score_three_of_a_kind([1,2,3,4,5]), 0)

    def test_score_four_of_a_kind(self):
        self.assertEqual(score_helper.score_four_of_a_kind([2,2,2,2,5]), 13)
        self.assertEqual(score_helper.score_four_of_a_kind([6,6,6,6,6]), 30)
        self.assertEqual(score_helper.score_four_of_a_kind([1,1,1,2,2]), 0)

    def test_score_full_house(self):
        self.assertEqual(score_helper.score_full_house([2,2,3,3,3]), 25)
        self.assertEqual(score_helper.score_full_house([5,5,5,2,2]), 25)
        self.assertEqual(score_helper.score_full_house([3,3,3,3,2]), 0)
        self.assertEqual(score_helper.score_full_house([1,2,3,4,5]), 0)

    def test_score_small_straight(self):
        self.assertEqual(score_helper.score_small_straight([1,2,3,4,6]), 30)
        self.assertEqual(score_helper.score_small_straight([2,4,3,1,6]), 30)
        self.assertEqual(score_helper.score_small_straight([2,3,4,5,2]), 30)
        self.assertEqual(score_helper.score_small_straight([5,4,3,1,6]), 30)
        self.assertEqual(score_helper.score_small_straight([3,4,5,6,3]), 30)
        self.assertEqual(score_helper.score_small_straight([5,4,3,2,1]), 30)
        self.assertEqual(score_helper.score_small_straight([1,3,4,5,6]), 0)

    def test_score_large_straight(self):
        self.assertEqual(score_helper.score_large_straight([1,2,3,4,5]), 40)
        self.assertEqual(score_helper.score_large_straight([2,4,5,3,1]), 40)
        self.assertEqual(score_helper.score_large_straight([2,3,4,5,6]), 40)
        self.assertEqual(score_helper.score_large_straight([2,4,5,3,6]), 40)
        self.assertEqual(score_helper.score_large_straight([1,2,3,4,4]), 0)
        self.assertEqual(score_helper.score_large_straight([1,1,2,3,4]), 0)

    def test_score_yahtzee(self):
        self.assertEqual(score_helper.score_yahtzee([6,6,6,6,6]), 50)
        self.assertEqual(score_helper.score_yahtzee([1,1,1,1,1]), 50)
        self.assertEqual(score_helper.score_yahtzee([2,2,2,2,3]), 0)

    def test_score_chance(self):
        self.assertEqual(score_helper.score_chance([1,2,3,4,5]), 15)
        self.assertEqual(score_helper.score_chance([6,6,6,6,6]), 30)
        self.assertEqual(score_helper.score_chance([1,1,1,1,1]), 5)

    def test_score_yahtzee_bonus(self):
        self.assertEqual(score_helper.score_yahtzee_bonus([1,1,1,1,1], True), 100)
        self.assertEqual(score_helper.score_yahtzee_bonus([2,2,2,2,2], True), 100)
        self.assertEqual(score_helper.score_yahtzee_bonus([2,2,2,2,2], False), 0)
        self.assertEqual(score_helper.score_yahtzee_bonus([2,2,2,2,3], True), 0)

if __name__ == "__main__":
    unittest.main()