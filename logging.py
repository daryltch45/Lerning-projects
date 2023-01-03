import logging
import math

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S', filemode='w', filename= __file__[:-2]+"log")

logger = logging.getLogger()
def quadratic_formula(a,b,c):
    """This function returns the result of a quadratic equation ax^2 + bx +c = 0."""
    logger.info(f"quadratic_formula {a}x^2 + {b}x +{c} = 0")
    #Calculate Delta
    logger.debug("#Calculate Delta")
    delta = math.sqrt(b**2 -4*a*c)
    # Compute the two roots
    logger.debug(f"# Compute the two roots")
    result1 = (-b - delta)/ (2 * a)
    result2 = (-b + delta) / (2 * a)
    # Return the root
    logger.debug("#Return the root")
    return result1,result2

print(quadratic_formula(1,2,-15))


