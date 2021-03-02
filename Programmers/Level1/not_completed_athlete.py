import collections

def solution(participant, completion):
    # for name in completion:
        # del participant[name]; // not in string.
        # participant.remove(name) // timeout
        
        # index = participant.index(name);
        # del participant[index];  // timeout
        
    participant_counter = collections.Counter(participant);
    completion_counter = collections.Counter(completion);
    c = participant_counter - completion_counter;    
    
    return list(c)[0]
