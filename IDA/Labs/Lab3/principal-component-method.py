import pandas as pd
import numpy as np

def reader(filename):
    with open(filename, 'r') as file:
        datalines = file.readlines()

    data_list = [[int(x) for x in line.split()] for line in datalines]

    data = np.array(data_list)
    return data

def rationing(matrix):
    new_matrix = matrix
    row_length = len(matrix[0])

    for j in range(row_length):
        mean_j = np.mean(matrix[:, j])
        std_j = np.std(matrix[:, j])
        print(mean_j, std_j)
        for i in range(len(matrix)):
            new_matrix[i,j] = (matrix[i,j]-mean_j)/std_j

    return new_matrix

print(rationing(reader("data7.txt")))