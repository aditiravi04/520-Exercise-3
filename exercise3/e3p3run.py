
from exercise3.e3prob3 import gpt_mean_absolute_deviation
from exercise3.e3p3test import check

try:
    check(gpt_mean_absolute_deviation)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")