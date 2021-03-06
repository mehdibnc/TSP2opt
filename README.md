# TSP2opt
Traveling Salesman Problem Solver. This python library gives a way to efficiently find good solutions to TSP using the 2-opt heuristic, implemented in rust. 

## Install

To install the library, run: 

`pip install tsp_2opt`

## Use 

The current version relies on the availability of a distance matrix, i.e. matrix giving pair-wise distance between cities in the TSP instance.

Here is a small example : 

```python
from tsp2opt.solver import tsp_solver
distances = [[0, 2, 3], [2, 0, 4], [3, 4, 0]]
route, length = tsp_solver(distances)
```

The solution obtained to a TSP instance after performing the 2-opt heuristic depends on the initial solution, therefore this library runs the heuristic `n` times with `n` different starting point in parralel (true parralelism is possible thanks to rust) and the best obtained is returned. You can pass `n` as a parameter to `tsp_solver()` and control the maximum number of workers :

```python
tsp_solver(distances, workers, n) 
```


Author : Mehdi Bennaceur
