Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
from pandas import DataFrame,Series
>>> X = pd.DataFrame([[["apples","pears","oranges"],["guava","strawberry","passion"]]])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    X = pd.DataFrame([[["apples","pears","oranges"],["guava","strawberry","passion"]]])
NameError: name 'pd' is not defined
>>>  X = DataFrame([[["apples","pears","oranges"],["guava","strawberry","passion"]]])
 
SyntaxError: unexpected indent
>>> X = DataFrame([[["apples","pears","oranges"],["guava","strawberry","passion"]]])
>>> df[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    df[0]
NameError: name 'df' is not defined
>>> X
                          0                             1
0  [apples, pears, oranges]  [guava, strawberry, passion]
>>> tags = X[0].apply(pd.Series)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tags = X[0].apply(pd.Series)
NameError: name 'pd' is not defined
>>> tags = X[0].apply(Series)
>>> tags
        0      1        2
0  apples  pears  oranges
>>> tags = tags.rename(columns = lambda x: 'tag_'+str(x))
>>> tags
    tag_0  tag_1    tag_2
0  apples  pears  oranges
>>> tags.get_dummies()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tags.get_dummies()
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/generic.py", line 3614, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'get_dummies'
>>> from pandas import get_dummies
>>> get_dummies(tags)
   tag_0_apples  tag_1_pears  tag_2_oranges
0             1            1              1
>>> from sklearn.preprocessing import MultiLabelBinarizer()
SyntaxError: invalid syntax
>>> from sklearn.preprocessing import MultiLabelBinarizer
>>> binarizer = MultiLabelBinarizer().fit(tags)
>>> binarizer.classes_
array(['0', '1', '2', '_', 'a', 'g', 't'], dtype=object)
>>> binarizer = MultiLabelBinarizer().fit(tags.values)
>>> binarizer.classes_
array(['apples', 'oranges', 'pears'], dtype=object)
>>> binarizer.transform(tags)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    binarizer.transform(tags)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 765, in transform
    yt = self._transform(y, class_to_index)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 789, in _transform
    indices.extend(set(class_mapping[label] for label in labels))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 789, in <genexpr>
    indices.extend(set(class_mapping[label] for label in labels))
KeyError: 't'
>>> binarizer.transform(tags.values)
array([[1, 1, 1]])
>>> X = DataFrame([[["apples","pears","oranges"],["guava","strawberry","passion"]],[["bananas","grapes","grapefruit"],["agave","acai","blueberry"]]])
>>> X
                               0                             1
0       [apples, pears, oranges]  [guava, strawberry, passion]
1  [bananas, grapes, grapefruit]      [agave, acai, blueberry]
>>> df.applymap(pd.Series)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    df.applymap(pd.Series)
NameError: name 'df' is not defined
>>> X.applymap(pd.Series)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    X.applymap(pd.Series)
NameError: name 'pd' is not defined
>>> X.applymap(Series)
                                                   0  \
0  0     apples
1      pears
2    oranges
dtype: ...   
1  0       bananas
1        grapes
2    grapefrui...   

                                                   1  
0  0         guava
1    strawberry
2       passio...  
1  0        agave
1         acai
2    blueberry
d...  
>>> X[0].apply(Series)
         0       1           2
0   apples   pears     oranges
1  bananas  grapes  grapefruit
>>> get_dummies(X[0].apply(Series))
   0_apples  0_bananas  1_grapes  1_pears  2_grapefruit  2_oranges
0         1          0         0        1             0          1
1         0          1         1        0             1          0
>>> get_dummies(Series([["apples","bananas","oranges"],["grapes","pears","grapefruit"]]))
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/categorical.py", line 330, in __init__
    codes, categories = factorize(values, sort=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/algorithms.py", line 471, in factorize
    labels = table.get_labels(values, uniques, 0, na_sentinel, check_nulls)
  File "pandas/_libs/hashtable_class_helper.pxi", line 1367, in pandas._libs.hashtable.PyObjectHashTable.get_labels
TypeError: unhashable type: 'list'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    get_dummies(Series([["apples","bananas","oranges"],["grapes","pears","grapefruit"]]))
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
>>> get_dummies(Series(DataFrame([["apples","bananas","oranges"],["grapes","pears","grapefruit"]])))
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/common.py", line 399, in _asarray_tuplesafe
    result[:] = values
ValueError: could not broadcast input array from shape (2,3) into shape (2)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    get_dummies(Series(DataFrame([["apples","bananas","oranges"],["grapes","pears","grapefruit"]])))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/series.py", line 264, in __init__
    raise_cast_failure=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/series.py", line 3277, in _sanitize_array
    subarr = _asarray_tuplesafe(data, dtype=dtype)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/common.py", line 402, in _asarray_tuplesafe
    result[:] = [tuple(x) for x in values]
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/common.py", line 402, in <listcomp>
    result[:] = [tuple(x) for x in values]
TypeError: 'int' object is not iterable
>>> Y = Series(DataFrame([["apples","bananas","oranges"],["grapes","pears","grapefruit"]]))
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/common.py", line 399, in _asarray_tuplesafe
    result[:] = values
ValueError: could not broadcast input array from shape (2,3) into shape (2)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    Y = Series(DataFrame([["apples","bananas","oranges"],["grapes","pears","grapefruit"]]))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/series.py", line 264, in __init__
    raise_cast_failure=True)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/series.py", line 3277, in _sanitize_array
    subarr = _asarray_tuplesafe(data, dtype=dtype)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/common.py", line 402, in _asarray_tuplesafe
    result[:] = [tuple(x) for x in values]
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/common.py", line 402, in <listcomp>
    result[:] = [tuple(x) for x in values]
TypeError: 'int' object is not iterable
>>> X[0] = pd.Series([["apples","oranges","pears"],["bananas","grapes","grapefruit"]])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    X[0] = pd.Series([["apples","oranges","pears"],["bananas","grapes","grapefruit"]])
NameError: name 'pd' is not defined
>>> X[0] = Series([["apples","oranges","pears"],["bananas","grapes","grapefruit"]])
>>> X[0]
0         [apples, oranges, pears]
1    [bananas, grapes, grapefruit]
Name: 0, dtype: object
>>> X[0].apply(Series)
         0        1           2
0   apples  oranges       pears
1  bananas   grapes  grapefruit
>>> get_dummies(X[0].apply(Series))
   0_apples  0_bananas  1_grapes  1_oranges  2_grapefruit  2_pears
0         1          0         0          1             0        1
1         0          1         1          0             1        0
>>> 
