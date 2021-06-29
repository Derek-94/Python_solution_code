# Enter your code here. Read input from STDIN. Print output to STDOUT
phone_book = {};
test_case = int(input());
for i in range(test_case):
    name, num = input().split(" ")
    phone_book[name] = num;
while True:
    try:
        find_name = input();
        if find_name in phone_book:
            print(f'{find_name}={phone_book[find_name]}');
        else:
            print('Not found')
    except:
        break;