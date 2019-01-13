import unittest
import pandas as pd

from football import remove_dashes, get_team_name

# """
# We will test just our part of code. We will not test pandas library.
# """


class TestFunctions(unittest.TestCase):

    def test_remove_dashes_case_1(self):
        self.assertEqual(remove_dashes('1'), 1)

    def test_remove_dashes_case_2(self):
        self.assertEqual(remove_dashes('2'), 2)

    def test_remove_dashes_case_3(self):
        self.assertEqual(remove_dashes('---'), None)

    def test_get_team_name_case_1(self):
        df = pd.DataFrame(
            {'F': [9, 5, 5, 5],
             'A': [9, 9, 9, 9]},
            index=['Arsenal', 'Leeds', 'Fulham', 'Bolton']
        )
        self.assertEqual(get_team_name(df), 'Arsenal')

    def test_get_team_name_case_2(self):
        df = pd.DataFrame(
            {'F': [5, 5, 8, 5],
             'A': [9, 9, 9, 9]},
            index=['Arsenal', 'Leeds', 'Fulham', 'Bolton']
        )
        self.assertEqual(get_team_name(df), 'Fulham')

    def test_get_team_name_case_3(self):
        df = pd.DataFrame(
            {'F': [9, 9, 9, 9],
             'A': [5, 9, 5, 5]},
            index=['Arsenal', 'Leeds', 'Fulham', 'Bolton']
        )
        self.assertEqual(get_team_name(df), 'Leeds')


if __name__ == '__main__':
    unittest.main()
