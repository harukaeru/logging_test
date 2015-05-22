import logging

# a kind of decorators (merely execute a function decorated statements of logging)
def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(" '%s' function is working" % (func.__name__))
        logging.info(' Starting')
        func(*args, **kwargs)
        logging.info(' Finishing')
    return wrapper
