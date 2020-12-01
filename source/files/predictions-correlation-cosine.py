cos_table = Table(["x","y"])
for _ in range(200):
    from random import random
    from math import cos
    seed = random()
    cos_table = cos_table.with_row([seed,cos(12.6*seed)])