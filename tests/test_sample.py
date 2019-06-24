from unittest import TestCase

import pandas as pd

from pandas_explode import explode


class ExplodeTests(TestCase):
    def test_row_explosion(self):
        df = pd.DataFrame({'s': ['a', 'b', 'c'], 'values': [[1, 2], [3, 4, 5], []]})
        exploded_df = explode(df, 'values')
        self.assertEqual(5, len(exploded_df), "Unexpected row count after explosion")
        self.assertEqual(list(range(1, 6)), exploded_df['values'].tolist())

    def test_col_explosion(self):
        df = pd.DataFrame({
            's': ['a', 'b', 'c'],
            'values': [{'col1': 1, 'col2': 2}, {'col1': 10, 'col3': 20}, {'col2': 2}],
        })
        exploded_df = explode(df, 'values', axis=1)
        self.assertSequenceEqual(['col1', 'col2', 'col3', 's'], sorted(exploded_df.columns))
