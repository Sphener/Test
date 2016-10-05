import numpy as np
def py(n):		
    for i in range(1, n + 1):
	for j in range(1, n + 1):
	    if i <= j:			#to avoid calculating pairs of (i,j) and (j,i) differently
		k = np.sqrt(i ** 2 + j ** 2)
		if k % 1 == 0:
		    if i + j + int(k) == 1000:
			print (i, j, int(k))
			return

py(1000)	#arbitrarily chosen argument. Chossing smaller will make the program quite faster, but it must not be less than 375
