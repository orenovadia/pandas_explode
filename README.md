pandas_explode
===============================

version number: 0.0.1
author: Oren Ovadia

Overview
--------

Explode utility for Pandas dataframes (similar to UNNEST or explode in Spark)


Example
-------

```
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

```


Installation / Usage
--------------------

To install use pip:

    $ pip install pandas_explode


Or clone the repo:

    $ git clone https://github.com/orenovadia/pandas_explode.git
    $ python setup.py install
    

Publishing
----------

    $ ./publish.sh
