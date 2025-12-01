import seaborn as sns
import matplotlib.pyplot as plt
from similarity import tanimoto_matrix

def heatmap(file_path, hname="heatmap.png",col="plasma"):
    data = tanimoto_matrix(file_path)
    plt.figure(figsize=(6, 5))
    sns.heatmap(data, annot=True, cmap=col)
    plt.savefig(hname, dpi=300, bbox_inches='tight')
