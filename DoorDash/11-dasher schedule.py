# You're a dasher, and you want to try planning out your schedule. You can view a list of deliveries along with their associated start time, end time, and dollar amount for completing the order. Assuming dashers can only deliver one order at a time, determine the maximum amount of money you can make from the given deliveries.

# The inputs are as follows:

# int start_time: when you plan to start your schedule
# int end_time: when you plan to end your schedule
# int d_starts[n]: the start times of each delivery[i]
# int d_ends[n]: the end times of each delivery[i]
# int d_pays[n]: the pay for each delivery[i]
# The output should be an integer representing the maximum amount of money you can make by forming a schedule with the given deliveries.

# Example #1
# start_time = 0
# end_time = 10
# d_starts = [2, 3, 5, 7]
# d_ends = [6, 5, 10, 11]
# d_pays = [5, 2, 4, 1]
# Expected output: 6

# https://leetcode.com/problems/maximum-profit-in-job-scheduling/ Need to check for start and end condition as well

# ================
# The key insights to keep in mind for this question are:

# sort and process the intervals by end time ascending,
# search the dp backwards to find the compatible entry when computing the current max for dp[i],
# optimize the look-back into dp by using a list of tuples instead of an array, and
# binary-search instead of scanning (since the dp items will be monotonically increasing).

# ================
# FOLLOW UP 1: Get the jobs you selected

# In the DP array, instead of just storing max profit for a given index, also store which intervals led to that max profit. This will be either be [currInterval, nextAvailableInterval], or [nextImmediateInterval] -- since these are the 2 choices we made in the DP solution.

# After you have finished with the DP, you end up with something like the following DP array:

# 0: [20, [0,3]] --> index 0 has max profit of 20, and used profits from indices 0,3 in to get there
# 1: ...
# 2: ...
# 3: [10, [4]] --> index 3 has max profit of 10, and used interval 4 to get it
# 4: [10, [4]] --> index 4 used itself to get max profit of 4
# ...
# You can follow through the indices and collect which values were used. If the current index is in the list of intervals used, add it to the solution. Continue checking for the remaining index in the list.

# 0: [0,3] --> add 0 to jobs since index == 0. go to index 3
# 3: [4] --> 3 is missing from intervals, so don't add it. go to index 4
# 4: [4] --> add 4 to jobs since index == 4. No other items used, so terminate

# jobs = [0,4]
# This is O(n) operation. You can also do this during the DP itself rather than getting the selected jobs at the end

# ================
# FOLLOW UP 2: SCALE FOR N ORDERS

# SIMPLE SOLUTION:

# run the scheduler once -> remove the jobs that yield max profit -> run the scheduler a second time with the remaining jobs -> remove the jobs -> ... -> repeat until we get k overlaps

# CONFUSING SOLUTION (ORIGINAL):

# At each interval, we select the max profit from 3 possible choices:

# Ignore the current interval, and get the value from the immediate next interval (allowing k overlaps)
# Include the current interval, and get the value from the next non-overlapping interval (allowing k overlaps)
# Include the current interval, and solve the suproblem for each overlapping interval (allowing k - 1 overlaps)
# 3.5 If there are no overlapping intervals, it means we can treat the current interval as the new starting point. So, just return dp[current][k_orig] -- where k_orig is the original max overlaps allowed for the subproblem.
# Note that options 1 and 2 are almost identical to the original problem, where no overlap is allowed.

# Through this recursion, we will end up trying a bunch of combos to get the max profit. I think the solution could definitely be optimized, but I think its OK in terms of correctness.

# CODE (it uses the same template as https://leetcode.com/problems/maximum-profit-in-job-scheduling/, and N is specified inside the function)

import bisect

class Solution:

    def jobScheduling(self, startTime, endTime, profit) -> int:       
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[0])
        starts = [j[0] for j in jobs]

        # n is the number of jobs you can have running concurrently
        n = 1

        dp = [[0] * (n) for _ in range(len(jobs))]
        for i in reversed(range(len(jobs))):
            overlapping_indices = [j for j in range(i+1, len(jobs)) if jobs[j][0] < jobs[i][1]]
            
            # we solve the suproblem for all k from 0 to N - 1, where k is the number of overlaps allowed
            for k in range(n):
                dp[i][k] = self.subproblem(starts, jobs, i, k, k, dp, overlapping_indices)

        # dp contains max profit at each interval, for 0 to N-1 overlaps
        return max(dp[0])

    def subproblem(self, starts, jobs, i, k, k_orig, dp, overlapping_indices):        
        # option 1: ignore curr and get the immediate next for k overlaps
        max_profit1 = dp[i+1][k] if i + 1 < len(jobs) else 0

        # option 2: curr + next_index that doesn't overlap, allowing for k overlaps
        next_index = bisect.bisect_left(starts, jobs[i][1])
        next_profit = dp[next_index][k] if next_index < len(jobs) else 0
        max_profit2 = jobs[i][2] + next_profit
        
        # option 3: curr + max_overlapping_subproblem, keeping track of k-1 overlaps relative to original allowed.
        max_profit3 = jobs[i][2]
        if k and overlapping_indices:
            # for each overlapping index, use the overlapping index, and try remaining overlaps (recursion) for k - 1.
            # Since we recurse, this will try the other cases as well

            max_remaining = 0
            for j in range(len(overlapping_indices)):
                profit = self.subproblem(starts, jobs, overlapping_indices[j], k-1, k_orig, dp, overlapping_indices[j+1:]) 
                max_remaining = max(max_remaining, profit)

            max_profit3 += max_remaining

        # option 3.5: if there are no overlapping with respect to the original, we reset the problem, starting at curr_index
        elif not overlapping_indices:
            max_profit3 = dp[i][k_orig]

        return max(max_profit1, max_profit2, max_profit3)
