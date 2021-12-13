# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    mul_result_bin = bin(A * B);
    return mul_result_bin.count('1');