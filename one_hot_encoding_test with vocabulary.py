Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import pandas as pd
>>> X = pd.DataFrame([["Does she sell seashells by the seashore","She sells seashells by the seashore"],["Do I sell seashells by the seashore","I sell seashells by the seashore"]])
>>> vocabulary = set()
>>> X.applymap(lambda x: [vocabulary.add(string) for string in x.split(" ")])
                                            0  \
0  [None, None, None, None, None, None, None]   
1  [None, None, None, None, None, None, None]   

                                      1  
0  [None, None, None, None, None, None]  
1  [None, None, None, None, None, None]  
>>> binarizer = LabelBinarizer().fit(list(vocabulary))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    binarizer = LabelBinarizer().fit(list(vocabulary))
NameError: name 'LabelBinarizer' is not defined
>>> from sklearn.preprocessing import LabelBinarizer
>>> binarizer = LabelBinarizer().fit(list(vocabulary))
>>> binarizer.classes_
array(['Do', 'Does', 'I', 'She', 'by', 'seashells', 'seashore', 'sell',
       'sells', 'she', 'the'], dtype='<U9')
>>> X_binarized = X.applymap(lambda x: binarizer.transform(x))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    X_binarized = X.applymap(lambda x: binarizer.transform(x))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 5068, in applymap
    return self.apply(infer)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 4877, in apply
    ignore_failures=ignore_failures)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 4973, in _apply_standard
    results[i] = func(v)
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 5066, in infer
    return lib.map_infer(x.asobject, func)
  File "pandas/_libs/src/inference.pyx", line 1521, in pandas._libs.lib.map_infer
  File "<pyshell#8>", line 1, in <lambda>
    X_binarized = X.applymap(lambda x: binarizer.transform(x))
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/preprocessing/label.py", line 330, in transform
    y_is_multilabel = type_of_target(y).startswith('multilabel')
  File "/Users/montana/miniconda3/lib/python3.6/site-packages/sklearn/utils/multiclass.py", line 244, in type_of_target
    'got %r' % y)
ValueError: ("Expected array-like (array or non-string sequence), got 'Does she sell seashells by the seashore'", 'occurred at index 0')
>>> X_binarized = X.applymap(lambda x: binarizer.transform(x.split(" "))
			 )
>>> X.applymap(lambda x: binarizer.inverse_transform(binarizer.transform(x.split(" "))))
                                                 0  \
0  [Does, she, sell, seashells, by, the, seashore]   
1      [Do, I, sell, seashells, by, the, seashore]   

                                            1  
0  [She, sells, seashells, by, the, seashore]  
1     [I, sell, seashells, by, the, seashore]  
>>> X_binarized.applymap(lambda x: binarizer.inverse_transform(x))
                                                 0  \
0  [Does, she, sell, seashells, by, the, seashore]   
1      [Do, I, sell, seashells, by, the, seashore]   

                                            1  
0  [She, sells, seashells, by, the, seashore]  
1     [I, sell, seashells, by, the, seashore]  
>>> Y = pd.Series(X[1])
>>> Y_binarized = Y.apply(lambda x: binarizer.transform(x.split(" ")))
>>> Y_binarized.apply(binarizer.inverse_transform)
0    [She, sells, seashells, by, the, seashore]
1       [I, sell, seashells, by, the, seashore]
Name: 1, dtype: object
>>> 
