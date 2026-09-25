with open("notes.txt","r")as f:
    print(f.read())
    print(f.readline())
    print(f.readlines())
with open("notes.txt","r")as f:
    for lines in f:
        print(lines)