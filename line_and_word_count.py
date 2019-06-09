
fname=input("Enter the file name ")
words=0
lines=  0
with open(fname ,'r') as f:
	for line in f:
		nwords  = line.split()
		words += len(nwords)
		lines += 1   
print(" Number of words: " ,words )
print("Number of Lines: " ,lines)
