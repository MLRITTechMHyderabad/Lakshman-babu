import math

print(math.sqrt(4))

# print(math.pow(4))

# print(math.factorial(6))

# print(math.fabs(-6))

# print(math.floor(4.9))

# print(math.ceil(4))

# print(math.trunc(4))

# print(math.pi)

#logging

import logging

logging.basicConfig(level = logging.DEBUG)
logging.debug("Debug messages printed here")
logging.info("Informational values")
logging.warning("Waring messages")
logging.error("Errors")
logging.critical("Critical issues")

"""
debug is basic level for development purpose 

debug > info > warning > error > critical
"""

logging.basicConfig(level = logging.INFO)
logging.debug("Debug messages printed here")
logging.info("Informational values")
logging.warning("Waring messages")
logging.error("Errors")
logging.critical("Critical issues")

logging.basicConfig(filename = "app.log", level = logging.ERROR, format = '%(asctim)s - %(levelname)s - %(message)s')
logging.debug("Debug messages printed here")
logging.info("Informational values")
logging.warning("Waring messages")
logging.error("Errors")
logging.critical("Critical issues")

