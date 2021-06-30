def fibonacci(n):

    # Write your code here.
    # arr = [0] * 30;
    # arr[0] = 0;
    # arr[1] = 1;
    
    # if n <= 1:
    #     return arr[n];
    
    # for i in range(2, n + 1):
    #     arr[i] = arr[i - 1] + arr[i - 2];
    # return arr[n]
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);    
    
n = int(input())
print(fibonacci(n))
