file = input("Enter filename (.txt) containing Template DNA sequence: ")
with open(file, "r") as dna_file:
    seq = dna_file.read().strip().upper()

table = seq.maketrans({
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G"
})
fin_seq = seq.translate(table)

print(fin_seq)
