words_count = input();

words = [];

for i in range(int(words_count)):
    tmp = input();
    if tmp not in words:
        words.append(tmp);

words.sort(key = lambda x: (len(x), x));

for i in words:
    print(i);