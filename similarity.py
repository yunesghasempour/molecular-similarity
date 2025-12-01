from fingerprint import fingerprint
from rdkit import DataStructs

def tanimoto_matrix(file_path):
    fps = fingerprint(file_path)
    n = len(fps)
    matrix = [[0.0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = DataStructs.TanimotoSimilarity(fps[i], fps[j])

    return matrix


