def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge_state = [0 for i in range(bridge_length)];
    
    while True:
        if len(truck_weights) > 0:
            truck = truck_weights[0];
            #print(bridge_state)
            #print(truck, "차례다.")

            if truck + sum(bridge_state) > weight:
                # 옮기고 다시.
                bridge_state.insert(0,0);
                bridge_state.pop();
                #print("넘 무거워서 그냥 다리위 트럭만 옮겼다",bridge_state)
                
                if truck_weights[0] + sum(bridge_state) < weight:
                    bridge_state.insert(0, truck_weights.pop(0));
                    bridge_state.pop();
                    #print("옮겼는데 다음 대기 트럭이 바로 올라올 수 있어 올라왔다.")

                answer += 1;
            else:
                bridge_state.insert(0, truck_weights.pop(0));
                bridge_state.pop();
                #print("새 트럭이 올라왔다.",bridge_state)
                answer += 1;
        elif sum(bridge_state) > 0:
            #print("대기 트럭은 없다. 다리위 트럭만 움직이자.")
            bridge_state.insert(0,0);
            bridge_state.pop();
            #print(bridge_state)
            answer += 1;
        else:
            break;
            
    return answer