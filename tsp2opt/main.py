from solver import tsp_solver
import numpy as np 
import time 



# dist_matrix = np.loadtxt("tsp2opt/data/tsp_48_33523.txt")
nodes = 1000
cost_mat = np.random.randint(100, size=(nodes, nodes))
cost_mat += cost_mat.T
np.fill_diagonal(cost_mat, 0)
dist_matrix = cost_mat.astype(np.float64).tolist()
start = time.time()
route, length = tsp_solver(dist_matrix)
print(f"Found route of length {length} in {time.time() - start} seconds.")



