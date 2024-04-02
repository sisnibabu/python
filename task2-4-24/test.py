import logging

logging.basicConfig(level = logging.DEBUG, filename='log12.txt', filemode = 'a',  format="%(asctime)s - %(levelname)s -%(message)s")

a = int(input("Enter a first number"))
b = int(input("Enter the second number"))

if (a>b):
    print(a-b)
elif (b>a):
    logging.warning("The number 1 is less than number 2")
    logging.debug("Change the number2")
else:
    logging.critical("The given number is not numeric")

value=int(input("Enter:"))
if value >= 0:
    logging.info("Value is positive: {}".format(value))
else:
    logging.error("Value is non-positive: {}".format(value))