# import numpy as np 
import lib2opt
import numpy as np 

nodes = 10
init_route = np.arange(nodes)
init_route = init_route.astype(np.int32)
init_route = init_route.tolist()
print(init_route)
cost_mat = np.random.randint(100, size=(nodes, nodes))
cost_mat = cost_mat.astype(np.float64)
cost_mat += cost_mat.T
np.fill_diagonal(cost_mat, 0)
cost_mat = cost_mat.tolist()
print(cost_mat)

print("\n Starting solver.... \n")

lib2opt.solver_2opt(init_route, cost_mat)
