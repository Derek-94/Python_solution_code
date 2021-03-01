print("Hello World!");

print("강한친구 대한육군");
print("강한친구 대한육군");


cat1 = "\    /\\"
cat2 = " )  ( ')"
cat3 = "(  /  )"
cat4 = " \(__)|"
print(cat1);
print(cat2);
print(cat3);
print(cat4);

dog1 = "|\_/|"
dog2 = "|q p|   /}"
dog3 = '( 0 )"""\\'
dog4 = '|"^"`    |'
dog5 = "||_/=\\\\__|"
print(dog1);
print(dog2);
print(dog3);
print(dog4);
print(dog5);

num1, num2 = map(int,(input().split()));
print(num1+num2);
print(num1-num2);
print(num1*num2);
print(num1//num2); # 몫
print(num1%num2); # 나머지

A, B, C = map(int, input().split());
print((A+B)%C);
print(((A%C) + (B%C))%C);
print((A*B)%C);
print(((A%C) * (B%C))%C);

n1 = input();
n2 = input();
print(int(n1) * int(n2[2]));
print(int(n1) * int(n2[1]));
print(int(n1) * int(n2[0]));
print(int(n1) * int(n2));