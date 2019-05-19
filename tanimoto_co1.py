import pybel
smiles = ['CCCC', 'CCCN']
mols = [pybel.readstring("/home/yobi/Documents/pytanimoto_smiles", x) for x in smiles] # Create a list of two molecules
fps = [x.calcfp() for x in mols] # Calculate their fingerprints
print (fps[0].bits, fps[1].bits)
print (fps[0] | fps[1]) # Print the Tanimoto coefficient
