# pylint: disable=all


import numpy as np

probability_map = np.zeros((3,3))
probability_map[1,1] += 1
probability_map[1,1] += 2
print(probability_map)