import inspect

def decorate_all_methods(decorator):
    def decorate(cls):
        for name, fn in inspect.getmembers(cls, inspect.ismethod):
            setattr(cls, name, decorator(fn))
        return cls
    return decorate
