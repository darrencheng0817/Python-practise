class Solution(object):
    def twoSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
        #data structure -> hashmap = <target - element, index> = <needed, index>
        hashmap = {}
        for index in range(0, len(nums)):
            item = nums[index]
            if item not in hashmap:
                hashmap[target - item] = index
            else:
                return[hashmap[item]+1, index+1]
