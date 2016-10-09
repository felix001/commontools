import logging
from functools import wraps

def log_class_function(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.debug("input args=%s kwargs=%s" % (str(args),str(kwargs)))
        response = func(self, *args, **kwargs)
        logging.debug("return=%s", str(response))
        return response
    return wrapper

def log_function(func):
    def wrapper(*args, **kwargs):
        logging.debug("input args=%s kwargs=%s" % (str(args),str(kwargs)))
        response = func(*args, **kwargs)
        logging.debug("return=%s", str(response))
        return response
    return wrapper

log = decorate_all_methods(log_decorator)
