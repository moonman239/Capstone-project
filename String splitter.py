Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
X = ["I sell seashells by the seashore.","She sells seashells by the seashore."]
>>> import pandas as pd
>>> X_pd = pd.Series(X)
>>> X_pd
0       I sell seashells by the seashore.
1    She sells seashells by the seashore.
dtype: object
>>> X_pd.get_dummies()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    X_pd.get_dummies()
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/generic.py", line 3614, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'get_dummies'
>>> pd.get_dummies(X_pd)
   I sell seashells by the seashore.  She sells seashells by the seashore.
0                                  1                                     0
1                                  0                                     1
>>> pd.get_dummies(X_pd[0])
   I sell seashells by the seashore.
0                                  1
>>> pd.get_dummies(X_pd.str.split(" "))
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 330, in __init__
    codes, categories = factorize(values, sort=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pd.get_dummies(X_pd.str.split(" "))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1215, in get_dummies
    sparse=sparse, drop_first=drop_first)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1222, in _get_dummies_1d
    codes, levels = _factorize_from_iterable(Series(data))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 2324, in _factorize_from_iterable
    cat = Categorical(values, ordered=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 332, in __init__
    codes, categories = factorize(values, sort=False)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'
>>> pd.get_dummies(X_pd[0].str.split(" "))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    pd.get_dummies(X_pd[0].str.split(" "))
AttributeError: 'str' object has no attribute 'str'
>>> X_pd
0       I sell seashells by the seashore.
1    She sells seashells by the seashore.
dtype: object
>>> pd.get_dummies(X_pd.str.split(" "))
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 330, in __init__
    codes, categories = factorize(values, sort=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pd.get_dummies(X_pd.str.split(" "))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1215, in get_dummies
    sparse=sparse, drop_first=drop_first)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1222, in _get_dummies_1d
    codes, levels = _factorize_from_iterable(Series(data))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 2324, in _factorize_from_iterable
    cat = Categorical(values, ordered=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 332, in __init__
    codes, categories = factorize(values, sort=False)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'
>>> Y = X_pd.str.split(" ")
>>> Y
0       [I, sell, seashells, by, the, seashore.]
1    [She, sells, seashells, by, the, seashore.]
dtype: object
>>> type(Y)
<class 'pandas.core.series.Series'>
>>> pd.DataFrame(Y)
                                             0
0     [I, sell, seashells, by, the, seashore.]
1  [She, sells, seashells, by, the, seashore.]
>>> pd.get_dummies(Y)
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 330, in __init__
    codes, categories = factorize(values, sort=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    pd.get_dummies(Y)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1215, in get_dummies
    sparse=sparse, drop_first=drop_first)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1222, in _get_dummies_1d
    codes, levels = _factorize_from_iterable(Series(data))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 2324, in _factorize_from_iterable
    cat = Categorical(values, ordered=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 332, in __init__
    codes, categories = factorize(values, sort=False)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'
>>> pd.get_dummies(Y[1])
   She  by  seashells  seashore.  sells  the
0    1   0          0          0      0    0
1    0   0          0          0      1    0
2    0   0          1          0      0    0
3    0   1          0          0      0    0
4    0   0          0          0      0    1
5    0   0          0          1      0    0
>>> Y[1]
['She', 'sells', 'seashells', 'by', 'the', 'seashore.']
>>> pd.get_dummies
<function get_dummies at 0x10dfe1ea0>
>>> pd.apply(get_dummies(Y))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    pd.apply(get_dummies(Y))
AttributeError: module 'pandas' has no attribute 'apply'
>>> Y.apply(get_dummies)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Y.apply(get_dummies)
NameError: name 'get_dummies' is not defined
>>> Y.apply(pd.get_dummies)
0       I  by  seashells  seashore.  sell  the
0  1...
1       She  by  seashells  seashore.  sells  the
0...
dtype: object
>>> ohe = Y.apply(pd.get_dummies)
>>> ohe
0       I  by  seashells  seashore.  sell  the
0  1...
1       She  by  seashells  seashore.  sells  the
0...
dtype: object
>>> from ipython import display
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    from ipython import display
ModuleNotFoundError: No module named 'ipython'
>>> from IPython import display
>>> display(ohe)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    display(ohe)
TypeError: 'module' object is not callable
>>> display.display(ohe)
0       I  by  seashells  seashore.  sell  the
0  1...
1       She  by  seashells  seashore.  sells  the
0...
dtype: object
>>> X = [["Do you sell seashells by the seashore?","Does she sell seashells by the seashore?"],["I sell seashells by the seashore.","She sells seashells by the seashore."]]
>>> X
[['Do you sell seashells by the seashore?', 'Does she sell seashells by the seashore?'], ['I sell seashells by the seashore.', 'She sells seashells by the seashore.']]
>>> nparray(X)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    nparray(X)
NameError: name 'nparray' is not defined
>>> pd.DataFrame(X)
                                        0  \
0  Do you sell seashells by the seashore?   
1       I sell seashells by the seashore.   

                                          1  
0  Does she sell seashells by the seashore?  
1      She sells seashells by the seashore.  
>>> X = [["Do you sell seashells by the seashore","I sell seashells by the seashore"],["Does she sell seashells by the seashore","She sells seashells by the seashore"]]
>>> pd.DataFrame(X)
                                         0  \
0    Do you sell seashells by the seashore   
1  Does she sell seashells by the seashore   

                                     1  
0     I sell seashells by the seashore  
1  She sells seashells by the seashore  
>>> Y = pd.DataFrame(X).str.split(" ")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    Y = pd.DataFrame(X).str.split(" ")
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/generic.py", line 3614, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'str'
>>> X_pd = pd.DataFrame(X)
>>> X_pd.str.split(" ")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    X_pd.str.split(" ")
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/generic.py", line 3614, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'str'
>>> Y_pd = X[0:2].str.split(" ")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    Y_pd = X[0:2].str.split(" ")
AttributeError: 'list' object has no attribute 'str'
>>> X[0:2]
[['Do you sell seashells by the seashore', 'I sell seashells by the seashore'], ['Does she sell seashells by the seashore', 'She sells seashells by the seashore']]
>>> X["0"]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    X["0"]
TypeError: list indices must be integers or slices, not str
>>> X[:2]
[['Do you sell seashells by the seashore', 'I sell seashells by the seashore'], ['Does she sell seashells by the seashore', 'She sells seashells by the seashore']]
>>> pd.Series(X).str.split(" ")
0   NaN
1   NaN
dtype: float64
>>> X.apply(lambda row: pd.get_dummies(row))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    X.apply(lambda row: pd.get_dummies(row))
AttributeError: 'list' object has no attribute 'apply'
>>> X_pd.apply(lambda row: pd.get_dummies(row))
                                                   0  \
0  (D, o,  , y, o, u,  , s, e, l, l,  , s, e, a, ...   
1  (D, o, e, s,  , s, h, e,  , s, e, l, l,  , s, ...   

                                                   1  
0  (I,  , s, e, l, l,  , s, e, a, s, h, e, l, l, ...  
1  (S, h, e,  , s, e, l, l, s,  , s, e, a, s, h, ...  
>>> X_pd
                                         0  \
0    Do you sell seashells by the seashore   
1  Does she sell seashells by the seashore   

                                     1  
0     I sell seashells by the seashore  
1  She sells seashells by the seashore  
>>> X_pd.applymap(lambda row: pd.get_dummies(row))
                                                   0  \
0     Do you sell seashells by the seashore
0    ...   
1     Does she sell seashells by the seashore
0  ...   

                                                   1  
0     I sell seashells by the seashore
0         ...  
1     She sells seashells by the seashore
0      ...  
>>> X_pd.apply(lambda x: type(x))
0    <class 'pandas.core.series.Series'>
1    <class 'pandas.core.series.Series'>
dtype: object
>>> X_pd.apply(lambda row: pd.get_dummies(row.str.split(" ")))
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 330, in __init__
    codes, categories = factorize(values, sort=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    X_pd.apply(lambda row: pd.get_dummies(row.str.split(" ")))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 4877, in apply
    ignore_failures=ignore_failures)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 4973, in _apply_standard
    results[i] = func(v)
  File "<pyshell#47>", line 1, in <lambda>
    X_pd.apply(lambda row: pd.get_dummies(row.str.split(" ")))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1215, in get_dummies
    sparse=sparse, drop_first=drop_first)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1222, in _get_dummies_1d
    codes, levels = _factorize_from_iterable(Series(data))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 2324, in _factorize_from_iterable
    cat = Categorical(values, ordered=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 332, in __init__
    codes, categories = factorize(values, sort=False)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: ("unhashable type: 'list'", 'occurred at index 0')
>>> X_pd.apply(lambda row: row.str.split(" "))
                                                 0  \
0    [Do, you, sell, seashells, by, the, seashore]   
1  [Does, she, sell, seashells, by, the, seashore]   

                                            1  
0     [I, sell, seashells, by, the, seashore]  
1  [She, sells, seashells, by, the, seashore]  
>>> Y = X_pd.apply(lambda row: row.str.split(" "))
>>> Y
                                                 0  \
0    [Do, you, sell, seashells, by, the, seashore]   
1  [Does, she, sell, seashells, by, the, seashore]   

                                            1  
0     [I, sell, seashells, by, the, seashore]  
1  [She, sells, seashells, by, the, seashore]  
>>> pd.get_dummies(Y)
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 330, in __init__
    codes, categories = factorize(values, sort=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    pd.get_dummies(Y)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1210, in get_dummies
    drop_first=drop_first)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/reshape/reshape.py", line 1222, in _get_dummies_1d
    codes, levels = _factorize_from_iterable(Series(data))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 2324, in _factorize_from_iterable
    cat = Categorical(values, ordered=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 332, in __init__
    codes, categories = factorize(values, sort=False)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'
>>> X_pd
                                         0  \
0    Do you sell seashells by the seashore   
1  Does she sell seashells by the seashore   

                                     1  
0     I sell seashells by the seashore  
1  She sells seashells by the seashore  
>>> 
