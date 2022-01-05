class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        if sum(gas) < sum(cost): # we will run out of gas at some point
            return -1
		# It means we have a solution
		# We need to calculate the index where the sum is minimum because from that index we will never run out of gas
		# We will just return calculated index + 1
        curr_sum = 0
        minim = float("inf")
        for i in range(n):
            curr_sum += gas[i]-cost[i]
            if curr_sum < minim:
                minim = curr_sum
                index = i
        if index + 1 == n: # if minimum sum is at the last index
            return 0
        else:
            return index + 1
