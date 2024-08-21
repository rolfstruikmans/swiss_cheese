import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cheese as ch

#========================================

#Read the Data from .csv file
path = "filepath/on/my/computer/"
file_name_random = "random_samples_3d_num_points_100000.csv"
file_name_cheese = "swiss_cheese_3d_num_points_70000.csv"
df = pd.read_csv(path+file_name_cheese, names = ['x', 'y', 'z'], header=0)
# print(df.head(10))

#set filepath for storage
path = "filepath/on/my/computer/"

#make a slice
n = 100  # number of slices
delta = 1/n

for i in range(n):
    step = delta*i
    filter = (step <= df.x) & (df.x < (step + delta))
    df_slice = df.loc[filter,:].loc[:,['y','z']]

    file_name = f"slice_of_swiss_cheese[{i}-{n}]"
    # file_name = f"slice_of_random_cube[{i}-{n}]"
    #save the slice
    file_name_csv = file_name + '.csv'
    df_slice.to_csv(path+file_name_csv)
    #plot the slice
    color_random = 'C0'
    color_cheese = 'yellow'
    color = color_cheese
    plt.scatter(df_slice.y, df_slice.z, s=80, alpha = 0.5, c = color)
    #save the plot
    file_name_plot = file_name + '.png'
    plt.savefig(path + file_name_plot)
    plt.close()

#plot the last slice
plt.scatter(df_slice.y, df_slice.z, s=80, alpha = 0.5, c = color)
plt.show()
#========================================

#convert dataframe to numpy array and filter numpy array
# arr = df.to_numpy()
# filtered_arr = arr[arr[:,2] < 0.00008]

#Sort by column
# dfx = df.sort_values(by=['x'], ascending=True)
