import main
import unittest
import pandas as pd
import os

df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df2 = pd.DataFrame({'a': [4, 10, 25, 1, 3], 'b': [1, 0, 34, 1, 78]})


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
    def test_calc_min(self):
        self.assertEqual(main.calc_min(df1, 'a'), 1)
        self.assertEqual(main.calc_min(df1, 'b'), 3)
        self.assertEqual(main.calc_min(df2, 'a'), 1)
        self.assertEqual(main.calc_min(df2, 'b'), 0)


if __name__ == '__main__':
    unittest.main()
