from fingerprint import fingerprint
from rdkit import DataStructs
import csv 

def tanimoto_matrix(file_path):
    fps = fingerprint(file_path)
    n = len(fps)
    matrix = [[0.0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = DataStructs.TanimotoSimilarity(fps[i], fps[j])
    # saving
    out_file = "tanimoto_matrix.csv"
    with open(out_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        
        writer.writerow([""] + [f"Mol_{i}" for i in range(n)])
         
        for idx, row in enumerate(matrix):
            writer.writerow([f"Mol_{idx}"] + row)
    return matrix


def matrix_length(file_path):
    fps = fingerprint(file_path)
    n = len(fps)
    return n 