def digit(x, n):     #returns the nth digit of x, where n=1 for ones place, n=2 for tens place, and so on
    b = ((x % 10 ** n) - (x % 10 ** (n - 1))) / float(10 ** (n - 1))
    return b    

def nd(x):                         #returns number of digits in x
    for i in range(50):
        if x - x % 10 ** i == 0:
	    return i
	    break

arr = range(999, 99, -1)                   #1d array of 999 through 100
arr2 = [[arr[i] * arr[j] for i in range(len(arr))]for j in range(len(arr))]	#2d array of all the products, with most repeated
for i in range(1, len(arr2)):   #13-15 converts arr2 into a triangular matrix, to remove the extra terms and make the program quicker
    for j in range(i):
	arr2[i][j] = 0

arr3 = []
flag = False
for t in arr2:
    for i in t:
        if i != 0:                   
            flag = False
            if nd(i) % 2 == 0:      #if no of digits are even
	        for j in range(1, nd(i) / 2 + 1):       
	            if digit(i, j) != digit(i, nd(i) - j + 1):     #inequality is more efficient here
		        flag = True
         	    if flag:
	  	        break
            else:               # no of digits odd
  	        for j in range(1, int(nd(i) - 1) / 2 + 1):
	            if digit(i, j) != digit(i, nd(i) - j + 1):
		        flag = True
	            if flag:
		        break
            if flag == False:      #if a number hasnt trigerred the inequality, it is a palindrome and will be appended to arr3
                arr3.append(i)
	        break
#    if flag == False:              #ignore this shit
#        break

max = arr3[0]            #the maximum of the array arr3
for i in range(len(arr3)):
    if arr3[i] > max:
        max = arr3[i]
print max 
