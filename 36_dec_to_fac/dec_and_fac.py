import logging
import math

logging.basicConfig(
    level=logging.DEBUG,
    format=" %(asctime)s [%(name)s %(lineno)s] %(levelname)s -> %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("dec_and_fac.log"),
        logging.StreamHandler()
    ]
)

logging.debug("starting run")




def make_fact_dict():
    """
    calculates and stores factorials

    :return: a dictionary of integers and their factorials
    """
    d = {}
    for i in range(10):
        d[i] = math.factorial(i)
        logging.debug(f"calculating factorial number {i}")
    return d


def dec2FactString(nb):
    d = make_fact_dict()
    s = ""
    vals = sorted(list(d.values()), reverse=True)
    x = nb
    for val in vals:

        if val < nb:
            div = x // val
            rem = nb % val
            s = s + str(div)
            x = rem
    return s


def factString2Dec(string):
    pass


