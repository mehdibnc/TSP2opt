from solver import tsp_solver
import numpy as np 
import time 



# nodes = 48
# init_route = np.random.permutation(nodes)
# init_route = init_route.astype(np.int32)
# init_route = init_route.tolist()
# init_route.append(init_route[0])

dist_matrix = np.loadtxt("tsp2opt/data/tsp_48_33523.txt")
start = time.time()
route, length = tsp_solver(dist_matrix)
print(f"Found route of length {length} in {time.time() - start} seconds.")

# dist_matrix = dist_matrix.astype(np.float64)
# dist_matrix= dist_matrix.tolist()
# symmetric = False 
# print("\n Starting solver.... \n")

# executor = ThreadPoolExecutor(max_workers=2)


# # route = lib2opt.solver_2opt(init_route, dist_matrix)


# future_1 = executor.submit(
#     lib2opt.solver_2opt_parr, init_route, dist_matrix, symmetric
# )
# init_route = np.random.permutation(nodes)
# init_route = init_route.astype(np.int32)
# init_route = init_route.tolist()
# init_route.append(init_route[0])

# future_2 = executor.submit(
#     lib2opt.solver_2opt_parr, init_route, dist_matrix, symmetric
# )

# start = time.time()
# result_1 = future_1.result()
# result_2 = future_2.result()
# print(f"Solution 1 cost : {compute_cost(result_1, dist_matrix)}")
# print(f"Solution 2 cost : {compute_cost(result_2, dist_matrix)}")
# print(f"Time : {time.time() - start}.")





