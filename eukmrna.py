stra = input("Enter your mRNA Transcript sequence: ").strip().upper() #Paste your transcript in a single line
print("Is your string an eukaryotic sequence: ",stra.endswith("AAAAAAAAA")) #This looks for poly A tail as a signal to recognize eukaryotic mRNA
