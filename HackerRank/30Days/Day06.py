# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case = int(input());
for i in range(test_case):
    str_input = str(input());
    even, odd = '', '';
    for i in range(len(str_input)):
        if i % 2 == 0:
            even += str_input[i];
        else:
            odd += str_input[i];
    print(even, odd)