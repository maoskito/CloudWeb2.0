#-*- coding: UTF-8 -*-
import random

def random_float(a, b, accuracy=2):
    v = round(random.uniform(a, b),accuracy)
    return str(v)

def random_int(a,b):
    return str(random.randint(a, b))