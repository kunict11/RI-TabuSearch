from itertools import permutations
import pandas as pd
import time

def load_data(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        distance_matrix = [[int(j) for j in f.readline().split()] for i in range(n)]
    return n, distance_matrix


def evaluate_solution(solution, distance_matrix, n):
    total_distance = 0
    
    for i in range(n-1):
        current_city = solution[i]
        next_city = solution[i+1]

        total_distance += distance_matrix[current_city][next_city]
        
    total_distance += distance_matrix[solution[0]][solution[-1]]
    
    return total_distance


def brute_force():
    results = []
    
    datasets = {
            'five_d': { 'filepath': './sample_data/five_d.txt', 'type': 'txt', 'best_known': 19  },
            'eleven' : { 'filepath': './sample_data/eleven.txt' , 'type': 'txt', 'best_known': 253 },
    }

    for key in datasets:
        n, distance_matrix = load_data(datasets[key]['filepath'])
        array = range(n)
        best = float('inf')

        start = time.time()
        for p in permutations(array):
            eval = evaluate_solution(p, distance_matrix, n)

            if eval < best:
                best = eval
        end = time.time()

        exec_time = end - start
        diff = abs(best - datasets[key]['best_known'])*100 / datasets[key]['best_known']
        results.append([key, n, exec_time, datasets[key]["best_known"], int(best), diff])

    df = pd.DataFrame(results, columns=['Dataset', 'Number of Cities', 'Execution Time (s)', 'Best Known', 'Best Found', 'Difference (%)'])
    return df.style.hide_index()