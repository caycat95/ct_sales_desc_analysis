import main
import unittest
import pandas as pd
# from pandas.util.testing import assert_frame

df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df2 = pd.DataFrame({'a': [4, 10, 25, 1, 3], 'b': [1, 0, 34, 1, 78]})


class TestStatisticsMethods(unittest.TestCase):
    def test_calc_min(self):
        self.assertEqual(main.calc_min(df1, 'a'), 1)
        self.assertEqual(main.calc_min(df1, 'b'), 3)
        self.assertEqual(main.calc_min(df2, 'a'), 1)
        self.assertEqual(main.calc_min(df2, 'b'), 0)


if __name__ == '__main__':
    unittest.main()
