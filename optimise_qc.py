import numpy as np

def optimise_qc(discomfort_array,inerter_array,damping_coefficient_array,discomfort_upper_limit):
    min_inerter_index, min_coefficient_index = np.where(
        discomfort_array == np.min(discomfort_array))

    min_inerter = inerter_array[min_inerter_index[0]]

    min_damping_coefficient = damping_coefficient_array[min_coefficient_index[0]]

    max_inerter_index, max_coefficient_index = np.where(discomfort_array == np.max(discomfort_array[discomfort_array <= discomfort_upper_limit]))

    max_inerter = inerter_array[max_inerter_index[0]]

    max_damping_coefficient = damping_coefficient_array[max_coefficient_index[0]]

    return min_inerter, min_damping_coefficient, \
           max_inerter, max_damping_coefficient
