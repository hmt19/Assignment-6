def pascal_triangle(n): 
  
    # Iterate through every line 
    # and print entries in it 
    for line in range(0, n): 
  
        # Every line has number of  
        # integers equal to line  
        # number 
        for i in range(0, line + 1): 
            print(binomialCoeff(line, i), 
                  " ", end = "") 
        print() 
  
# Function to calculate nCi 
def binomialCoeff(n, i): 
    res = 1
    if(i > n - i): 
        i = n - i 
    for k in range(0 , i): 
        res = res * (n - k) 
        res = res // (k + 1) 
  
    return res 
  
# Driver Code 
n = 5
pascal_triangle(n)
