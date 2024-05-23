from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        d = deque()
        n = len(nums)
        max_window = list()
        i =0
        while(i<k):
            while( len(d)!=0 and nums[d[-1]] <= nums[i]):
                d.pop()
            d.append(i)
            i +=1
        
        while(i<n):
            max_window.append(nums[d[0]])
            
            #remove out of window element
            while( len(d)!=0 and d[0] <= i-k):
                d.popleft()

            # remove smallest element in k window
            while( len(d)!=0 and nums[d[-1]] <= nums[i]):
                d.pop()
            d.append(i)
            i +=1

        max_window.append(nums[d[0]])
        return max_window
if __name__ == "__main__":
    nums = [1,3,1,2,0,5]
    k = 3
    obj = Solution()
    print(obj.maxSlidingWindow(nums, k))
