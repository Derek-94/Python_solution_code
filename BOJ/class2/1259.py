while True:
    input_num = input();
    if input_num == "0":
        break;
    input_num_reverse = input_num[::-1];
    if input_num == input_num_reverse:
        print("yes");
    else:
        print("no");