Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
from sklearn.preprocessing import MultiLabelBinarizer
>>> import pandas as pd
>>> X = pd.DataFrame([["I have 12345678 tomatoes"],["12345678"]],columns=["answer_text","context"])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    X = pd.DataFrame([["I have 12345678 tomatoes"],["12345678"]],columns=["answer_text","context"])
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 369, in __init__
    arrays, columns = _to_arrays(data, columns, dtype=dtype)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 6284, in _to_arrays
    dtype=dtype)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 6363, in _list_to_arrays
    coerce_float=coerce_float)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 6420, in _convert_object_array
    'columns' % (len(columns), len(content)))
AssertionError: 2 columns passed, passed data had 1 columns
>>> X = pd.DataFrame([["I have 12345678 tomatoes","12345678"],columns=["answer_text","context"])
		 
SyntaxError: invalid syntax
>>> X = pd.DataFrame(["I have 12345678 tomatoes","12345678"],columns=["answer_text","context"])
Traceback (most recent call last):
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/internals.py", line 4622, in create_block_manager_from_blocks
    placement=slice(0, len(axes[0])))]
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/internals.py", line 2957, in make_block
    return klass(values, ndim=ndim, fastpath=fastpath, placement=placement)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/internals.py", line 2082, in __init__
    placement=placement, **kwargs)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/internals.py", line 120, in __init__
    len(self.mgr_locs)))
ValueError: Wrong number of items passed 1, placement implies 2

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    X = pd.DataFrame(["I have 12345678 tomatoes","12345678"],columns=["answer_text","context"])
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 385, in __init__
    copy=copy)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 533, in _init_ndarray
    return create_block_manager_from_blocks([values], [columns, index])
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/internals.py", line 4631, in create_block_manager_from_blocks
    construction_error(tot_items, blocks[0].shape[1:], axes, e)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/internals.py", line 4608, in construction_error
    passed, implied))
ValueError: Shape of passed values is (1, 2), indices imply (2, 2)
>>> x=pd.DataFrame(["I have 12345678 tomatoes","12345678"])
>>> x
                          0
0  I have 12345678 tomatoes
1                  12345678
>>> x=pd.DataFrame([["I have 12345678 tomatoes"],["12345678"])
	       
SyntaxError: invalid syntax
>>> x=pd.DataFrame([["I have 12345678 tomatoes"],["12345678"]])
>>> x
                          0
0  I have 12345678 tomatoes
1                  12345678
>>> x.T
                          0         1
0  I have 12345678 tomatoes  12345678
>>> x=pd.DataFrame([["I have 12345678 tomatoes","12345678"]])
>>> x
                          0         1
0  I have 12345678 tomatoes  12345678
>>> binarizer = MultiLabelBinarizer.fit(x)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    binarizer = MultiLabelBinarizer.fit(x)
TypeError: fit() missing 1 required positional argument: 'y'
>>> binarizer = MultiLabelBinarizer.fit(x[0])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    binarizer = MultiLabelBinarizer.fit(x[0])
TypeError: fit() missing 1 required positional argument: 'y'
>>> binarizer = MultiLabelBinarizer.fit(x[0],x[1])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    binarizer = MultiLabelBinarizer.fit(x[0],x[1])
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 696, in fit
    if self.classes is None:
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/generic.py", line 3614, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'classes'
>>> binarizer = MultiLabelBinarizer().fit(x)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    binarizer = MultiLabelBinarizer().fit(x)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 697, in fit
    classes = sorted(set(itertools.chain.from_iterable(y)))
TypeError: 'int' object is not iterable
>>> binarizer = MultiLabelBinarizer().fit(x.values)
>>> binarizer.classes_
array(['12345678', 'I have 12345678 tomatoes'], dtype=object)
>>> binarizer = MultiLabelBinarizer().fit(x[0])
>>> binarizer = MultiLabelBinarizer().fit(x[0].str.split(" "))
>>> binarizer.transform("12345678")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    binarizer.transform("12345678")
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 765, in transform
    yt = self._transform(y, class_to_index)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 789, in _transform
    indices.extend(set(class_mapping[label] for label in labels))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 789, in <genexpr>
    indices.extend(set(class_mapping[label] for label in labels))
KeyError: '1'
>>> binarizer.transform(["12345678"])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    binarizer.transform(["12345678"])
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 765, in transform
    yt = self._transform(y, class_to_index)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 789, in _transform
    indices.extend(set(class_mapping[label] for label in labels))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 789, in <genexpr>
    indices.extend(set(class_mapping[label] for label in labels))
KeyError: '1'
>>> binarizer.transform(x[1]))
SyntaxError: invalid syntax
>>> binarizer.transform(x[1])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    binarizer.transform(x[1])
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 765, in transform
    yt = self._transform(y, class_to_index)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 789, in _transform
    indices.extend(set(class_mapping[label] for label in labels))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 789, in <genexpr>
    indices.extend(set(class_mapping[label] for label in labels))
KeyError: '1'
>>> binarizer.classes_
array(['12345678', 'I', 'have', 'tomatoes'], dtype=object)
>>> 
