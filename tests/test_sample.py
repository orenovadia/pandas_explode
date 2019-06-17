import pandas as pd
from pandas_explode import explode


def test_explosion():
        df = pd.DataFrame({'s': ['a', 'b', 'c'], 'values': [[1, 2], [3, 4, 5], []]})
        exploded_df = explode(df, 'values')
        assert len(exploded_df) == 5, "Unexpected row count after explosion"


def test_col_explosion():
        df = pd.DataFrame({
                's': ['a', 'b', 'c'],
                'values': [{'col1': 1, 'col2': 2}, {'col1': 10, 'col3': 20}, {'col2': 2}],
        })
        exploded_df = explode(df, 'values', axis=1)
        assert sorted(exploded_df.columns) == ['col1', 'col2', 'col3', 's']

