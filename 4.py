def digit(x, n):    
    b = ((x % 10 ** n) - (x % 10 ** (n - 1))) / float(10 ** (n - 1))
    return b    

def nd(x):
    for i in range(50):
        if x - x % 10 ** i == 0:
	    return i
	    break

arr = range(999, 99, -1)
arr2 = [[arr[i] * arr[j] for i in range(len(arr))]for j in range(len(arr))]
for i in range(1, len(arr2)):
    for j in range(i):
	arr2[i][j] = 0

arr3 = []
flag = False
for t in arr2:
    for i in t:
        if i != 0:
            flag = False
            if nd(i) % 2 == 0:
	        for j in range(1, nd(i) / 2 + 1):
	            if digit(i, j) != digit(i, nd(i) - j + 1):
		        flag = True
         	    if flag:
	  	        break
            else:
  	        for j in range(1, int(nd(i) - 1) / 2 + 1):
	            if digit(i, j) != digit(i, nd(i) - j + 1):
		        flag = True
	            if flag:
		        break
            if flag == False:
                arr3.append(i)
	        break
#    if flag == False:
#        break

max = arr3[0]
for i in range(len(arr3)):
    if arr3[i] > max:
        max = arr3[i]
print max 
