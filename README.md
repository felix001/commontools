# commontools
commontools is set of tools to help with common tasks

# installation

```
sudo pip install git+https://github.com/rickd3/commontools.git
sudo pip install git+ssh://git@github.com/rickd3/commontools.git
```

# convert.py

```
get_ranges([1,2,3,4,5,6])
# ['1-6']

get_list(["1-6"])
# [1, 2, 3, 4, 5, 6]

list_lists =  [["apples", "bananas", "pears", "orange"],
               ["123", "12453", "125454", "21332"]]
to_table(list_lists)
# apples |bananas   |pears  |orange       |
# 123    |12453     |125454 |21332        |
```

# log.py
Allows you to log the input and output for each function.

```
from log import class_logger,method_logger

@class_logger
class exampleclass(object):
    def __init__(self,size=False):
        self.size = size
        
    def funt1(self,weight=None):
        return weight
        
    def funt2(self,shape=None):
        return shape

@method_logger
def funt3(color=None):
    return color
```

Example output ... 
```
10-08 23:27 root         DEBUG    input_args=() input_kwargs={} return=None
10-08 23:27 root         DEBUG    input_args=() input_kwargs={'weight': 333} return=333
```
