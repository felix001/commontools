import logging
from general import decorate_all_methods
from functools import wraps

def class_method_logger(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:    
            logging.debug("input args=%s kwargs=%s" % (str(args),str(kwargs)))
            response = func(self, *args, **kwargs)
            logging.debug("return=%s", str(response))
            return response
        except Exception as exc:
            logging.exception(exc)
            raise     
    return wrapper

def method_logger(func):
    def wrapper(*args, **kwargs):
        try:
            logging.debug("input args=%s kwargs=%s" % (str(args),str(kwargs)))
            response = func(*args, **kwargs)
            logging.debug("return=%s", str(response))
            return response
        except Exception as exc:
            logging.exception(exc)
            raise
    return wrapper

class_logger = decorate_all_methods(class_method_logger)
