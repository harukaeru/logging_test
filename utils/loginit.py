import logging
import argparse

# create the parser
parser = argparse.ArgumentParser()

# set the parameter to the parser for getting an argument
parser.add_argument("--loglevel","-l", default="INFO", help="Set level of log message")

# parsing in it
args = parser.parse_args()

# assign the argument value to loglevel
loglevel = args.loglevel

# get the real number of logging.{loglevel} (e.g. logging.DEBUG, logging.INFO)
numeric_level = getattr(logging, loglevel.upper(), None)

# if parsing is failed, then raise an Error
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

# initial config for logging
logging.basicConfig(level=numeric_level)
