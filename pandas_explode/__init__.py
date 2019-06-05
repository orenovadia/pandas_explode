import pandas as pd


def explode(df, column):
    """

    :param df: Dataframe
    :param column: Column of sequences to explode
    >>> df = pd.DataFrame({'s': ['a', 'b', 'c'], 'values': [[1, 2], [3, 4, 5], []]})
    >>> df
       s     values
    0  a     [1, 2]
    1  b  [3, 4, 5]
    2  c         []
    >>> explode(df, 'values')
       s  values
    0  a       1
    0  a       2
    1  b       3
    1  b       4
    1  b       5
    """

    def row_evolve(series, value):
        series = series.copy()
        series[column] = value
        return series

    return pd.DataFrame(row_evolve(row, v)
                        for i, row in df.iterrows() for v in row[column]
                        )


def patch():
    """
    Patch `pandas.Dataframe` with an `explode` method:
    >>> df = pd.DataFrame([{'s': 'a', 'values': [1, 2]}])
    >>> patch()
    >>> df.explode('values')
       s  values
    0  a       1
    0  a       2

    """
    pd.DataFrame.explode = explode


if __name__ == '__main__':
    import doctest
    doctest.testmod()
