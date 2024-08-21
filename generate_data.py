import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cheese as ch

#========================================

swiss_cheese = ch.SwissCheese(num_points = 70000, dimensions=(1,1,1), max_hole_perc=0.3, hole_radius_min=0.05, hole_radius_max=0.1)
print('volume: '+ str(swiss_cheese.volume))
print('total_hole_volume: '+ str(swiss_cheese.total_hole_volume))
print('num_holes: '+ str(swiss_cheese.num_holes))

random_cube = ch.SwissCheese(num_points = 100000, dimensions=(1,1,1), max_hole_perc=0.001, hole_radius_min=0.1, hole_radius_max=0.1)
print('volume: '+ str(random_cube.volume))
print('total_hole_volume: '+ str(random_cube.total_hole_volume))
print('num_holes: '+ str(random_cube.num_holes))

df = pd.DataFrame(random_cube.data)
path = "filepath/on/my/computer/"
file_name1 = "swiss_cheese_3d_num_points_70000.csv"
file_name2 = "random_samples_3d_num_points_100000.csv"

df.to_csv(path+file_name1)
df.to_csv(path+file_name2)

#==========================================
#alternative to store numpy.ndarray as csv using numpy

# a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
# np.savetxt("foo.csv", a, delimiter=",")
