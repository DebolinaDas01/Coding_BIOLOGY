seq_file = input("Enter file name in .txt containing mRNA sequence: ")

with open(seq_file, "r") as seq_data:
    seq_res = seq_data.read().upper().strip()
    pos = seq_res.find("AGGAGG") +1

    print("Position of your shine dalgarno sequence is=", pos) #Position is read from the right using 1-based indexing. There may still be false positives or negetives, still a work in progress.
  
