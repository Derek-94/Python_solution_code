import sys;

card_cnt, target = map(int, sys.stdin.readline().split());
cards = list(map(int, sys.stdin.readline().split()));
result = 0;
for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            if cards[i] + cards[j] + cards[k] > target:
                continue;
            else:
                result = max(result, cards[i] + cards[j] + cards[k]);

print(result)