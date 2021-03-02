from concurrent.futures import ThreadPoolExecutor
from lib2opt import solver_2opt_parr
from utils import get_best_from_batch, get_init_route, is_symmetric, check_type
import numpy as np 
import time 


def tsp_solver(distances: np.ndarray, workers: int = 5, r: int = 10):
    """ 
    """
    #-- Check input type
    distances = check_type(distances)
    #-- Check symmetry
    symmetric = is_symmetric(distances)
    executor = ThreadPoolExecutor(max_workers=workers)
    nodes = len(distances)
    solutions = [None] * r
    #--
    for i in range(r):
        #-- Seed for reproducibility
        init_route = get_init_route(nodes, seed=i)
        future = executor.submit(
            solver_2opt_parr, init_route, distances, symmetric
        )
        solutions[i] = future
    #--
    for i in range(r):
        solutions[i] = solutions[i].result()
    #-- Retrieve best solution
    best, length = get_best_from_batch(solutions, distances)
    return best, length
    
