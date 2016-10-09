import logging
from functools import wraps

def class_method_logger(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.debug("input args=%s kwargs=%s" % (str(args),str(kwargs)))
        response = func(self, *args, **kwargs)
        logging.debug("return=%s", str(response))
        return response
    return wrapper

def method_logger(func):
    def wrapper(*args, **kwargs):
        logging.debug("input args=%s kwargs=%s" % (str(args),str(kwargs)))
        response = func(*args, **kwargs)
        logging.debug("return=%s", str(response))
        return response
    return wrapper

class_logger = decorate_all_methods(class_method_logger)
