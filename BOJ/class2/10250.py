import sys;
test_case = int(sys.stdin.readline());

for i in range(test_case):
    h, w, guest = map(int, sys.stdin.readline().split());
    if guest % h == 0:
        room_num = guest // h;
    else: 
        room_num = guest // h + 1;
    floor_num = guest % h;
    print(f'{floor_num if floor_num != 0 else h}{room_num if len(str(room_num)) == 2 else "0"+ str(room_num)}')
