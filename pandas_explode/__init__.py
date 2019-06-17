import pandas as pd


def explode(df, column, axis=0):
    """

    :param df: Dataframe
    :param column: Column of sequences to explode
    :param axis : {0/'index', 1/'columns'}, default 0
        The axis to concatenate along
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
    >>> df = pd.DataFrame({'s': ['a', 'b', 'c'], 'values': [{'col1': 1, 'col2': 2}, {'col1': 10, 'col3': 20}, {'col2': 2}]})
    >>> df
       s                    values
    0  a    {'col1': 1, 'col2': 2}
    1  b  {'col1': 10, 'col3': 20}
    2  c               {'col2': 2}
    >>> explode(df, 'values', axis=1)
       s  col1  col2  col3
    0  a   1.0   2.0   NaN
    1  b  10.0   NaN  20.0
    2  c   NaN   2.0   NaN

    """

    def row_evolve(series, value):
        series = series.copy()
        series[column] = value
        return series

    def explode_rows(df, column):
        return pd.DataFrame(row_evolve(row, v)
                        for i, row in df.iterrows() for v in row[column]
                        )

    def explode_columns(df, column):
        return pd.concat((df.drop(columns=column), df[column].apply(pd.Series)), axis=1)

    # Standardize axis parameter to int
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Only DataFrame is supported for explode functionality."
                         " Input was of type {input_type}".format(input_type=type(df)))
    else:
        axis = df._get_axis_number(axis)

    if not 0 <= axis <= 1:
        raise AssertionError("axis must be either 0 ('index') or 1 ('columns'), input was"
                             " {axis}".format(axis=axis))

    result = explode_rows(df, column) if axis==0 else explode_columns(df, column)
    return result


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
