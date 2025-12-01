from rdkit.Chem import AllChem
from reader import read_smiles 
def fingerprint(file_path):
    mols = read_smiles(file_path)
    fps = []
    for mol in mols :
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
        fps.append(fp)
    return fps

