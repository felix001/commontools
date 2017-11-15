Provides the ability to log the input and output for a function, either directly or whether it is within class.

```
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/test.log',
                    filemode='w')

from log import class_logger, method_logger

@class_logger
class exampleclass(object):
    def __init__(self,size=False):
        self.size = size
        
    def funct1(self,weight=None):
        return weight
        
    def funct2(self,shape=None):
        return shape

@method_logger
def funct3(color=None):
    return color

>>> c = exampleclass(size=True)
>>> c.funct1(weight=123)
```

Example output ... 
```
[rick@server ~]$ cat /tmp/test.log
11-15 15:17 log          DEBUG    input_args=() input_kwargs={'size': True} return=None
11-15 15:17 log          DEBUG    input_args=() input_kwargs={'weight': 123} return=123
```
