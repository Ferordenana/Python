# [0,1,1,2,3,5, .....] 

def fibo(quantity):
    fibonacci_list = [0,1]
    for i in range(2, quantity): 
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list

print(fibo(12))
