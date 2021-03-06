use pyo3::prelude::*;
use pyo3::wrap_pyfunction;



pub fn compute_route_cost(route: &Vec<i32>, distances: &Vec<Vec<f64>>) -> f64 {
    // Computes the cost (length) of route according to distances matrix
    let mut cost: f64 = 0.0;
    for i in 1..route.len() {
        cost += distances[route[i-1] as usize][route[i] as usize];
    }
    return cost;
}

#[pyfunction]
fn solver_2opt(route: Vec<i32>, distances: Vec<Vec<f64>>, symmetric: bool) -> PyResult<Vec<i32>> {
    // Implement 2-opt local search starting from route
    let mut best: Vec<i32> = route.clone(); // best sol
    let mut compbest: Vec<i32> = route.clone(); // best sol companion
    let mut improved: bool = true; // monitor improvement
    let mut cost_change: f64 = 0.0; // change in cost at each iteration
    let mut best_cost: f64 = compute_route_cost(&route, &distances);
    let mut candidate_cost: f64;
    while improved {
        improved = false;
        for i in 1..route.len() - 2 {
            for j in i+1..route.len(){
                if j - i == 1 {
                    continue;
                }
                if symmetric {
                    cost_change = distances[best[i-1] as usize][best[j-1] as usize] + distances[best[i] as usize][best[j] as usize] - distances[best[i-1] as usize][best[i] as usize] - distances[best[j-1] as usize][best[j] as usize];
                    if cost_change < 0.0 {
                        for k in 0..j-i {
                            best[i+k as usize] = compbest[j-1-k as usize];
                        }
                        improved = true;
                        compbest.clone_from_slice(&best);
                    }
                }
                else {
                    for k in 0..j-i {
                        compbest[i+k as usize] = best[j-1-k as usize];
                    }
                    candidate_cost = compute_route_cost(&compbest, &distances);
                    if candidate_cost < best_cost {
                        best_cost = candidate_cost;
                        best.clone_from_slice(&compbest);
                        improved = true;
                    }
                    else {
                        compbest.clone_from_slice(&best);
                    }

                }
            }
        }
        
    }
    Ok(best.to_vec()) 
}

#[pyfunction]
fn solver_2opt_parr(py: Python, route: Vec<i32>, distances: Vec<Vec<f64>>, symmetric: bool) -> PyResult<Vec<i32>>  {
    py.allow_threads(|| solver_2opt(route, distances, symmetric))
}



#[pymodule]
fn tsp_2opt(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(solver_2opt))?;
    m.add_wrapped(wrap_pyfunction!(solver_2opt_parr))?;
    Ok(())
}


// Some tests
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn cost_computation() {
        let route: Vec<i32> = vec![0, 1, 2, 0];
        let distances: Vec<Vec<f64>> = vec![vec![0.0, 2.0, 3.0], vec![2.0, 0.0, 4.0], vec![3.0, 4.0, 0.0]];
        let dist = compute_route_cost(&route, &distances);
        assert_eq!(dist, 9.0);
    }
}

