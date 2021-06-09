user_input = input();

time_slot = [];

for i in range(int(user_input)):
    input_tmp = input();
    time_slot.append(input_tmp);

start_time_slot = [];
end_time_slot = [];

for time in time_slot:
    time_tmp = time[0:2] + time[3:5];
    start_time_slot.append(time_tmp);
    time_tmp = time[8:10] + time[11:];
    end_time_slot.append(time_tmp);

start_time_slot.sort();
end_time_slot.sort();

max_start = start_time_slot[len(start_time_slot) - 1]
min_end = end_time_slot[0];

if start_time_slot[len(start_time_slot) - 1] > end_time_slot[0]:
    print(-1);
else:
    print(f'{max_start[0:2]}:{max_start[2:4]} ~ {min_end[0:2]}:{min_end[2:4]}')

