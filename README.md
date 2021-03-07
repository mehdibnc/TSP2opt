# Traveling Salesman Problem (TSP) Solver
This python library gives a solver to efficiently find good sub-optimal solutions to the TSP. It uses the [2-opt heuristic](https://en.wikipedia.org/wiki/2-opt) and the search part is implemented in rust. 

## Install

To install the library, run: 

`pip install tsp_2opt`

For now, the library is working only on MacOS X platforms.

## Use 

The current version relies on the availability of a distance matrix, i.e. matrix giving pair-wise distance between cities in the TSP instance.

Here is a small example : 

```python
from tsp_2opt.solver import tsp_solver
distances = [[0, 2, 3], [2, 0, 4], [3, 4, 0]]
route, length = tsp_solver(distances)
```

The solution obtained to a TSP instance after performing the 2-opt heuristic depends on the initial solution (starting point of the search), therefore this library runs the heuristic `n` times with `n` different starting point in parralel (true parallelism is possible thanks to rust) and the best obtained is returned. You can pass `n` as a parameter to `tsp_solver()` and control the maximum number of workers :

```python
tsp_solver(distances, workers, n) 
```
