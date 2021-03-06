import numpy as np 


def check_type(distances):
    """ 
    """
    if isinstance(distances, np.ndarray):
        distances = distances.astype(np.float64)
        return distances.tolist()
    elif isinstance(distances, list):
        map(lambda x : np.float64(x), distances)
        return distances
    raise TypeError(f"Expected distances matrix to be of type list or np.ndarray but got {type(distances)} instead.")


def compute_cost(route: list, distances: np.ndarray) -> float:
    """ Computes the cost of a route according to distances matrix
        between n cities.

        Args:
            route: permutation of 1..n, with first element appended to the end.
            distances: distance matrix, array-like

        Returns:
            c: route distance.
    """
    c = 0
    for i in range(1, len(route)):
        c += distances[int(route[i-1])][int(route[i])]
    c += distances[int(route[-1])][int(route[0])]
    return c

def get_best_from_batch(routes: list, distances: np.ndarray):
    """  
    """
    lengths = [None]*len(routes)
    for i in range(len(routes)):
        lengths[i] = compute_cost(routes[i], distances)
    best_id = np.argmin(lengths)
    return routes[best_id], lengths[best_id]

def get_init_route(nodes: int, seed: int):
    """ 
    """
    np.random.seed(seed)
    init_route = np.random.permutation(nodes)
    init_route = init_route.astype(np.int32)
    init_route = init_route.tolist()
    init_route.append(init_route[0])
    return init_route

def is_symmetric(distances):
    """ Indicates whether distances is symmetric.
    """
    return np.allclose(np.array(distances), np.array(distances).T)
