def solution(k, room_number):
    ret = []
    rooms = dict()

    for i in room_number:
        reserve = i
        while True:
            if reserve in rooms:
                reserve += 1
            else:
                rooms[reserve] = 1
                ret.append(reserve)
                break

    return ret