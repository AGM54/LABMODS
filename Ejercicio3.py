import numpy as np
from scipy.optimize import linear_sum_assignment
cost_matrix_i = np.array([
    [3, 8, 2, 10],
    [6, 5, 2, 7],
    [6, 4, 7, 5],
    [8, 4, 2, 5],
    [7, 8, 6, 7]
])

cost_matrix_ii = np.array([
    [3, 9, 2, 7],
    [6, 1, 5, 6],
    [9, 4, 7, 10],
    [2, 5, 4, 1],
    [9, 6, 2, 6]
])

def resolver_asignacion(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_ind, col_ind].sum()
    assignment = list(zip(row_ind + 1, col_ind + 1))  
    return assignment, total_cost

# Solución para el modelo (i)
asignacion_i, costo_total_i = resolver_asignacion(cost_matrix_i)
print(f"Asignación óptima para el modelo (i): {asignacion_i}")
print(f"Costo total para el modelo (i): {costo_total_i}")

# Solución para el modelo (ii)
asignacion_ii, costo_total_ii = resolver_asignacion(cost_matrix_ii)
print(f"Asignación óptima para el modelo (ii): {asignacion_ii}")
print(f"Costo total para el modelo (ii): {costo_total_ii}")
