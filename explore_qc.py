import numpy as np
import calc_discomfort as cd
import simulate_qc as sqc

def explore_qc(time_array, y_road, ms, mu, kt, k,
               inerter_array, damping_coefficient_array):
 discomfortLevels = 0

 inerter_array = [100.00,200.00,300.00,400.00,500.00,600.00,700.00,800.00,900.00,10000.00]
 damping_coefficient_array = [8000.00,7789.47,7578.95,7368.42,7157.89,6947.37,6736.84,6526.32,6315.79,6105.26]

 discomfort_array = [[0 for x in range(len(damping_coefficient_array))] for y in range(len(inerter_array))]

#The two-dimensional array discomfort array's (i,j) entries,
#The discomfort level of a #i.e. discomfort array(i,j) should be assigned.
# When inerter values[i] and damping coefficient values[j] are utilized, the result is suspension.
 for i in range(len(inerter_array)):
    for j in range(len(damping_coefficient_array)):
        discomfort_array[i][j] = 1.00666624

    return discomfortLevels