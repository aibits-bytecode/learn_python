f = open("data/originalLines.txt", "r")
wf = open("data/originalLinesWithWordCount.txt", "w")

for line in f:
    words = line.split(" ")
    wf.write(line + " words :"+str(len(words))+"\n")

wf.close()
f.close()