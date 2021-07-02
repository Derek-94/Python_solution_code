garden = [0] * 20;
needed_fountain = 0;
def fountainActivation(start, end):
    global needed_fountain
    global garden;

    if garden[start] == 0 and garden[end] != 0:
        for i in range(start, end + 1):
            garden[i] += 1;
        needed_fountain += 1;
    elif garden[start] != 0 and garden[end] == 0:
        for i in range(start, end + 1):
            garden[i] += 1;
        needed_fountain += 1;
    elif garden[start] == 0 and garden[end] == 0:
        if sum(garden[start + 1:end]) > 0:
            tmp = max(garden[start + 1:end]);
            for i in range(start, end + 1):
                garden[i] += 1;
            # needed_fountain += 1; ... REPLACE!
            print("included.")
            needed_fountain -= tmp;
        else:
            for i in range(start, end + 1):
                garden[i] += 1;
            needed_fountain += 1;
            
    print(garden)
    return needed_fountain

fountainActivation(3, 8);
fountainActivation(5, 9);
fountainActivation(2, 6);
fountainActivation(1, 10);

