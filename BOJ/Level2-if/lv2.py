# #1330
num1, num2 = map(int, input().split());
if(num1 > num2):
    print(">");
elif (num1 < num2):
    print("<");
else:
    print("==")

# #9498
score = int(input());
if(score >= 90 and score <= 100):
    print("A");
elif(score >= 80 and score <= 89):
    print("B");
elif(score >= 70 and score <= 79):
    print("C");
elif(score >= 60 and score <= 69):
    print("D");
else:
    print("F");

# #2753
year = int(input());
if(year % 4):
    print(0);
elif(year % 100 or not(year % 400)):
    print(1);
else:
    print(0);

# #14681
x = int(input());
y = int(input());
if(x > 0 and y > 0):
    print(1);
elif(x < 0 and y > 0):
    print(2);
elif(x < 0 and y < 0):
    print(3);
elif(x > 0 and y < 0):
    print(4);

# #2884번
hr, min = map(int, input().split());
if(min - 45 < 0):
    hr -= 1;
    min = (60 + (min - 45));
    if(hr < 0):
        hr = 23;
else:
    min -= 45;
    if(hr < 0):
        hr = 23;

print(hr,min);
