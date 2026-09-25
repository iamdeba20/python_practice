with open("notes.txt", "r") as infile, open("upper.txt", "w") as outfile:
    for line in infile:
        if line.lower().startswith("a"):
            outfile.write(line.upper())
with open("upper.txt","a")as f:
    f.write("ALL DONE.\n")