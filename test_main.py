import main
import unittest
import pandas as pd
import os
import numpy as np

from pandas.testing import assert_frame_equal

df1 = pd.DataFrame({'a': [1, 2, 1], 'b': [3, 4, 3]})
df2 = pd.DataFrame({'a': [4, 10, 25, 1, 3], 'b': [1, 0, 34, 1, 78]})
df3 = pd.DataFrame({'Total': [12.3, 56.7, 34.6],
                    'gross income': [4.5, 23.3, 12.4]})
df4 = pd.DataFrame({'gross income': [100.02, 456.3, 25.75],
                    'Total': [3.5, 4.6, 10.1]})
df5 = pd.DataFrame({'gross income': [100.09, 345.9, 23.8789],
                    'Total': [10.7, 34.5, 89.001]})
df6 = pd.DataFrame({'Total': [45.6, 23.089, 75.6],
                    'gross income': [506.987, 23.567, 456.789]})


class TestCSVMethods(unittest.TestCase):
    def test_pd_read_csv(self):
        df1.to_csv('df1.csv')
        df2.to_csv('df2.csv')

        result1 = main.pd_read_csv('df1.csv')
        result2 = main.pd_read_csv('df2.csv')

        with open("test.txt", "w") as f:
            f.write("This is not a csv file.")
            f.close()

        self.assertIsInstance(result1, pd.DataFrame)
        self.assertIsInstance(result2, pd.DataFrame)
        self.assertRaises(FileNotFoundError, main.pd_read_csv,
                          'doesnotexist.csv')
        self.assertRaises(ValueError, main.pd_read_csv, 'test.txt')

        os.remove('df1.csv')
        os.remove('df2.csv')
        os.remove('test.txt')


class TestStatisticsMethods(unittest.TestCase):
    def test_calc_total_profit(self):
        self.assertEqual(main.calc_total_profit(df3), 40.2)
        self.assertEqual(main.calc_total_profit(df4), 582.07)
        self.assertEqual(main.calc_total_profit(df5), 469.86)
        self.assertEqual(main.calc_total_profit(df6), 987.34)

    def test_calc_total_rev(self):
        self.assertEqual(main.calc_total_rev(df3), 103.60)
        self.assertEqual(main.calc_total_rev(df4), 18.20)
        self.assertEqual(main.calc_total_rev(df5), 134.20)
        self.assertEqual(main.calc_total_rev(df6), 144.28)

    def test_calc_min(self):
        self.assertEqual(main.calc_min(df1, 'a'), 1)
        self.assertEqual(main.calc_min(df1, 'b'), 3)
        self.assertEqual(main.calc_min(df2, 'a'), 1)
        self.assertEqual(main.calc_min(df2, 'b'), 0)

    def test_calc_max(self):
        self.assertEqual(main.calc_max(df1, 'a'), 2)
        self.assertEqual(main.calc_max(df1, 'b'), 4)
        self.assertEqual(main.calc_max(df2, 'a'), 25)
        self.assertEqual(main.calc_max(df2, 'b'), 78)


class TestDataGrabMethods(unittest.TestCase):
    def test_get_column_values(self):
        self.assertEqual(main.get_column_values(df1, 'a').tolist(), [1, 2])
        self.assertEqual(main.get_column_values(df1, 'b').tolist(), [3, 4])
        self.assertEqual(main.get_column_values(df2, 'a').tolist(),
                         [4, 10, 25, 1, 3])
        self.assertEqual(main.get_column_values(df2, 'b').tolist(),
                         [1, 0, 34, 78])

    def test_get_column_rows(self):
        test_pd1 = pd.DataFrame({'a': [1, 1], 'b': [3, 3]})
        test_pd2 = pd.DataFrame({'a': [4, 1], 'b': [1, 1]})

        np.array_equal(main.get_column_rows(
            df1, 'b', 3).values, test_pd1.values)
        np.array_equal(main.get_column_rows(
            df2, 'b', 1).values, test_pd2.values)


if __name__ == '__main__':
    unittest.main()
