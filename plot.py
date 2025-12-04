import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.manifold import MDS

def heatmap(data, labels=None,col="plasma", l =25):
    plt.figure(figsize=(l, l))

    sns.clustermap(data, annot=True, cmap=col, figsize=(l, l))
    plt.savefig( "plot.png",dpi=300, bbox_inches='tight')




def tanimoto_hist(data, name):
    matrix = np.array(data)
    
    sims = matrix[np.triu_indices(len(matrix), k=1)]

    plt.figure(figsize=(8,5))
    plt.hist(sims, bins=20, density=True, alpha=0.7)
    plt.xlabel("Tanimoto Similarity")
    plt.ylabel("Density")
    plt.title("Tanimoto Similarity Distribution (Histogram)")
    plt.grid(alpha=0.3)
    plt.savefig(name, dpi=300, bbox_inches='tight')