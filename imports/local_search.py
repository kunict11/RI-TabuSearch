import random

def initialize(distance_matrix, n):
    min_idx = 0
    solution = []
    
    solution.append(0)
    
    while True:
        i = min_idx
        min_dist = float('inf')
        
        for j in range(n):
            if distance_matrix[i][j] < min_dist and i != j and j not in solution:
                min_idx = j
                min_dist = distance_matrix[i][j]
                
        solution.append(min_idx)
        
        if len(solution) == n:
            break
    
    return solution

def evaluate_solution(solution, distance_matrix, n):
    total_distance = 0
    
    for i in range(n-1):
        current_city = solution[i]
        next_city = solution[i+1]

        total_distance += distance_matrix[current_city][next_city]
        
    total_distance += distance_matrix[solution[0]][solution[-1]]
    
    return total_distance

def modify(solution, distance_matrix, n):

    best = float('inf')
    best_sol = []
    
    for i in range(n):
        for j in range(i+1, n):
            new_solution = solution[:];
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            
            new_val = evaluate_solution(new_solution, distance_matrix, n)
            
            if new_val < best:
                best = new_val
                best_sol = new_solution

    return best_sol, best

def local_search(distance_matrix, n, num_iters):
    current_solution = initialize(distance_matrix, n)
    current_value = evaluate_solution(current_solution, distance_matrix, n)

    solution = current_solution
    best_value = current_value

    for i in range(num_iters):
        new_solution, new_value = modify(current_solution, distance_matrix, n)

        if new_value < current_value:
            current_value = new_value
            current_solution = new_solution

            if new_value < best_value:
                best_value = new_value
                solution = new_solution

    return solution, best_value
