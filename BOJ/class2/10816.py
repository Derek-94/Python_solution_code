import sys;
import collections;
card_total_num = int(sys.stdin.readline());
cards = list(map(int, sys.stdin.readline().split()));
check_num_count = int(sys.stdin.readline());
check_num = list(map(int, sys.stdin.readline().split()));

counter = collections.Counter(cards);
for i in check_num:
    print(counter[i], end = " ")