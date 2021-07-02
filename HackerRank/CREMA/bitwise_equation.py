def calculate(sum_target, xor_target):
    x = 0;
    while x < sum_target:
        y = sum_target - x;
        if bin(xor_target) == bin(x ^ y):
            #print(x, y);
            return x, y;
        if x == sum_target - 1:
            #print("End. not found.")
            return 0, 0;
        else:
            #print("increasing...")
            x += 1;

def bitwiseEquations(a, b):
    # Write your code here
    results = [];
    for i in range(len(a)):
        x, y = calculate(a[i], b[i]);
        results.append(2 * x + 3 * y);
    return results;