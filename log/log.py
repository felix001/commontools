import logging
from general.general import decorate_all_methods
from functools import wraps

logger = logging.getLogger(__name__)

def class_method_logger(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:    
            response = func(self, *args, **kwargs)
            logger.debug("input_args=%s input_kwargs=%s return=%s" % (args,kwargs,response))                     
            return response
        except Exception as exc:
            logger.exception(exc)
            raise     
    return wrapper

class_logger = decorate_all_methods(class_method_logger)

def method_logger(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            logger.debug("input_args=%s input_kwargs=%s return=%s" % (args,kwargs,response))
            return response
        except Exception as exc:
            logger.exception(exc)
            raise
    return wrapper
