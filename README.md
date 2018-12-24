# datatable C api example

## Linux

Python: 3.6.7

Datatable: datatable-0.7.0.dev396-cp36-cp36m-linux_x86_64.whl

Ubuntu: 18.04

```py
>>> import datatable as dt
>>> d = dt.fread('example.csv')
>>> import example
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: /home/qkou/Desktop/py36/lib/python3.6/site-packages/example-0.0.1-py3.6-linux-x86_64.egg/example.cpython-36m-x86_64-linux-gnu.so: undefined symbol: DtFrame_NRows
```

## OSX

Python: 3.7.1

Datatable: datatable-0.7.0.dev396-cp37-cp37m-macosx_10_7_x86_64.whl

```py
>>> import datatable as dt
>>> d = dt.fread('example.csv')
>>> import example
>>> example.nrow(d)
10
```