
from exercise3.e3prob8 import gpt_even_odd_palindrome
from exercise3.e3p8test import check

try:
    check(gpt_even_odd_palindrome)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")