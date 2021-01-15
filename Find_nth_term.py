#Finding nth term of fibbo series
FiboArray = [0,1] 
  
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FiboArray): 
        return FiboArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FiboArray.append(temp_fib) 
        return temp_fib 
  
# Runner
  
print(fibonacci(n)) # In the bracket where is written type the number you want to find the nth term of the series