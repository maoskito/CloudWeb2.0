#-*- coding: UTF-8 -*-
import random

def random_float(a,b):
    v = round(random.uniform(a, b))
    return str(v)

def random_int(a,b):
    return str(random.randint(a, b))

