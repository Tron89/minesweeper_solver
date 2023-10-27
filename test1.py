# pylint: disable=all

import numpy as np


a = []
bombs_location = np.array(a)
location_new_bomb =np.array((1,2))
print(location_new_bomb)
bombs_location = np.append(bombs_location, location_new_bomb)
print(bombs_location)
bombs_location = np.delete(bombs_location, -1)
print(bombs_location)