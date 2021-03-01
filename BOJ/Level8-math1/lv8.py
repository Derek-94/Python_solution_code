# #1712
# fix, move, price = map(int, input().split());
# if price - move <= 0:
#     print(-1);
# else:
#     print(fix // (price - move) + 1);

# #2292
roomNum = int(input());
layer = 1;
cmp = 1;
while roomNum > cmp:
    cmp += (6 * layer);
    layer += 1;
print(layer);