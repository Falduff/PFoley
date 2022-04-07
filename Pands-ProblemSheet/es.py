import sys

fname = sys.argv[1]
#assuming the text file is in the same directory as program
l = "e"
k=0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1

print (k)