import numpy as np

import math

latitudes = [53.557078, 48.858363, 39.562553, 36.156214, -22.971177, 21.281004, -28.002695]
np_latitudes = np.array(latitudes)
longitudes = [10.023109, 2.294481, 2.661947, -115.148736, -43.182543, -157.837456, 153.431781]
np_longitudes = np.array(longitudes)
print(np_longitudes)


locations = ['HAW Hamburg', 'Eiffel Tower', 'Palma de Mallorca', 'Las Vegas', 'Copacabana', 'Waikiki Beach', 'Surfer’s Paradise']
np_locations = np.array(locations)
print(np_locations)



del_y = 111.3 * abs(np_latitudes[0] - np_latitudes[1])
del_x = 111.3 * math.cos((math.radians(np_latitudes[0]) + math.radians(np_latitudes[1])) / 2) * abs (math.radians(np_longitudes[0]) - math.radians(np_longitudes[1]))

print(del_x)
print(del_y)

distance = math.sqrt((del_x ** 2) + (del_y ** 2))

print("The Distance between ", np_locations[0], " and ", np_locations[1], " is: ")

print(distance)
