user_input = input();

room = [];
funiture = [];

for i in range(int(user_input)):
    room.append(list(map(int, input())))

# 1 개짜리 넣기.
funiture.append(sum(sum(room, [])));

for i in range(1, len(room) + 1):
    sum_val = sum_square(i, room);
    funiture.append(sum_val);


def sum_square(std, room):
    sum_room = [];
    count = 0;
    for i in range(len(room) - std):
        for j in range(len(room) - std):
            
    

        