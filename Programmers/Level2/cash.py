import collections;
def solution(cacheSize, cities):
    answer = 0;
    cash = collections.deque();
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower();
        if city in cash:
            #print(city, "는 cash에 있다.")
            #print("현재 cash 상태는", cash);
            answer += 1;
            cash.remove(city);
            cash.append(city);
            #print("====조종 후 cash는====", cash);
        else:
            #print("없다. miss다.")
            answer += 5;
            if len(cash) < cacheSize:
                #print("아직 여유가 있으니 걍 넣자.")
                cash.append(city);
                #print("====조종 후 cash는====", cash);
            else:
                #print("====꽉찼다.====")
                cash.popleft();
                cash.append(city);
                #print("====조종 후 cash는====", cash);
            
    
    
    return answer