a = open("nasam1.txt","r")  # open file, read-only
b = open("nasam2.txt", "w") # open file, write
lines = a.readlines()
lines.sort()

for line in lines:
	b.write(line)
a.close()
b.close()
