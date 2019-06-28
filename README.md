[![Build Status](https://travis-ci.org/orenovadia/pandas_explode.svg?branch=master)](https://travis-ci.org/orenovadia/pandas_explode)

# pandas_explode

author: Oren Ovadia

## Overview

Explode utility for Pandas dataframes (similar to `UNNEST` or `explode`)


## Examples

```python
import pandas as pd 
import pandas_explode 
pandas_explode.patch() # adds a `df.explode` method to all DataFrames 

df = pd.DataFrame({'s': ['a', 'b', 'c'], 'values': [[1, 2], [3, 4, 5], []]})
df
#    s     values
# 0  a     [1, 2]
# 1  b  [3, 4, 5]
# 2  c         []
df.explode('values')
#    s  values
# 0  a       1
# 0  a       2
# 1  b       3
# 1  b       4
# 1  b       5

df = pd.DataFrame({'s': ['a', 'b', 'c'], 'values': [{'col1': 1, 'col2': 2}, {'col1': 10, 'col3': 20}, {'col2': 2}]})
df
#    s                    values
# 0  a    {'col1': 1, 'col2': 2}
# 1  b  {'col1': 10, 'col3': 20}
# 2  c               {'col2': 2}
df.explode('values', axis=1)
#    s  col1  col2  col3
# 0  a   1.0   2.0   NaN
# 1  b  10.0   NaN  20.0
# 2  c   NaN   2.0   NaN
df.explode('values', axis=1, record_prefix=True)
#    s  values.col1  values.col2  values.col3
# 0  a          1.0          2.0          NaN
# 1  b         10.0          NaN         20.0
# 2  c          NaN          2.0          NaN

```


## Installation / Usage

To install use pip:

    $ pip install pandas_explode


Or clone the repo:

    $ git clone https://github.com/orenovadia/pandas_explode.git
    $ python setup.py install
    

## Publishing

    $ ./publish.sh
