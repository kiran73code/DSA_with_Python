from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    start = 0
    total_gain = 0
    cur_gain = 0
    n = len(gas)

    for i in range(0, n):
        total_gain +=  gas[i] - cost[i]
        cur_gain += gas[i]- cost[i]

        if cur_gain < 0 :
            cur_gain =0 
            start = i + 1
    
    if total_gain >=0:
        return start
    else:
        return -1
    
if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(canCompleteCircuit(gas, cost))