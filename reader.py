from rdkit import Chem

def read_smiles(file_path):
    mols = []
    with open(file_path, 'r') as f:
        for line in f:
            mol = Chem.MolFromSmiles(line)
            mols.append(mol)
    return mols
