str = input("Input your DNA Sequence to find the methionine coding sequencences: ").strip().upper() #This may not be entirely accurate as this does not consider frameshift or point mutations.

print("The number of methionine amino acids your mrna codes for : ",str.count("AUG"))
