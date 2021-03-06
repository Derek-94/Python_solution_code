key_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]
]

def find_index(number):
    for i in range(4):
        for j in range(3):
            if key_pad[i][j] == number:
                return i, j;

def judge(press, left_hand_loc, right_hand_loc, hand):
    x, y = find_index(press);
    if press in [1, 4, 7]:
        return "L", x, y;
    elif press in [3, 6, 9]:
        right_loc = [x, y];
        return "R", x, y;
    else:
        left_distance = abs(left_hand_loc[0] - x) + abs(left_hand_loc[1] - y);
        right_distance = abs(right_hand_loc[0] - x) + abs(right_hand_loc[1] - y);
        if left_distance > right_distance:
            return "R", x, y;
        elif left_distance < right_distance:
            return "L", x, y;
        else:
            return hand, x, y

def solution(numbers, hand):
    answer = '';
    hand_move = "";
    if hand == "right":
        hand = "R";
    else:
        hand = "L"
    
    left_hand_loc = [3, 0];
    right_hand_loc= [3, 2];
    
    for press_num in numbers:
        hand_move, nextX, nextY = judge(press_num, left_hand_loc, right_hand_loc, hand);
        if hand_move == "L":
            left_hand_loc = [nextX, nextY];
        else:
            right_hand_loc = [nextX, nextY];
        answer += hand_move;
    
    return answer