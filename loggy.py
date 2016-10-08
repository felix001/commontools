import logging
import inspect
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.debug("input args=%s kwargs=%s" % (str(args),str(kwargs)))
        response = func(self, *args, **kwargs)
        logging.debug("return=%s", str(response))
        return response
    return wrapper

def decorate_all_methods(decorator):
    def decorate(cls):
        for name, fn in inspect.getmembers(cls, inspect.ismethod):
            setattr(cls, name, decorator(fn))
        return cls
    return decorate

log = decorate_all_methods(log_decorator)
