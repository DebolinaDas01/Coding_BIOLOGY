seq = input("Enter your Nucleotide sequence as text: ").strip().upper() #Enter the sequence as text in one line.
if not set(seq).issubset({'A', 'T', 'C', 'G'}): # Checks and verifies for valid nucleotide sequences only.
    print("Invalid nucleotide sequence. Please enter a sequence containing only A, T, C, and G.")   
else:
    print("Length of your nucleotide sequence is: ", len(seq)) #Prints the length of the sequence entered by the user after removal of spaces.

